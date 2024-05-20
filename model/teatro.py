from model.evento import Evento

class Teatro(Evento):
    def __init__(self, nombre, lugar, direccion, fecha, hora_apertura , hora_show , estado , aforo, etapa, arriendo):
        super().__init__(nombre, lugar, direccion, fecha, hora_apertura , hora_show , estado , aforo, etapa)
        self._arriendo = arriendo
        self._utilidad_tiquetera = 0
        super().add_utilidad(-arriendo)

        # Getter para arriendo
    def get_arriendo(self):
        return self._arriendo

    # Setter para arriendo
    def set_arriendo(self, arriendo):
        self._arriendo = arriendo
        # Actualizar la utilidad después de cambiar el arriendo
        super().set_utilidad(-arriendo)

    # Getter para utilidad_tiquetera
    def get_utilidad_tiquetera(self):
        return self._utilidad_tiquetera
        # Setter para utilidad_tiquetera
    def set_utilidad_tiquetera(self, utilidad_tiquetera):
        self._utilidad_tiquetera = utilidad_tiquetera

    def add_utilidad (self,valor,cantidad_boletas):
        comision_tiquetera = 0.07
        super().add_utilidad(valor*cantidad_boletas) 
        self._utilidad_tiquetera += valor*comision_tiquetera*cantidad_boletas
        super().modificar_aforo(cantidad_boletas) 
    def comprar_boletas(self, nombre_categoria, cantidad_boletas, nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago ,edad):
        if super().get_aforo() >= cantidad_boletas:
            self.add_utilidad(self._boleteria.get_precio_categoria(nombre_categoria), cantidad_boletas)
            self._boleteria.comprar_boleta(nombre_categoria, cantidad_boletas, nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago, self._nombre, self._lugar, self._direccion, self._fecha, self._hora_apertura, self._hora_show,edad)
    