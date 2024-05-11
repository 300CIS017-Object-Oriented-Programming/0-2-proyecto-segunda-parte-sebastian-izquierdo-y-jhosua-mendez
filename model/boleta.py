import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import webbrowser
class Boleta():
    def __init__(self, id_boleta, nombre_cliente, id_cliente, nombre_evento, lugar_evento, direccion_evento, fecha_evento, hora_apertura, hora_show, cantidad, total):
        self.id_boleta = id_boleta
        self.nombre_cliente = nombre_cliente
        self.id_cliente = id_cliente
        self.nombre_evento = nombre_evento
        self.lugar_evento = lugar_evento
        self.direccion_evento = direccion_evento
        self.fecha_evento = fecha_evento
        self.hora_apertura = hora_apertura
        self.hora_show = hora_show
        self.cantidad = cantidad
        self.pago_total = total

    def crear_pdf(self):
        """
        Esta función crea un archivo PDF con los detalles de la boleta y lo muestra en Streamlit para su descarga.

        """
        # Crear un archivo PDF
        file_name = f"{self.id_boleta}.pdf"
        c = canvas.Canvas(file_name, pagesize=letter)
        width, height = letter

        # Agregar los detalles de la boleta al PDF
        c.drawString(50, height - 50, f"ID de la boleta: {self.id_boleta}")
        c.drawString(50, height - 70, f"Nombre del cliente: {self.nombre_cliente}")
        c.drawString(50, height - 90, f"ID del cliente: {self.id_cliente}")
        c.drawString(50, height - 110, f"Nombre del evento: {self.nombre_evento}")
        c.drawString(50, height - 130, f"Lugar del evento: {self.lugar_evento}")
        c.drawString(50, height - 150, f"Dirección del evento: {self.direccion_evento}")
        c.drawString(50, height - 170, f"Fecha del evento: {self.fecha_evento}")
        c.drawString(50, height - 190, f"Hora de apertura: {self.hora_apertura}")
        c.drawString(50, height - 210, f"Hora del show: {self.hora_show}")
        c.drawString(50, height - 230, f"Cantidad de boletas: {self.cantidad}")
        c.drawString(50, height - 250, f"Total pagado: {self.pago_total}")

        # Guardar el archivo PDF
        c.save()

        # Leer el archivo PDF en bytes
        with open(file_name, "rb") as f:
            bytes = f.read()


        # Abrir el archivo PDF en el navegador
        webbrowser.open(file_name)