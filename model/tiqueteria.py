from model.cliente import Cliente
import random
import string
from model.boleta import Boleta
import pandas as pd
import os
import webbrowser
class Tiqueteria():
    def __init__(self, etapa):
        self._etapa = etapa
        self._venta_regular = 0
        self._venta_preventa = 0
        self._ingresos_totales = 0
        self._boletas_vendidas = {}
        self._clientes = []
        self._categoria = {}
        self._cantidad_categorias = {}
        self._cantidad_boletas_transferencia = {}  #tiene el valor de ingresos recaudado por categoria en transferencia
        self._cantidad_boletas_efectivo = {}  #tiene el valor de ingresos recaudado por categoria en efectio
        self._cantidad_boletas_tarjeta = {}  #tiene el valor de ingresos recaudado por categoria en tarjeta
        self._asistencia = 0

    def set_etapa(self, etapa):
        self._etapa = etapa

    def get_etapa(self):
        return self._etapa

    def agregar_categoria(self, nombre_categoria, precio_categoria):
        self._categoria[nombre_categoria] = precio_categoria
        self._cantidad_boletas_efectivo[nombre_categoria] = 0
        self._cantidad_boletas_tarjeta[nombre_categoria] = 0
        self._cantidad_categorias[nombre_categoria] = 0
        self._cantidad_boletas_transferencia[nombre_categoria] = 0

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
    def agregar_boleta_transferencia(self, categoria, cantidad):
        self._cantidad_boletas_transferencia[categoria] += cantidad

    def agregar_boleta_tarjeta(self, categoria, cantidad):
        self._cantidad_boletas_tarjeta[categoria] += cantidad

    def get_cantidad_boletas_efectivo(self, nombre_categoria):
        return self._cantidad_boletas_efectivo[nombre_categoria]

    def get_cantidad_boletas_tarjeta(self, nombre_categoria):
        return self._cantidad_boletas_tarjeta[nombre_categoria]
    def get_cantidad_boletas_transferencia(self, nombre_categoria):
        return self._cantidad_boletas_transferencia[nombre_categoria]

    def get_cantidad_boletas(self, nombre_categoria):
        return self._cantidad_categorias[nombre_categoria]
    def get_precio_categoria(self, nombre_categoria ):
        return self._categoria[nombre_categoria]

    def mostrar_categorias(self):
        for nombre_categoria in self._categoria.keys():
            valor = self._categoria[nombre_categoria]
            print(f"Categoria: {nombre_categoria} Precio : {valor}")

    def comprar_boleta(self, nombre_categoria, cantidad_boletas,nombre_cliente, apellido_cliente, id_cliente, telefono_cliente, como_se_entero, metodo_pago, nombre_evento , lugar_evento , direccion_evento , fecha_evento , hora_apertura , hora_show,edad):
        precio_boleta = self._categoria[nombre_categoria]
        pago_total = precio_boleta * cantidad_boletas
        self._cantidad_categorias[nombre_categoria] += cantidad_boletas
        if self._etapa == "Preventa":
            self._venta_preventa += pago_total
        elif self._etapa == "Regular":
            self._venta_regular += pago_total
        self._ingresos_totales += pago_total
        self.agregar_cliente(Cliente(id_cliente, nombre_cliente, apellido_cliente, telefono_cliente, como_se_entero, nombre_categoria, metodo_pago, edad))
        if metodo_pago == "Efectivo":
            self.agregar_boleta_efectivo(nombre_categoria, cantidad_boletas)
        elif metodo_pago == "Tarjeta":
            self.agregar_boleta_tarjeta(nombre_categoria, cantidad_boletas)
        elif metodo_pago == "Transferencia":
            self.agregar_boleta_transferencia(nombre_categoria, cantidad_boletas)
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

    def reporte_ventas_boletas(self, nombre_evento, boletas_vendidas):
        ans = "            Reporte de ventas        \n "
        ans += f"          {nombre_evento}       \n"
        ans += "Cantidad de boletas vendidas por categoria     \n"
        for nombre_categoria in self._categoria.keys():
            ans += f"Categoria: {nombre_categoria} Cantidad de boletas vendidas: {self._cantidad_categorias[nombre_categoria]} \n"
        ans += f"Total de boletas vendidas: {boletas_vendidas} \n"
        ans += "     Ingresos     \n"
        ans += f"Venta en preventa: {self._venta_preventa} \n"
        ans += f"Venta en regular: {self._venta_regular} \n"
        ans += f"Ingresos totales: {self._ingresos_totales} \n"

        return ans

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
        ans = False
        if codigo in self._boletas_vendidas.keys():
            self._boletas_vendidas[codigo].registrar_entrada()
            ans = True
            self._asistencia += self._boletas_vendidas[codigo].get_cantidad()
        return ans

    def datos_edades_clientes(self):
        edades ={"0-18": 0, "19-30": 0, "31-50": 0, "51-70": 0, "71-100": 0}
        for cliente in self._clientes:
            edad = cliente.get_edad()
            if edad <= 18:
                edades["0-18"] += 1
            elif edad <= 30:
                edades["19-30"] += 1
            elif edad <= 50:
                edades["31-50"] += 1
            elif edad <= 70:
                edades["51-70"] += 1
            else:
                edades["71-100"] += 1
        return edades
    def prefrencia_categoria(self):
        return self._cantidad_categorias
    def datos_tipo_pago(self):
        tipo_pago = {}
        for cliente in self._clientes:
            pago = cliente.get_pago()
            if pago not in tipo_pago.keys():
                tipo_pago[pago] = 1
            else:
                tipo_pago[pago] += 1
        return tipo_pago
    def datos_basicos(self):
        ans = ""
        for cliente in self._clientes:
            ans += "Nombre: " + cliente.get_nombre() + " " + cliente.get_apellido() + " \n"
            ans += "telefono: " + cliente.get_telefono() + " \n"
            ans += "id: " + cliente.get_id() + " \n"
            ans += "Como se entero: " + cliente.get_como_se_entero() + " \n"
            ans += " \n"
        return ans
    def crear_excel_clientes(self , nombre_evento):
        # Crear una lista de diccionarios, donde cada diccionario representa un cliente
        data = []
        for cliente in self._clientes:
            data.append({
                'Nombre': cliente.get_nombre(),
                'Apellido': cliente.get_apellido(),
                'ID': cliente.get_id(),
                'Telefono': cliente.get_telefono(),
                'Como se entero': cliente.get_como_se_entero(),
                'Metodo de pago': cliente.get_pago(),
                'Edad': cliente.get_edad(),
                'Categoria': cliente.get_categoria()
            })
        # Convertir la lista de diccionarios a un DataFrame
        df = pd.DataFrame(data)
        name = nombre_evento + ".xlsx"
        excel_file = 'archivos/' + name
        df.to_excel(excel_file, index=False)
        # Abrir la ubicación del archivo en el explorador de archivos
        webbrowser.open(os.path.realpath(excel_file))

