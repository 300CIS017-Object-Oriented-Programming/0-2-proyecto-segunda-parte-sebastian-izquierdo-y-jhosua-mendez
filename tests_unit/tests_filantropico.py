import unittest
from model.filantropico import Filantropico

class TestFilantropico(unittest.TestCase):

    def setUp(self):
        self.filantropico = Filantropico("Nombre", "Lugar", "Direccion", "2022-12-31", "10:00", "12:00", "Activo", 100, "Preventa")

    def test_initialization(self):
        self.assertEqual(self.filantropico.get_nombre(), "Nombre")
        self.assertEqual(self.filantropico.get_lugar(), "Lugar")
        self.assertEqual(self.filantropico.get_direccion(), "Direccion")
        self.assertEqual(self.filantropico.get_fecha(), "2022-12-31")
        self.assertEqual(self.filantropico.get_hora_apertura(), "10:00")
        self.assertEqual(self.filantropico.get_hora_show(), "12:00")
        self.assertEqual(self.filantropico.get_estado(), "Activo")
        self.assertEqual(self.filantropico.get_aforo(), 100)
        self.assertEqual(self.filantropico.get_boletas_vendidas(), 0)
        self.assertEqual(self.filantropico._patrocinios, {})

    def test_agregar_patrocinio(self):
        self.filantropico.agregar_patrocinio("Patrocinador", 5000)
        self.assertEqual(self.filantropico.get_patrocinio("Patrocinador"), 5000)

    def test_comprar_boletas(self):
        # Aquí necesitarás implementar una prueba para el método comprar_boletas.
        # La implementación exacta dependerá de cómo hayas implementado este método en tu clase Filantropico.
        pass

    def test_obtener_patrocinios(self):
        self.filantropico.agregar_patrocinio("Patrocinador1", 5000)
        self.filantropico.agregar_patrocinio("Patrocinador2", 3000)
        self.assertIn("Patrocinador1", self.filantropico.obtener_patrocinios())
        self.assertIn("Patrocinador2", self.filantropico.obtener_patrocinios())

if __name__ == '__main__':
    unittest.main()