import unittest
from model.artista import Artista
from model.evento import Evento  # Asegúrate de importar la clase Evento

class TestArtista(unittest.TestCase):

    def setUp(self):
        self.artista = Artista("Artista de Prueba")
        self.evento = Evento("Evento de Prueba", "2022-12-31", "Lugar de Prueba", 100, 50)  # Asegúrate de ajustar los argumentos según tu clase Evento

    def test_initialization(self):
        self.assertEqual(self.artista.nombre_artista, "Artista de Prueba")
        self.assertEqual(self.artista.eventos, [])

    def test_get_nombre(self):
        self.assertEqual(self.artista.get_nombre(), "Artista de Prueba")

    def test_add_evento(self):
        self.artista.add_evento(self.evento)
        self.assertEqual(len(self.artista.eventos), 1)
        self.assertEqual(self.artista.eventos[0], self.evento)

    def test_mostrar_eventos(self):
        self.artista.add_evento(self.evento)
        result = self.artista.mostrar_eventos()
        self.assertIn("Evento: Evento de Prueba", result)
        self.assertIn("Fecha: 2022-12-31", result)
        self.assertIn("Lugar: Lugar de Prueba", result)
        self.assertIn("Cantidad boletas vendidas: 50", result)
        self.assertIn("aforo: 33.33333333333333%", result)  # Este valor puede variar dependiendo de cómo calculas el aforo

if __name__ == '__main__':
    unittest.main()