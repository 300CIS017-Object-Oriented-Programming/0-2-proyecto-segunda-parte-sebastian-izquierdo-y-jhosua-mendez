import unittest
from model.boleta import Boleta

class TestBoleta(unittest.TestCase):

    def setUp(self):
        self.boleta = Boleta(1, "Cliente", 123, "Evento", "Lugar", "Direccion", "2022-12-31", "10:00", "12:00", 2, 200)

    def test_initialization(self):
        self.assertEqual(self.boleta.id_boleta, 1)
        self.assertEqual(self.boleta.nombre_cliente, "Cliente")
        self.assertEqual(self.boleta.id_cliente, 123)
        self.assertEqual(self.boleta.nombre_evento, "Evento")
        self.assertEqual(self.boleta.lugar_evento, "Lugar")
        self.assertEqual(self.boleta.direccion_evento, "Direccion")
        self.assertEqual(self.boleta.fecha_evento, "2022-12-31")
        self.assertEqual(self.boleta.hora_apertura, "10:00")
        self.assertEqual(self.boleta.hora_show, "12:00")
        self.assertEqual(self.boleta.cantidad, 2)
        self.assertEqual(self.boleta.pago_total, 200)
        self.assertEqual(self.boleta.registro_entrada, False)

    def test_get_cantidad(self):
        self.assertEqual(self.boleta.get_cantidad(), 2)

    def test_registrar_entrada(self):
        self.boleta.registrar_entrada()
        self.assertEqual(self.boleta.registro_entrada, True)

    # Para el método crear_pdf, es un poco más complicado probarlo directamente ya que crea un archivo PDF y abre un navegador web.
    # Podrías probar que el archivo se crea correctamente verificando que existe después de llamar al método.
    # Sin embargo, esto requeriría que tu entorno de pruebas tenga acceso al sistema de archivos y pueda abrir un navegador web, lo cual no siempre es posible.
    # Por lo tanto, es posible que desees considerar refactorizar tu código para hacerlo más fácil de probar, por ejemplo, separando la creación del PDF y la apertura del navegador web en diferentes métodos.

if __name__ == '__main__':
    unittest.main()