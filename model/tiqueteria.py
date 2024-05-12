from model.cliente import Cliente
import random
import string
from model.boleta import Boleta


class Tiqueteria():
    def __init__(self, etapa):
        self._etapa = etapa
        self._venta_regular = 0
        self._venta_preventa = 0
        self._ingresos_totales = 0
        self._boletas_vendidas = {}
        self._clientes = []
        self._categoria = {}
        self._cantidad_boletas_efectivo = {}  #tiene el valor de ingresos recaudado por categoria en efectio
        self._cantidad_boletas_tarjeta = {}  #tiene el valor de ingresos recaudado por categoria en tarjeta

    def set_etapa(self, etapa):
        self._etapa = etapa

    def get_etapa(self):
        return self._etapa

    def agregar_categoria(self, nombre_categoria, precio_categoria):
        self._categoria[nombre_categoria] = precio_categoria
        self._cantidad_boletas_efectivo[nombre_categoria] = 0
        self._cantidad_boletas_tarjeta[nombre_categoria] = 0

    def agregar_venta_preventa(self, cantidad):
        self._venta_preventa += cantidad
        self._ingresos_totales += cantidad

    def agregar_venta_regular(self, cantidad):
        self._venta_regular += cantidad
        self._ingresos_totales += cantidad

    def get_ingresos_totales(self):
        return self._ingresos_totales

    def agregar_cliente(self, cliente):
        self._clientes.append(cliente)

    def agregar_boleta_efectivo(self, categoria, cantidad):
        self._cantidad_boletas_efectivo[categoria] += cantidad

    def agregar_boleta_tarjeta(self, categoria, cantidad):
        self._cantidad_boletas_tarjeta[categoria] += cantidad

    def get_cantidad_boletas_efectivo(self, nombre_categoria):
        return self._cantidad_boletas_efectivo[nombre_categoria]

    def get_cantidad_boletas_tarjeta(self, nombre_categoria):
        return self._cantidad_boletas_tarjeta[nombre_categoria]

    def get_precio_categoria(self, nombre_categoria ):
        return self._categoria[nombre_categoria]

    def mostrar_categorias(self):
        for nombre_categoria in self._categoria.keys():
            valor = self._categoria[nombre_categoria]
            print(f"Categoria: {nombre_categoria} Precio : {valor}")

    def comprar_boleta(self, nombre_categoria, cantidad_boletas,nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago, nombre_evento , lugar_evento , direccion_evento , fecha_evento , hora_apertura , hora_show):
        precio_boleta = self._categoria[nombre_categoria]
        pago_total = precio_boleta * cantidad_boletas
        if self._etapa == "Preventa":
            self._venta_preventa += pago_total
        elif self._etapa == "Regular":
            self._venta_regular += pago_total
        self._ingresos_totales += pago_total
        self.agregar_cliente(Cliente(id_cliente, nombre_cliente, apellido_cliente, telefono_cliente, como_se_entero, nombre_categoria, metodo_pago))
        if metodo_pago == "Efectivo":
            self.agregar_boleta_efectivo(nombre_categoria, cantidad_boletas)
        else:
            self.agregar_boleta_tarjeta(nombre_categoria, cantidad_boletas)
        codigo = self.generar_codigo_unico()
        boleta = Boleta(codigo, nombre_cliente, id_cliente, nombre_evento, lugar_evento, direccion_evento, fecha_evento, hora_apertura, hora_show, cantidad_boletas,pago_total)
        self._boletas_vendidas[codigo] = boleta
        boleta.crear_pdf()
    def mostrar_clientes(self):
        print("Reporte de todos los clientes")
        for cliente in self._clientes:
            cliente.reporte()

    def reporte_financiero(self):
        pass

    def reporte_ventas_boletas(self):
        pass

    def get_categorias(self):
        categorias = []
        for nombre_categoria in self._categoria.keys():
            categorias.append(nombre_categoria)
        return categorias
    def obtener_precio(self, categoria):
        return self._categoria[categoria]

    def generar_codigo_unico(self):
        codigo = ""
        flag = True
        while flag:
            letras = ''.join(random.choice(string.ascii_uppercase) for _ in range(3))
            numeros = ''.join(random.choice(string.digits) for _ in range(3))
            codigo = letras + numeros
            if codigo not in self._boletas_vendidas.keys():
                flag = False
        return codigo
    def validar_boleta(self, codigo):
        return codigo in self._boletas_vendidas.keys()