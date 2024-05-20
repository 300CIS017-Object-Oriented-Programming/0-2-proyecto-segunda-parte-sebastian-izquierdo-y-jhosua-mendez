
class Cliente():
    def __init__(self, id, nombre, apellido, telefono,como_se_entero,categoria ,pago, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.como_se_entero = como_se_entero
        self.categoria = categoria
        self.pago = pago
        self.edad = edad

    # Getter para id
    def get_edad(self):
        return self.edad
    def get_id(self):
        return self._id

    # Setter para id
    def set_id(self, id):
        self._id = id

    # Getter para nombre
    def get_nombre(self):
        return self._nombre

    # Setter para nombre
    def set_nombre(self, nombre):
        self._nombre = nombre

    # Getter para apellido
    def get_apellido(self):
        return self._apellido

    # Setter para apellido
    def set_apellido(self, apellido):
        self._apellido = apellido

    # Getter para telefono
    def get_telefono(self):
        return self._telefono

    # Setter para telefono
    def set_telefono(self, telefono):
        self._telefono = telefono

    # Getter para como_se_entero
    def get_como_se_entero(self):
        return self._como_se_entero

    # Setter para como_se_entero
    def set_como_se_entero(self, como_se_entero):
        self._como_se_entero = como_se_entero

    # Getter para categoria
    def get_categoria(self):
        return self._categoria

    # Setter para categoria
    def set_categoria(self, categoria):
        self._categoria = categoria

    # Getter para pago
    def get_pago(self):
        return self._pago

    # Setter para pago
    def set_pago(self, pago):
        self._pago = pago

    def reporte(self):
        print("Cliente reporte")
        print("Nombre: " + self.nombre)
        print("Apellido: " + self.apellido)
        print("Telefono: " + self.telefono)
        print("Categoria: " + self.categoria)
        print("Tipo de pago: " + self.pago)
