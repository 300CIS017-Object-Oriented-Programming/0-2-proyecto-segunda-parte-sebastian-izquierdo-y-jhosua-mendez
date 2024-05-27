import unittest
from model.controlador import Controlador

class TestControlador(unittest.TestCase):

    def setUp(self):
        self.controlador = Controlador()

    def test_crear_bar(self):
        self.assertTrue(self.controlador.crear_bar("Bar1", "Lugar1", "Direccion1", "2022-12-31", "10:00", "12:00", "Activo", 100, "Preventa", 5000, 10))
        self.assertEqual(len(self.controlador.eventos), 1)

    def test_agregar_artista(self):
        self.controlador.crear_bar("Bar1", "Lugar1", "Direccion1", "2022-12-31", "10:00", "12:00", "Activo", 100, "Preventa", 5000, 10)
        self.assertTrue(self.controlador.agregar_artista("Artista1"))
        self.assertEqual(len(self.controlador.artistas), 1)

    def test_agregar_categoria(self):
        self.controlador.crear_bar("Bar1", "Lugar1", "Direccion1", "2022-12-31", "10:00", "12:00", "Activo", 100, "Preventa", 5000, 10)
        self.assertTrue(self.controlador.agregar_categoria("Categoria1", 100))

    # Continúa con el resto de los métodos de la clase Controlador

if __name__ == '__main__':
    unittest.main()