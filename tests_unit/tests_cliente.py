import unittest
from model.cliente import Cliente

class TestCliente(unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(1, "Nombre", "Apellido", "1234567890", "Internet", "Categoria", "Tarjeta", 30)

    def test_initialization(self):
        self.assertEqual(self.cliente.id, 1)
        self.assertEqual(self.cliente.nombre, "Nombre")
        self.assertEqual(self.cliente.apellido, "Apellido")
        self.assertEqual(self.cliente.telefono, "1234567890")
        self.assertEqual(self.cliente.como_se_entero, "Internet")
        self.assertEqual(self.cliente.categoria, "Categoria")
        self.assertEqual(self.cliente.pago, "Tarjeta")
        self.assertEqual(self.cliente.edad, 30)

    def test_getters(self):
        self.assertEqual(self.cliente.get_id(), 1)
        self.assertEqual(self.cliente.get_nombre(), "Nombre")
        self.assertEqual(self.cliente.get_apellido(), "Apellido")
        self.assertEqual(self.cliente.get_telefono(), "1234567890")
        self.assertEqual(self.cliente.get_como_se_entero(), "Internet")
        self.assertEqual(self.cliente.get_categoria(), "Categoria")
        self.assertEqual(self.cliente.get_pago(), "Tarjeta")
        self.assertEqual(self.cliente.get_edad(), 30)

    def test_setters(self):
        self.cliente.set_id(2)
        self.cliente.set_nombre("Nuevo Nombre")
        self.cliente.set_apellido("Nuevo Apellido")
        self.cliente.set_telefono("0987654321")
        self.cliente.set_como_se_entero("Amigo")
        self.cliente.set_categoria("Nueva Categoria")
        self.cliente.set_pago("Efectivo")
        self.cliente.set_edad(35)

        self.assertEqual(self.cliente.get_id(), 2)
        self.assertEqual(self.cliente.get_nombre(), "Nuevo Nombre")
        self.assertEqual(self.cliente.get_apellido(), "Nuevo Apellido")
        self.assertEqual(self.cliente.get_telefono(), "0987654321")
        self.assertEqual(self.cliente.get_como_se_entero(), "Amigo")
        self.assertEqual(self.cliente.get_categoria(), "Nueva Categoria")
        self.assertEqual(self.cliente.get_pago(), "Efectivo")
        self.assertEqual(self.cliente.get_edad(), 35)

if __name__ == '__main__':
    unittest.main()