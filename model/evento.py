from model.tiqueteria import Tiqueteria
from abc import ABC, abstractmethod
class Evento():

   def __init__(self,nombre , lugar , direccion , fecha , hora_apertura , hora_show , estado , aforo, etapa):
       self._nombre = nombre
       self._lugar = lugar
       self._direccion = direccion
       self._fecha = fecha
       self._hora_show = hora_show
       self._hora_apertura = hora_apertura
       self._estado = estado
       self._artistas = []
       self._aforo = aforo
       self._boletas_vendidas = 0
       self._ganancia = 0
       self._gastos = 0
       self._utilidad = 0
       self._boleteria = Tiqueteria(etapa)
       self._boleteria.agregar_categoria("Cortesia", 0)

       # Métodos para obtener los valores de los atributos

   def get_nombre(self):
       return self._nombre

   def get_lugar(self):
       return self._lugar

   def get_direccion(self):
       return self._direccion

   def get_fecha(self):
       return self._fecha

   def get_hora_apertura(self):
       return self._hora_apertura

   def get_hora_show(self):
       return self._hora_show

   def get_estado(self):
       return self._estado

   def get_aforo(self):
       return self._aforo

   def get_boletas_vendidas(self):
       return self._boletas_vendidas

   def get_ganancia(self):
       return self._ganancia

   def get_gastos(self):
       return self._gastos

   def get_utilidad(self):
       return self._utilidad

   def get_boleteria(self):
       return self._boleteria

       # Métodos para establecer los valores de los atributos

   def set_nombre(self, nombre):
       self._nombre = nombre

   def set_lugar(self, lugar):
       self._lugar = lugar

   def set_direccion(self, direccion):
       self._direccion = direccion

   def set_fecha(self, fecha):
       self._fecha = fecha

   def set_hora_apertura(self, hora_apertura):
       self._hora_apertura = hora_apertura

   def set_hora_show(self, hora_show):
       self._hora_show = hora_show

   def set_estado(self, estado):
       self._estado = estado

   def set_aforo(self, aforo):
       self._aforo = aforo
   def set_etapa(self, etapa):
         self._boleteria.set_etapa(etapa)
   def modificar_aforo(self, cantidad):
       self._aforo -= cantidad
   def set_boletas_vendidas(self, boletas_vendidas):
       self._boletas_vendidas = boletas_vendidas

   def set_ganancia(self, ganancia):
       self._ganancia = ganancia

   def set_gastos(self, gastos):
       self._gastos = gastos

   def set_utilidad(self, utilidad):
       self._utilidad += utilidad
   def add_utilidad(self, valor):
       self._utilidad += valor

   def añadir_artista(self, artista):
       self._artistas.append(artista)
   def añadir_categoria(self, categoria , precio):
        self._boleteria.agregar_categoria(categoria , precio)
   def mostrar_Artistas(self):
       if len(self._artistas) != 0 :
            print("Artistas del evento")
            for artista in self._artistas:
                print(artista)
       else:
           print("No hay Artistas")
   def mostrar_boletas(self):
       self._boleteria.get_categorias()

   def obtener_categorias(self):
       return self._boleteria.get_categorias()
   def obtener_precio_categoria(self, nombre_categoria):
       return self._boleteria.get_precio_categoria(nombre_categoria)

   def validar_boleta(self, codigo):
       return self._boleteria.validar_boleta(codigo)

   def add_boletas_vendidas(self, cantidad):
       self._boletas_vendidas += cantidad

   @abstractmethod
   def comprar_boletas(self):
       pass
   def reporte_clientes(self):
       self._boleteria.mostrar_clientes()
   def reporte_financiero(self):
        self._boleteria.reporte_financiero()
   def reporte_venta_boletas(self):
        return self._boleteria.reporte_ventas_boletas(self._nombre, self._boletas_vendidas)