import unittest
from model.evento import Evento
from model.tiqueteria import Tiqueteria

class TestEvento(unittest.TestCase):

    def setUp(self):
        self.evento = Evento("Nombre", "Lugar", "Direccion", "2022-12-31", "10:00", "12:00", "Activo", 100, "Preventa", 10)

    def test_initialization(self):
        self.assertEqual(self.evento.get_nombre(), "Nombre")
        self.assertEqual(self.evento.get_lugar(), "Lugar")
        self.assertEqual(self.evento.get_direccion(), "Direccion")
        self.assertEqual(self.evento.get_fecha(), "2022-12-31")
        self.assertEqual(self.evento.get_hora_apertura(), "10:00")
        self.assertEqual(self.evento.get_hora_show(), "12:00")
        self.assertEqual(self.evento.get_estado(), "Activo")
        self.assertEqual(self.evento.get_aforo(), 100)
        self.assertEqual(self.evento.get_boletas_vendidas(), 0)
        self.assertEqual(self.evento.get_ganancia(), 0)
        self.assertEqual(self.evento.get_gastos(), 0)
        self.assertEqual(self.evento.get_utilidad(), 0)
        self.assertIsInstance(self.evento.get_boleteria(), Tiqueteria)
        self.assertEqual(self.evento.get_descuento_preventa(), 10)

    def test_setters(self):
        self.evento.set_nombre("Nuevo Nombre")
        self.evento.set_lugar("Nuevo Lugar")
        self.evento.set_direccion("Nueva Direccion")
        self.evento.set_fecha("2023-01-01")
        self.evento.set_hora_apertura("11:00")
        self.evento.set_hora_show("13:00")
        self.evento.set_estado("Inactivo")
        self.evento.set_aforo(200)
        self.evento.set_boletas_vendidas(50)
        self.evento.set_ganancia(5000)
        self.evento.set_gastos(2000)
        self.evento.set_utilidad(3000)
        self.evento.set_etapa("Venta")

        self.assertEqual(self.evento.get_nombre(), "Nuevo Nombre")
        self.assertEqual(self.evento.get_lugar(), "Nuevo Lugar")
        self.assertEqual(self.evento.get_direccion(), "Nueva Direccion")
        self.assertEqual(self.evento.get_fecha(), "2023-01-01")
        self.assertEqual(self.evento.get_hora_apertura(), "11:00")
        self.assertEqual(self.evento.get_hora_show(), "13:00")
        self.assertEqual(self.evento.get_estado(), "Inactivo")
        self.assertEqual(self.evento.get_aforo(), 200)
        self.assertEqual(self.evento.get_boletas_vendidas(), 50)
        self.assertEqual(self.evento.get_ganancia(), 5000)
        self.assertEqual(self.evento.get_gastos(), 2000)
        self.assertEqual(self.evento.get_utilidad(), 3000)
        self.assertEqual(self.evento.get_boleteria().get_etapa(), "Venta")

    def test_set_gastos(self):
        self.evento.set_gastos(5000)
        self.assertEqual(self.evento.get_gastos(), 5000)

    def test_set_and_add_utilidad(self):
        self.evento.set_utilidad(1000)
        self.assertEqual(self.evento.get_utilidad(), 1000)
        self.evento.add_utilidad(500)
        self.assertEqual(self.evento.get_utilidad(), 1500)

    def test_artista_management(self):
        self.evento.añadir_artista("Artista de Prueba")
        self.assertIn("Artista de Prueba", self.evento._artistas)

    def test_categoria_management(self):
        self.evento.añadir_categoria("Categoria de Prueba", 100)
        self.assertIn("Categoria de Prueba", self.evento.obtener_categorias())

    def test_boleta_management(self):
        self.evento.add_boletas_vendidas(50)
        self.assertEqual(self.evento.get_boletas_vendidas(), 50)

if __name__ == '__main__':
    unittest.main()