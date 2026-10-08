"""Pruebas del motor de process-atlas: despliegue, idempotencia, registro de códigos y hooks.

Cada prueba trabaja sobre una copia temporal del repositorio (.claude/ y
00_Recursos_metodologia/), nunca sobre el repositorio real. Solo biblioteca estándar.

Uso: python -m unittest discover -s tests -v
"""
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
EJEMPLO = os.path.join(REPO, 'ejemplos', 'panaderia')
IGNORAR = shutil.ignore_patterns('__pycache__', '.state', 'settings.local.json')
MARCADOR = re.compile(r'\{\{[A-Z][A-Z0-9_]*\}\}')


class Base(unittest.TestCase):
    con_ejemplo = True

    def setUp(self):
        self.tmp = tempfile.mkdtemp(prefix='process_atlas_')
        for carpeta in ('.claude', '00_Recursos_metodologia'):
            shutil.copytree(os.path.join(REPO, carpeta), os.path.join(self.tmp, carpeta), ignore=IGNORAR)
        if self.con_ejemplo:
            for nombre in ('00_Perfil_organizacion.md', '00_Mapa_procesos.md'):
                shutil.copy(os.path.join(EJEMPLO, nombre), self.ruta('00_Recursos_metodologia', 'Metodologia', nombre))

    def tearDown(self):
        shutil.rmtree(self.tmp, ignore_errors=True)

    def ruta(self, *partes):
        return os.path.join(self.tmp, *partes)

    def leer(self, *partes):
        with open(self.ruta(*partes), encoding='utf-8') as f:
            return f.read()

    def ejecutar(self, script, *args, entrada=None):
        r = subprocess.run([sys.executable, self.ruta('.claude', *script.split('/'))] + list(args),
                           input=(json.dumps(entrada) if entrada is not None else '').encode('utf-8'),
                           capture_output=True, cwd=self.tmp)
        return r.returncode, r.stdout.decode('utf-8', errors='replace')

    def desplegar(self, *args):
        return self.ejecutar('scripts/desplegar_sistema.py', *args)

    def hook(self, nombre, ruta):
        codigo, salida = self.ejecutar('hooks/' + nombre, entrada={'tool_input': {'file_path': ruta}})
        self.assertEqual(codigo, 0)
        return json.loads(salida) if salida.strip() else {}

    def escribir_con_hooks(self, ruta, texto):
        """Simula la tool Write: hook previo, escritura y hook posterior. Devuelve (pre, post)."""
        pre = self.hook('pre_escritura.py', ruta)
        if pre.get('hookSpecificOutput', {}).get('permissionDecision') == 'deny':
            return pre, None
        os.makedirs(os.path.dirname(ruta), exist_ok=True)
        with open(ruta, 'w', encoding='utf-8') as f:
            f.write(texto)
        return pre, self.hook('post_escritura.py', ruta)

    def marcadores_restantes(self):
        restantes = []
        perfil = self.ruta('00_Recursos_metodologia', 'Metodologia', '00_Perfil_organizacion.md')
        for base in ('.claude', '00_Recursos_metodologia'):
            for dirpath, _, filenames in os.walk(self.ruta(base)):
                for n in filenames:
                    r = os.path.join(dirpath, n)
                    if n.endswith('.md') and os.path.abspath(r) != os.path.abspath(perfil):
                        with open(r, encoding='utf-8') as f:
                            if MARCADOR.search(f.read()):
                                restantes.append(r)
        return restantes


class SinPerfil(Base):
    con_ejemplo = False

    def test_despliegue_bloqueado_sin_respuestas(self):
        codigo, salida = self.desplegar()
        self.assertEqual(codigo, 1)
        self.assertIn('BLOQUEADO', salida)
        self.assertIn('P-01', salida)
        self.assertFalse(os.path.exists(self.ruta('MPR_001')))

    def test_triaje_indica_f0(self):
        codigo, salida = self.ejecutar('hooks/triaje_sesion.py')
        contexto = json.loads(salida)['hookSpecificOutput']['additionalContext']
        self.assertIn('F0', contexto)
        self.assertNotIn('AUTOCOMPROBACI', contexto)


