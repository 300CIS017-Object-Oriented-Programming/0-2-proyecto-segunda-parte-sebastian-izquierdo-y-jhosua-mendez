class Controller_view():
    def __init__(self):
        self.menu = True
        self.agregando_items = False
        self.creando_evento = False
        self.comprando = False
        self.reset = False
        self.modificando = False
        self.formulario_cliente = False
        self.validando = False
        self.reportes = False
        self.reporte_ventas = False
        self.reporte_clientes = False
        self.reporte_financiero = False
        self.consulta_artista = False
        self.crear_evento_pagina = False
        self.tiqueteria_pagina = False

    def activate_reporte_ventas(self):
        self.reporte_ventas = True
    def activate_reporte_clientes(self):
        self.reporte_clientes = True
    def activate_reporte_financiero(self):
        self.reporte_financiero = True
    def activate_consulta_artista(self):
        self.consulta_artista = True
    def activate_reportes(self):
        self.reportes = True
    def activate_validando(self):
        self.validando = True
    def activate_formulario_cliente(self):
        self.formulario_cliente = True
    def activate_menu(self):
        self.menu = True
    def activate_agregando_items(self):
        self.agregando_items = True
    def activate_creando_evento(self):
        self.creando_evento = True
    def activate_comprando(self):
        self.comprando = True
    def activate_reset(self):
        self.reset = True
    def activate_modificando(self):
        self.modificando = True
    def activate_crear_evento_pagina(self):
        self.crear_evento_pagina = True
    def activate_tiqueteria_pagina(self):
        self.tiqueteria_pagina = True

    def desactivate_reporte_ventas(self):
        self.reporte_ventas = False
    def desactivate_reporte_clientes(self):
        self.reporte_clientes = False
    def desactivate_reporte_financiero(self):
        self.reporte_financiero = False
    def desactivate_consulta_artista(self):
        self.consulta_artista = False
    def desactivate_reportes(self):
        self.reportes = False
    def desactivate_validando(self):
        self.validando = False
    def desactivate_formulario_cliente(self):
        self.formulario_cliente = False
    def desactivate_menu(self):
        self.menu = False
    def desactivate_agregando_items(self):
        self.agregando_items = False
    def desactivate_creando_evento(self):
        self.creando_evento = False
    def desactivate_comprando(self):
        self.comprando = False
    def desactivate_reset(self):
        self.reset = False
    def desactivate_modificando(self):
        self.modificando = False
    def desactivate_crear_evento_pagina(self):
        self.crear_evento_pagina = False
    def desactivate_tiqueteria_pagina(self):
        self.tiqueteria_pagina = False

    def get_reportes(self):
        return self.reportes
    def get_formulario_cliente(self):
        return self.formulario_cliente
    def get_menu(self):
        return self.menu
    def get_agregando_items(self):
        return self.agregando_items
    def get_creando_evento(self):
        return self.creando_evento
    def get_comprando(self):
        return self.comprando
    def get_reset(self):
        return self.reset
    def get_modificando(self):
        return self.modificando
    def get_validando(self):
        return self.validando
    def get_reporte_ventas(self):
        return self.reporte_ventas
    def get_reporte_clientes(self):
        return self.reporte_clientes
    def get_reporte_financiero(self):
        return self.reporte_financiero
    def get_consulta_artista(self):
        return self.consulta_artista
    def get_crear_evento_pagina(self):
        return self.crear_evento_pagina
    def get_tiqueteria_pagina(self):
        return self.tiqueteria_pagina