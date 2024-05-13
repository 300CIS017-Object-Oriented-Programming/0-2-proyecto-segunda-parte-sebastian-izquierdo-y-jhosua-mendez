import streamlit as st
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

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
        self.registro_entrada = False

    def crear_pdf(self):
        """
        Esta función crea un archivo PDF con los detalles de la boleta y lo muestra en Streamlit para su descarga.

        """
        # Crear un archivo PDF
        file_name = f"{self.id_boleta}.pdf"
        c = canvas.Canvas(file_name, pagesize=letter)
        width, height = letter

        # Registrar una fuente personalizada
        pdfmetrics.registerFont(TTFont('Arial', 'Arial.ttf'))

        # Agregar una imagen
        logo = "./resource/logo.jpeg"
        c.drawInlineImage(logo, 5 * inch, height - 2 * inch, width=2 * inch, height=2 * inch)
        # Cambiar el color del texto
        c.setFillColor(HexColor(0x123456))
        # Agregar los detalles de la boleta al PDF
        c.setFont('Helvetica-Bold', 16)
        c.drawString(3*inch, height - 1*inch, "Boleta de Entrada")
        c.drawString(1*inch, height - 2*inch, f"ID de la boleta: {self.id_boleta}")
        # Cambiar la fuente y el tamaño del texto
        c.setFont('Helvetica', 12)
        c.drawString(1*inch, height - 3*inch, f"Nombre: {self.nombre_cliente}")
        c.drawString(4*inch, height - 3*inch, f"CC: {self.id_cliente}")
        c.drawString(1*inch, height - 4*inch, f"Nombre del evento: {self.nombre_evento}")
        c.drawString(4*inch, height - 4*inch, f"Lugar: {self.lugar_evento}")
        c.drawString(1*inch, height - 5*inch, f"Dirección: {self.direccion_evento}")
        c.drawString(4*inch, height - 5*inch, f"Fecha: {self.fecha_evento}")
        c.drawString(1*inch, height - 6*inch, f"Hora de apertura: {self.hora_apertura}")
        c.drawString(4*inch, height - 6*inch, f"Hora del show: {self.hora_show}")
        c.drawString(1*inch, height - 7*inch, f"Cantidad: {self.cantidad}")
        c.drawString(4*inch, height - 7*inch, f"Total pagado: {self.pago_total}")

        # Guardar el archivo PDF
        c.save()

        # Leer el archivo PDF en bytes
        with open(file_name, "rb") as f:
            bytes = f.read()


        # Abrir el archivo PDF en el navegador
        webbrowser.open(file_name)

    def get_cantidad(self):
        return self.cantidad
    def registrar_entrada(self):
        """
        Esta función registra la entrada del cliente al evento.
        """
        self.registro_entrada = True