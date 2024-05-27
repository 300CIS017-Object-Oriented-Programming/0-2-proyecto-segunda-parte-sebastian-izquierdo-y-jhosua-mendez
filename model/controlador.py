from model.bar import Bar
from model.teatro import Teatro
from model.filantropico import Filantropico
from model.artista import Artista
from model.boleta import Boleta
from datetime import datetime
import webbrowser
import pandas as pd
import os
class Controlador:
    def __init__(self):
        self.eventos = []
        self.artistas = {}

    def crear_bar(self,nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa,pago_artistas, descuento_preventa):
        evento = Bar(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa, descuento_preventa)
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
    def crear_teatro(self,nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa,arriendo, descuento_preventa):
        evento = Teatro(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa,arriendo, descuento_preventa)
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
                ans = evento.comprar_boletas(categoria_seleccionada, cantidad_boletas, nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago,edad)
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

    def reporte_clientes_datos_basicos(self, evento_seleccionado):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                return evento.get_boleteria().datos_basicos()
    def reporte_clientes_datos_edades(self, evento_seleccionado):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                return evento.get_boleteria().datos_edades_clientes()
    def reporte_clientes_tipo_pago(self, evento_seleccionado):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                return evento.get_boleteria().datos_tipo_pago()
    def reporte_clientes_preferencia_categoria(self, evento_seleccionado):
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                return evento.get_boleteria().prefrencia_categoria()
    def generar_excel_clientes(self, evento_seleccionado):
        ans = False
        for evento in self.eventos:
            if evento.get_nombre() == evento_seleccionado:
                evento.get_boleteria().crear_excel_clientes(evento_seleccionado)
                ans = True
        return ans

    def mostrar_eventos_fecha(self, fecha_inicial, fecha_final):
        eventos = []
        for evento in self.eventos:
            fecha = evento.get_fecha()
            if fecha_inicial <= fecha <= fecha_final:
                datos = {
                    "Nombre": evento.get_nombre(),
                    "Fecha": fecha.strftime("%Y-%m-%d"),
                    "Hora apertura": evento.get_hora_apertura(),
                    "Hora show": evento.get_hora_show(),
                    "Estado": evento.get_estado(),
                    "Etapa": evento.get_boleteria().get_etapa(),
                    "Aforo": evento.get_aforo()
                }
                eventos.append(datos)

        eventos.sort(key=lambda evento: datetime.strptime(evento['Fecha'], "%Y-%m-%d"))
        return eventos

    def generar_excel_clientes_todos(self):
        lista_final = []
        for evento in self.eventos:
            lista_final += evento.get_boleteria().crear_excel_clientes_completo()
        # Convertir la lista de diccionarios a un DataFrame
        df = pd.DataFrame(lista_final)
        name = "base_de_datos_general" + ".xlsx"
        excel_file = 'archivos/' + name
        df.to_excel(excel_file, index=False)
        # Abrir la ubicación del archivo en el explorador de archivos
        webbrowser.open(os.path.realpath(excel_file))
