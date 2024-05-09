from model.cliente import Cliente


class Tiqueteria():
    def __init__(self, etapa):
        self._etapa = etapa
        self._venta_regular = 0
        self._venta_preventa = 0
        self._ingresos_totales = 0
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

    def comprar_boleta(self, nombre_categoria, cantidad_boletas):
        flag = False
        if nombre_categoria not in self._categoria.keys():
            print("Categoria inexistente")
        else:
            flag = True
        if (flag):
            precio_boleta = self._categoria[nombre_categoria]
            if self._etapa == "PREVENTA":
                self._venta_preventa += precio_boleta
                self._ingresos_totales += precio_boleta
            elif self._etapa == "REGULAR":
                self._venta_regular += precio_boleta
                self._ingresos_totales += precio_boleta
            metodo_pago = input("Por favor, informe el metodo pago Efectivo o Tarjeta: ")
            nombre = input("Digite su nombre: ")
            apellido = input("Digite su apellido: ")
            id = input("Digite su id: ")
            telefono = input("Digite el telefono: ")
            como_se_entero = input("Digite su como se entero: ")
            self.agregar_cliente(Cliente(id, nombre, apellido, telefono, como_se_entero, nombre_categoria, metodo_pago))
            if metodo_pago == "Efectivo":
                self.agregar_boleta_efectivo(nombre_categoria, cantidad_boletas)
            else:
                self.agregar_boleta_tarjeta(nombre_categoria, cantidad_boletas)

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