class Despliegue(Base):

    def test_comprobar_no_escribe(self):
        codigo, salida = self.desplegar('--comprobar')
        self.assertEqual(codigo, 0, salida)
        self.assertFalse(os.path.exists(self.ruta('MPR_001')))
        self.assertTrue(self.marcadores_restantes())

    def test_despliegue_completo_e_idempotente(self):
        codigo, salida = self.desplegar()
        self.assertEqual(codigo, 0, salida)
        for n in range(1, 6):
            carpeta = 'MPR_%03d' % n
            for sub in ('Procedimientos', 'Manuales'):
                self.assertTrue(os.path.isdir(self.ruta(carpeta, sub)))
            mapa = self.leer(carpeta, carpeta + '_mapa_relaciones.md')
            self.assertIn('# MPR-%03d – Mapa de relaciones' % n, mapa)
            self.assertIn('Sin relaciones registradas.', mapa)
            self.assertNotIn('[[', mapa)
        self.assertFalse(os.path.exists(self.ruta('MPR_006')))
        self.assertEqual(self.marcadores_restantes(), [])
        self.assertIn('Panadería La Espiga', self.leer('.claude', 'CLAUDE.md'))
        self.assertIn('*(Pendiente de desarrollo)*', self.leer('00_Recursos_metodologia', 'Nomenclatura', 'Sistema_de_nomenclatura.md'))
        global_ = self.leer('00_Mapa_global_relaciones.md')
        self.assertIn('| Origen ↓ / Destino → | MPR-001 | MPR-002 | MPR-003 | MPR-004 | MPR-005 |', global_)
        self.assertTrue(os.path.exists(self.ruta('00_Mapa_contenidos_pendientes.md')))
        self.assertTrue(os.path.isdir(self.ruta('En_proceso', 'Procesado')))
        self.assertIn('`MPR-001` a `MPR-005`', self.leer('00_Recursos_metodologia', 'Nomenclatura', 'Registro_de_codigos.md'))
        codigo, salida = self.desplegar()
        self.assertIn('nada que hacer', salida)
        codigo, salida = self.ejecutar('hooks/triaje_sesion.py')
        contexto = json.loads(salida)['hookSpecificOutput']['additionalContext']
        self.assertNotIn('F0', contexto)
        self.assertNotIn('F7', contexto, contexto)
        self.assertNotIn('AUTOCOMPROBACI', contexto)

    def test_nuevo_macroproceso_conserva_marcas(self):
        self.desplegar()
        ruta_global = self.ruta('00_Mapa_global_relaciones.md')
        texto = self.leer('00_Mapa_global_relaciones.md').replace('| **MPR-002** | |', '| **MPR-002** | X |', 1)
        with open(ruta_global, 'w', encoding='utf-8') as f:
            f.write(texto)
        mapa = self.ruta('00_Recursos_metodologia', 'Metodologia', '00_Mapa_procesos.md')
        with open(mapa, encoding='utf-8') as f:
            contenido = f.read()
        contenido = contenido.replace('| MPR-005 | Seguridad alimentaria | Soporte |',
                                      '| MPR-005 | Seguridad alimentaria | Soporte |\n| MPR-006 | Mantenimiento | Soporte |')
        with open(mapa, 'w', encoding='utf-8') as f:
            f.write(contenido)
        codigo, salida = self.desplegar()
        self.assertEqual(codigo, 0, salida)
        self.assertTrue(os.path.isdir(self.ruta('MPR_006', 'Procedimientos')))
        global_ = self.leer('00_Mapa_global_relaciones.md')
        self.assertIn('MPR-006 |', global_)
        self.assertIn('| **MPR-002** | X |', global_)

    def test_mapa_con_hueco_bloquea(self):
        mapa = self.ruta('00_Recursos_metodologia', 'Metodologia', '00_Mapa_procesos.md')
        with open(mapa, encoding='utf-8') as f:
            contenido = f.read().replace('| MPR-003 |', '| MPR-009 |')
        with open(mapa, 'w', encoding='utf-8') as f:
            f.write(contenido)
        codigo, salida = self.desplegar()
        self.assertEqual(codigo, 1)
        self.assertIn('MPR-009', salida)


