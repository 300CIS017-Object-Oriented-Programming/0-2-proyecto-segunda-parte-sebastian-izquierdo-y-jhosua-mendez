class Controller_view():
    def __init__(self):
        self.controlador = False
        self.agregando_items = False
        self.creando_evento = False
        self.comprando = False
        self.reset = False
        self.modificando = False

    def activate_controlador(self):
        self.controlador = True
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

    def deactivate_controlador(self):
        self.controlador = False
    def deactivate_agregando_items(self):
        self.agregando_items = False
    def deactivate_creando_evento(self):
        self.creando_evento = False
    def deactivate_comprando(self):
        self.comprando = False
    def deactivate_reset(self):
        self.reset = False
    def deactivate_modificando(self):
        self.modificando = False


    def get_controlador(self):
        return self.controlador
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