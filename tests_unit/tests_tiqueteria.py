import unittest
from model.tiqueteria import Tiqueteria
from model.cliente import Cliente
from model.boleta import Boleta

class TestTiqueteria(unittest.TestCase):
    def setUp(self):
        self.tiqueteria = Tiqueteria("Preventa")

    def test_set_get_etapa(self):
        self.tiqueteria.set_etapa("Regular")
        self.assertEqual(self.tiqueteria.get_etapa(), "Regular")

    def test_agregar_categoria(self):
        self.tiqueteria.agregar_categoria("VIP", 100)
        self.assertEqual(self.tiqueteria.get_precio_categoria("VIP"), 100)

    def test_agregar_venta_preventa(self):
        self.tiqueteria.agregar_venta_preventa(100)
        self.assertEqual(self.tiqueteria.get_ingresos_totales(), 100)

    def test_agregar_venta_regular(self):
        self.tiqueteria.agregar_venta_regular(200)
        self.assertEqual(self.tiqueteria.get_ingresos_totales(), 200)

    def test_agregar_cliente(self):
        cliente = Cliente("123", "John", "Doe", "1234567890", "Internet", "VIP", "Efectivo", 30)
        self.tiqueteria.agregar_cliente(cliente)
        # Add more assertions based on your implementation

    # Continue with other methods...

if __name__ == '__main__':
    unittest.main()