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