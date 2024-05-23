import unittest
from model.controller_view import Controller_view

class TestControllerView(unittest.TestCase):

    def setUp(self):
        self.controller_view = Controller_view()

    def test_initialization(self):
        self.assertTrue(self.controller_view.get_menu())
        self.assertFalse(self.controller_view.get_agregando_items())
        self.assertFalse(self.controller_view.get_creando_evento())
        self.assertFalse(self.controller_view.get_comprando())
        self.assertFalse(self.controller_view.get_reset())
        self.assertFalse(self.controller_view.get_modificando())
        self.assertFalse(self.controller_view.get_formulario_cliente())
        self.assertFalse(self.controller_view.get_validando())
        self.assertFalse(self.controller_view.get_reportes())
        self.assertFalse(self.controller_view.get_reporte_ventas())
        self.assertFalse(self.controller_view.get_reporte_clientes())
        self.assertFalse(self.controller_view.get_reporte_financiero())
        self.assertFalse(self.controller_view.get_consulta_artista())
        self.assertFalse(self.controller_view.get_crear_evento_pagina())
        self.assertFalse(self.controller_view.get_tiqueteria_pagina())

    def test_activate_desactivate_methods(self):
        self.controller_view.activate_agregando_items()
        self.assertTrue(self.controller_view.get_agregando_items())
        self.controller_view.desactivate_agregando_items()
        self.assertFalse(self.controller_view.get_agregando_items())

        # Continúa con el resto de los métodos de activación y desactivación

if __name__ == '__main__':
    unittest.main()