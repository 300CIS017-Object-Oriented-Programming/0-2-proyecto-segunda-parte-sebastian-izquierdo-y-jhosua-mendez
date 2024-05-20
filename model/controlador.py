from model.bar import Bar
from model.teatro import Teatro
from model.filantropico import Filantropico
from model.artista import Artista
from model.boleta import Boleta
class Controlador:
    def __init__(self):
        self.eventos = []
        self.artistas = {}

    def crear_bar(self,nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa,pago_artistas):
        evento = Bar(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa)
        evento.set_pago_artista(pago_artistas)
        self.eventos.append(evento)
        return True
    def agregar_artista(self, nombre):
        ans = False
        if len(self.eventos) != 0:
            evento = self.eventos[-1]
            evento.añadir_artista(nombre)
            if nombre in self.artistas:
                self.artistas[nombre].add_evento(evento)
            else:
                artista = Artista(nombre)
                artista.add_evento(evento)
                self.artistas[nombre] = artista
            ans = True
        return ans
    def agregar_categoria(self,nombre_categoria,precio):
        ans = False
        if len(self.eventos) != 0:
            evento = self.eventos[-1]
            evento.añadir_categoria(nombre_categoria,precio)
            ans = True
        return ans
    def crear_teatro(self,nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa,arriendo):
        evento = Teatro(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa,arriendo)
        evento.set_arriendo(arriendo)
        self.eventos.append(evento)
        return True
    def crear_filantropico(self,nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa):
        evento = Filantropico(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa)
        self.eventos.append(evento)
        return True
    def agregar_patrocinio(self,nombre_patrocinio , monto):
        ans = False
        if len(self.eventos) != 0:
            evento = self.eventos[-1]
            evento.agregar_patrocinio(nombre_patrocinio,monto)
            ans = True
        return ans

    def get_tamanio_eventos(self):
        return len(self.eventos)
    def lista_eventos(self):
        return self.eventos
    def moficar_estado_evento(self, nombre, estado):
        ans = False
        for evento in self.eventos:
            if evento.get_estado() != "realizado":
                if evento.get_nombre() == nombre:
                    evento.set_estado(estado)
                    ans = True
        return ans

    def modificar_etapa_evento(self, nombre, etapa):
        ans = False
        for evento in self.eventos:
            if evento.get_nombre() == nombre:
                evento.set_etapa(etapa)
                ans = True
        return ans

    def eliminar_evento(self, nombre):
        ans = False
        for evento in self.eventos:
            if evento.get_nombre() == nombre:
                if evento.get_boletas_vendidas() == 0:
                    self.eventos.remove(evento)
                    ans = True
        return ans

    def mostrar_boletas(self,evento_seleccionado):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                return evento.obtener_categorias()

    def precio_categoria(self, evento_seleccionado, categoria_seleccionada):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                return evento.obtener_precio_categoria(categoria_seleccionada)

    def comprar_boletas(self, evento_seleccionado, categoria_seleccionada, cantidad_boletas, nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago,edad):
        ans = False
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                ans = evento.comprar_boletas(categoria_seleccionada, cantidad_boletas, nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago)
        return ans
    def disponibilidad(self, evento_seleccionado , cantidad_boletas):
        ans = False
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                if evento.get_aforo() >= cantidad_boletas:
                    ans = True
        return ans

    def cantidad_disponible(self, evento_seleccionado):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                return evento.get_aforo()
    def validar_boletas(self, evento_seleccionado, codigo):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                return evento.validar_boleta(codigo)
    def reporte_de_ventas(self, evento_seleccionado):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                ans = evento.reporte_venta_boletas()
        return ans

    def lista_artistas(self):
        artista = []
        for nombre in self.artistas.keys():
            artista.append(nombre)
        return artista

    def get_evento(self, nombre_evento):
        for evento in self.eventos:
            if evento.get_nombre() == nombre_evento:
                return evento

    def get_tiqueteria(self, nombre_evento):
        for evento in self.eventos:
            if evento.get_nombre() == nombre_evento:
                return evento.get_boleteria()
    def mostrar_eventos(self, artista_seleccionado):
        return self.artistas[artista_seleccionado].mostrar_eventos()
