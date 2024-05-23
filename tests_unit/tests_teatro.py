import unittest
from model.teatro import Teatro

class TestTeatro(unittest.TestCase):

    def setUp(self):
        self.teatro = Teatro("Nombre", "Lugar", "Direccion", "2022-12-31", "10:00", "12:00", "Activo", 100, "Preventa", 5000, 10)

    def test_initialization(self):
        self.assertEqual(self.teatro.get_nombre(), "Nombre")
        self.assertEqual(self.teatro.get_lugar(), "Lugar")
        self.assertEqual(self.teatro.get_direccion(), "Direccion")
        self.assertEqual(self.teatro.get_fecha(), "2022-12-31")
        self.assertEqual(self.teatro.get_hora_apertura(), "10:00")
        self.assertEqual(self.teatro.get_hora_show(), "12:00")
        self.assertEqual(self.teatro.get_estado(), "Activo")
        self.assertEqual(self.teatro.get_aforo(), 100)
        self.assertEqual(self.teatro.get_boletas_vendidas(), 0)
        self.assertEqual(self.teatro.get_arriendo(), 5000)
        self.assertEqual(self.teatro.get_utilidad_tiquetera(), 0)

    def test_setters(self):
        self.teatro.set_arriendo(6000)
        self.assertEqual(self.teatro.get_arriendo(), 6000)

        self.teatro.set_utilidad_tiquetera(2000)
        self.assertEqual(self.teatro.get_utilidad_tiquetera(), 2000)

    def test_add_utilidad(self):
        self.teatro.add_utilidad(100, 2)
        self.assertEqual(self.teatro.get_utilidad_tiquetera(), 14.0)

    def test_comprar_boletas(self):
        # Aquí necesitarás implementar una prueba para el método comprar_boletas.
        # La implementación exacta dependerá de cómo hayas implementado este método en tu clase Teatro.
        pass

if __name__ == '__main__':
    unittest.main()