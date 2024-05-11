
from model.evento import Evento
class Bar(Evento):
    def __init__(self,nombre , lugar , direccion , fecha , hora_apertura , hora_show , estado , aforo, etapa):
        super().__init__(nombre , lugar , direccion , fecha , hora_apertura , hora_show , estado , aforo , etapa)
        self._pago_artista = 0
        self._utilidad_bar = 0
        self._utilidad_artista = 0

    # Getter para pago_artista
    def get_pago_artista(self):
        return self._pago_artista

    # Setter para pago_artista
    def set_pago_artista(self, pago_artista):
        self.pago_artista = pago_artista

    # Getter para utilidad_bar
    def get_utilidad_bar(self):
        return self._utilidad_bar

    # Setter para utilidad_bar
    def set_utilidad_bar(self, utilidad_bar):
        self._utilidad_bar = utilidad_bar

    # Getter para utilidad_artista
    def get_utilidad_artista(self):
        return self._utilidad_artista

    # Setter para utilidad_artista
    def set_utilidad_artista(self, utilidad_artista):
        self._utilidad_artista = utilidad_artista

    def comprar_boletas(self, nombre_categoria, cantidad_boletas,nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago):
        ans = False
        if super().get_aforo() >= cantidad_boletas:
            self.add_utilidad(self._boleteria.get_precio_categoria(nombre_categoria), cantidad_boletas)
            self._boleteria.comprar_boleta(nombre_categoria, cantidad_boletas, nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago, self._nombre, self._lugar, self._direccion, self._fecha, self._hora_apertura, self._hora_show)

            ans = True
        return ans

    def add_utilidad(self, cantidad , cantidad_boletas):
        comision_bar = 0.20
        comision_artista = 0.80
        self._utilidad_bar += cantidad_boletas * float(cantidad) * comision_bar
        self._utilidad_artista += cantidad_boletas * float(cantidad) * comision_artista
        super().add_utilidad(cantidad_boletas * float(cantidad))
        super().modificar_aforo(cantidad_boletas)