class RegistroDeCodigos(Base):

    def setUp(self):
        super().setUp()
        self.desplegar()

    def test_bandeja_admite_cualquier_nombre(self):
        ruta = self.ruta('En_proceso', 'Notas_MPR_001_reunion.md')
        pre, post = self.escribir_con_hooks(ruta, '# notas\n')
        self.assertNotIn('hookSpecificOutput', pre)
        self.assertTrue(os.path.exists(ruta))
        self.assertNotIn('AVISO', json.dumps(post))

    def test_procedimiento_valido_se_inscribe(self):
        ruta = self.ruta('MPR_002', 'Procedimientos', 'PRC_001_amasado_horneado.md')
        pre, post = self.escribir_con_hooks(ruta, '# PRC-001 – Procedimiento de amasado y horneado\n')
        self.assertIsNotNone(post)
        registro = self.leer('00_Recursos_metodologia', 'Nomenclatura', 'Registro_de_codigos.md')
        self.assertIn('| PRC-001 | Procedimiento de amasado y horneado | MPR-002 | En curso |', registro)
        self.assertIn('| `PRC` | `PRC-001` en adelante | PRC-001 | PRC-002 |', registro)
        self.assertEqual(os.listdir(self.ruta('.claude', 'hooks', '.state')), [])

    def test_codigo_con_hueco_se_deniega(self):
        pre, post = self.escribir_con_hooks(self.ruta('MPR_002', 'Procedimientos', 'PRC_003_x.md'), '# x\n')
        self.assertEqual(pre['hookSpecificOutput']['permissionDecision'], 'deny')
        self.assertIn('PRC-001', pre['hookSpecificOutput']['permissionDecisionReason'])

    def test_subcarpeta_equivocada_se_deniega(self):
        pre, _ = self.escribir_con_hooks(self.ruta('MPR_002', 'Manuales', 'PRC_001_x.md'), '# x\n')
        self.assertEqual(pre['hookSpecificOutput']['permissionDecision'], 'deny')

    def test_macroproceso_fuera_del_mapa_se_deniega(self):
        pre, _ = self.escribir_con_hooks(self.ruta('MPR_007', 'MPR_007.md'), '# MPR-007 – x\n')
        self.assertEqual(pre['hookSpecificOutput']['permissionDecision'], 'deny')

    def test_documento_de_macroproceso_se_inscribe(self):
        self.escribir_con_hooks(self.ruta('MPR_003', 'MPR_003.md'), '# MPR-003 – Macroproceso operativo de venta\n')
        registro = self.leer('00_Recursos_metodologia', 'Nomenclatura', 'Registro_de_codigos.md')
        self.assertIn('| MPR-003 | Macroproceso operativo de venta | En curso |', registro)
        self.assertIn('| MPR-003 | — |', registro)

    def test_normaliza_nombre_de_archivo_nuevo(self):
        ruta = self.ruta('00_Recursos_metodologia', 'Tablas', 'Tabla De Proveedores.md')
        _, post = self.escribir_con_hooks(ruta, '# x\n')
        self.assertTrue(os.path.exists(self.ruta('00_Recursos_metodologia', 'Tablas', 'Tabla_de_proveedores.md')))
        self.assertIn('renombrado', post['systemMessage'])

    def test_vistas_y_auditoria(self):
        os.makedirs(self.ruta('MPR_001', 'Manuales'), exist_ok=True)
        with open(self.ruta('MPR_001', 'Manuales', 'MAN_001_uso_tpv.md'), 'w', encoding='utf-8') as f:
            f.write('# MAN-001 – Manual de uso — Terminal de venta\n')
        codigo, salida = self.ejecutar('hooks/auditar_codigos.py')
        self.assertIn('MAN_001_uso_tpv.md', salida)
        self.ejecutar('hooks/actualizar_vistas.py')
        self.assertIn('MAN_001_uso_tpv.md — manual', self.leer('00_Recursos_metodologia', 'Arbol_del_proyecto.md'))
        self.assertIn('| MAN-001 |', self.leer('00_Recursos_metodologia', 'Tablas', 'Tabla_de_fichas.md'))


if __name__ == '__main__':
    unittest.main()
