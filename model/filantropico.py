from model.evento import Evento

class Filantropico(Evento):
    def __init__(self,nombre , lugar , direccion , fecha , hora_apertura , hora_show , estado , aforo, etapa):
        super().__init__(nombre , lugar , direccion , fecha , hora_apertura , hora_show , estado , aforo, etapa)
        self._patrocinios = {}

    def agregar_patrocinio(self,nombre,valor):
        self._patrocinios[nombre] = valor
        super().add_utilidad(valor)

    def mostar_patrocinios(self):
        for elemento in self._patrocinios:
            print(f"Patrocinio de {elemento} por el valor:  {self._patrocinios[elemento]}")
    def comprar_boletas(self , nombre_categoria , cantidad , nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago):
        if super().get_aforo() >= cantidad:
            self._boleteria.comprar_boleta(nombre_categoria, cantidad, nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago, self._nombre, self._lugar, self._direccion, self._fecha, self._hora_apertura, self._hora_show)
            super().modificar_aforo(cantidad)
    def obtener_patrocinios(self):
        ans = []
        for patrocinio in self._patrocinios.keys():
            ans.append(patrocinio)
        return ans
    def get_patrocinio(self, nombre_patrocinio):
        return self._patrocinios[nombre_patrocinio]