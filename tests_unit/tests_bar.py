import unittest
from model.bar import Bar

class TestBar(unittest.TestCase):

    def setUp(self):
        self.bar = Bar("Nombre", "Lugar", "Direccion", "2022-12-31", "10:00", "12:00", "Activo", 100, "Preventa", 10)

    def test_initialization(self):
        self.assertEqual(self.bar.get_nombre(), "Nombre")
        self.assertEqual(self.bar.get_lugar(), "Lugar")
        self.assertEqual(self.bar.get_direccion(), "Direccion")
        self.assertEqual(self.bar.get_fecha(), "2022-12-31")
        self.assertEqual(self.bar.get_hora_apertura(), "10:00")
        self.assertEqual(self.bar.get_hora_show(), "12:00")
        self.assertEqual(self.bar.get_estado(), "Activo")
        self.assertEqual(self.bar.get_aforo(), 100)
        self.assertEqual(self.bar.get_boletas_vendidas(), 0)
        self.assertEqual(self.bar.get_pago_artista(), 0)
        self.assertEqual(self.bar.get_utilidad_bar(), 0)
        self.assertEqual(self.bar.get_utilidad_artista(), 0)

    def test_setters(self):
        self.bar.set_pago_artista(5000)
        self.assertEqual(self.bar.get_pago_artista(), 5000)

        self.bar.set_utilidad_bar(2000)
        self.assertEqual(self.bar.get_utilidad_bar(), 2000)

        self.bar.set_utilidad_artista(3000)
        self.assertEqual(self.bar.get_utilidad_artista(), 3000)

    def test_comprar_boletas(self):
        # Aquí necesitarás implementar una prueba para el método comprar_boletas.
        # La implementación exacta dependerá de cómo hayas implementado este método en tu clase Bar.
        pass

    def test_add_utilidad(self):
        self.bar.add_utilidad(100, 2)
        self.assertEqual(self.bar.get_utilidad_bar(), 40.0)
        self.assertEqual(self.bar.get_utilidad_artista(), 160.0)

if __name__ == '__main__':
    unittest.main()