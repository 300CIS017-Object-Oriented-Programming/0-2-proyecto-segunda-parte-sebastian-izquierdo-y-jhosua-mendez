from model.evento import Evento
from model.bar import Bar
from model.teatro import Teatro
from model.filantropico import Filantropico
from model.artista import Artista
from model.tiqueteria import Tiqueteria
from model.cliente import Cliente
from streamlit_elements import elements, mui, html, sync
from model.controlador import Controlador
from model.controller_view import Controller_view
import streamlit as st
import streamlit.components.v1 as components
import time as tm
import pandas as pd
horizontal_bar = "<hr style='margin-top: 0; margin-bottom: 0; height: 1px; border: 1px solid #635985;'><br>"    # thin divider line

class View():

    def __init__(self):
        if 'controlador' not in st.session_state: #Controlador de la logica NO TOCAR
            st.session_state['controlador'] = Controlador()

        if 'cont_view' not in st.session_state: #Controlador de la vista NO TOCAR
            st.session_state['cont_view'] = Controller_view()

    # agrega un evento tipo bar a la lista de eventos -- funcional
    def crear_bar(self):
        st.title("Formulario Bar")
        container = st.container()
        col1, col2, col3 = container.columns(3)
        with container.form("crear_evento"):
            with col1:
                nombre = st.text_input("Nombre del evento:")
                lugar = st.text_input("Lugar del evento:")
                direccion = st.text_input("Direccion del evento:")
                pago_artistas = st.number_input("Cuanto le va pagar a los artistas:", min_value=0)
            with col2:
                fecha = st.date_input("Fecha del evento:")
                hora_apertura = st.time_input("Hora de apertura del evento:")
                hora_show = st.time_input("Hora del show del evento:")
            with col3:
                estado = st.selectbox("Estado del evento:",options=["Por realizar","Realizado" , "Cancelado", "Aplazado", "Cerrado"])
                aforo = st.number_input("Aforo del evento:", min_value=1)
                etapa = st.selectbox("Etapa del evento:", options=["PREVENTA", "REGULAR"])
            creado = st.form_submit_button("Crear evento")
            if creado:
                if st.session_state['controlador'].crear_bar(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa, pago_artistas):
                    container.success("Evento creado con éxito " )
                    st.session_state['cont_view'].activate_agregando_items()

        if  st.session_state['cont_view'].get_agregando_items():
            with st.sidebar.form("agregar_categoria"):
                nombre = st.text_input("Nombre de la categoria:")
                precio = st.number_input("Precio de la categoria:", min_value=0)
                creado1 = st.form_submit_button("Agregar categoria")
                if creado1:
                    if st.session_state['controlador'].agregar_categoria(nombre, precio):
                        st.sidebar.success("Categoria agregada con éxito")
            with st.sidebar.form("agregar_artista"):
                nombre = st.text_input("Nombre del artista:")
                creado2 = st.form_submit_button("Agregar artista")
                if creado2:
                    if st.session_state['controlador'].agregar_artista(nombre):
                        st.sidebar.success("Artista agregado con éxito")
            if st.sidebar.button("Finalizar"):
                st.session_state['cont_view'].desactivate_agregando_items()
                st.session_state['cont_view'].desactivate_creando_evento()
                st.session_state['cont_view'].activate_menu()


    # agrega un evento tipo teatro a la lista de eventos -- funcional
    def crear_teatro(self):
        st.title("Formulario Teatro")
        container = st.container()
        col1, col2, col3 = container.columns(3)
        with container.form("crear_evento"):
            with col1:
                nombre = st.text_input("Nombre del evento:")
                lugar = st.text_input("Lugar del evento:")
                direccion = st.text_input("Direccion del evento:")
                arriendo = st.number_input("Costo arriendo: ", min_value=0)
            with col2:
                fecha = st.date_input("Fecha del evento:")
                hora_apertura = st.time_input("Hora de apertura del evento:")
                hora_show = st.time_input("Hora del show del evento:")
            with col3:
                estado = st.selectbox("Estado del evento:",options=["Por realizar","Realizado" , "Cancelado", "Aplazado", "Cerrado"])
                aforo = st.number_input("Aforo del evento:", min_value=1)
                etapa = st.selectbox("Etapa del evento:", options=["PREVENTA", "REGULAR"])
            creado = st.form_submit_button("Crear evento")
            if creado:
                if st.session_state['controlador'].crear_teatro(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa, arriendo):
                    container.success("Evento creado con éxito ")
                    st.session_state['cont_view'].activate_agregando_items()

        if st.session_state['cont_view'].get_agregando_items():
            with st.sidebar.form("agregar_categoria"):
                nombre = st.text_input("Nombre de la categoria:")
                precio = st.number_input("Precio de la categoria:", min_value=0)
                creado1 = st.form_submit_button("Agregar categoria")
                if creado1:
                    if st.session_state['controlador'].agregar_categoria(nombre, precio):
                        st.sidebar.success("Categoria agregada con éxito")
                with st.sidebar.form("agregar_artista"):
                    nombre = st.text_input("Nombre del artista:")
                    creado2 = st.form_submit_button("Agregar artista")
                    if creado2:
                        if st.session_state['controlador'].agregar_artista(nombre):
                            st.sidebar.success("Artista agregado con éxito")
            if st.sidebar.button("Finalizar"):
                st.session_state['cont_view'].desactivate_agregando_items()
                st.session_state['cont_view'].desactivate_creando_evento()
                st.session_state['cont_view'].activate_menu()

    # agrega un evento tipo filantropico a la lista de eventos -- funcional
    def crear_filantropico(self):
        st.title("Formulario Filantropico")
        container = st.container()
        col1, col2, col3 = container.columns(3)
        with container.form("crear_evento"):
            with col1:
                nombre = st.text_input("Nombre del evento:")
                lugar = st.text_input("Lugar del evento:")
                direccion = st.text_input("Direccion del evento:")
            with col2:
                fecha = st.date_input("Fecha del evento:")
                hora_apertura = st.time_input("Hora de apertura del evento:")
                hora_show = st.time_input("Hora del show del evento:")
            with col3:
                estado = st.selectbox("Estado del evento:",options=["Por realizar","Realizado", "Cancelado", "Aplazado", "Cerrado"])
                aforo = st.number_input("Aforo del evento:", min_value=1)
                etapa = st.selectbox("Etapa del evento:", options=["PREVENTA", "REGULAR"])
            creado = st.form_submit_button("Crear evento")
            if creado:
                if st.session_state['controlador'].crear_filantropico(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa):
                    container.success("Evento creado con éxito " )
                    st.session_state['cont_view'].activate_agregando_items()

        if st.session_state['cont_view'].get_agregando_items():
            with st.sidebar.form("agregar_patrocinio"):
                nombre = st.text_input("Nombre del patrocinador:")
                valor = st.number_input("Valor del patrocinio:", min_value=0)
                creado1 = st.form_submit_button("Agregar patrocinio")
                if creado1:
                    if st.session_state['controlador'].agregar_patrocinio(nombre, valor):
                        st.sidebar.success("Patrocinio agregado con éxito")
            with st.sidebar.form("agregar_artista"):
                nombre = st.text_input("Nombre del artista:")
                creado2 = st.form_submit_button("Agregar artista")
                if creado2:
                    if st.session_state['controlador'].agregar_artista(nombre):
                        st.sidebar.success("Artista agregado con éxito")
            if st.sidebar.button("Finalizar"):
                st.session_state['cont_view'].desactivate_agregando_items()
                st.session_state['cont_view'].desactivate_creando_evento()
                st.session_state['cont_view'].activate_menu()

    # crea un evento -- funcional
    def crear_evento(self):
        st.sidebar.title("Bienvenido a la creacion de eventos")
        st.sidebar.write("Elige el tipo de evento que deseas realizar: ")
        menu = ["Bar", "Teatro", "Filantropico"]
        opcion = {item: st.sidebar.checkbox(item) for item in menu}
        if opcion["Bar"]:
            self.crear_bar()
            print(st.session_state['cont_view'].get_creando_evento())

        if opcion["Teatro"]:
            self.crear_teatro()

        if opcion["Filantropico"]:
            self.crear_filantropico()

    # muestra el menu principal -- funcional parcialmente
    def menu_principal(self):
        components.html(
            """
        <!DOCTYPE html>
        <html>
        <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
        * {box-sizing: border-box;}
        body {font-family: Verdana, sans-serif;}
        .mySlides {display: none;}
        img {vertical-align: middle;}

        /* Slideshow container */
        .slideshow-container {
          max-width: 10000px;
          position: relative;
          margin: auto;
        }
        
        .active {
          background-color: #717171;
        }

        /* Fading animation */
        .fade {
          animation-name: fade;
          animation-duration: 3s;
        }

        @keyframes fade {
          from {opacity: .4} 
          to {opacity: 1}
        }

        /* On smaller screens, decrease text size */
        @media only screen and (max-width: 300px) {
          .text {font-size: 11px}
        }
        </style>
        </head>
        <body>

        <div class="slideshow-container">

        <div class="mySlides fade">
          <img src="https://tuboleta.com/imagenes/663e528ca0307.webp" style="width:100%">
        </div>

        <div class="mySlides fade">
          <img src="https://tuboleta.com/imagenes/663d952286dbc.webp" style="width:100%">
        </div>

        <div class="mySlides fade">
          <img src="https://tuboleta.com/imagenes/663d9522c6735.png" style="width:100%">
        </div>
        
        <div class="mySlides fade">
          <img src="https://tuboleta.com/imagenes/663e528d086a6.webp" style="width:100%">
        </div>

        </div>
        <br>

        <div style="text-align:center">
          <span class="dot"></span> 
          <span class="dot"></span> 
          <span class="dot"></span> 
        </div>

        <script>
        let slideIndex = 0;
        showSlides();

        function showSlides() {
          let i;
          let slides = document.getElementsByClassName("mySlides");
          let dots = document.getElementsByClassName("dot");
          for (i = 0; i < slides.length; i++) {
            slides[i].style.display = "none";  
          }
          slideIndex++;
          if (slideIndex > slides.length) {slideIndex = 1}    
          for (i = 0; i < dots.length; i++) {
            dots[i].className = dots[i].className.replace(" active", "");
          }
          slides[slideIndex-1].style.display = "block";  
          dots[slideIndex-1].className += " active";
          setTimeout(showSlides, 10000); // Change image every 10 seconds
        }
        </script>

        </body>
        </html> 

            """,
            height=600,
        )

        # Crea cuatro columnas
        col1, col2, col3, col4 , col5= st.columns(5)
        with col1:
            if st.button("Crear Evento"):
                st.session_state['cont_view'].activate_creando_evento()
                st.session_state['cont_view'].desactivate_menu()

        with col2:
            if st.button("Tiquetera"):
                st.session_state['cont_view'].activate_comprando()
                st.session_state['cont_view'].desactivate_menu()

        with col3:
            if st.button("Reportes"):
               pass
        with col4:
            if st.button("Modificar evento"):
                st.session_state['cont_view'].activate_modificando()
                st.session_state['cont_view'].desactivate_menu()
        with col5:
            if st.button("Validar ingreso"):
                st.session_state['cont_view'].activate_validando()
                st.session_state['cont_view'].desactivate_menu()
                st.rerun()

    def tiquetera(self):
        contenedor = st.sidebar.container()
        contenedor.title("Bienvenido a la tiquetera")
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            contenedor.write("No hay eventos disponibles")
            tm.sleep(2)
            st.session_state['cont_view'].desactivate_comprando()
            st.session_state['cont_view'].activate_menu()
        else:
            nombres_eventos = [evento.get_nombre() for evento in controller.lista_eventos()]
            evento_seleccionado = contenedor.selectbox('Selecciona un evento:', nombres_eventos)
            cartegorias = [categoria for categoria in controller.mostrar_boletas(evento_seleccionado)]
            categoria_seleccionada = contenedor.selectbox('Selecciona una categoria:', cartegorias)
            valor = controller.precio_categoria(evento_seleccionado, categoria_seleccionada)
            contenedor.write(f"El precio de la categoria seleccionada es: {valor} ")
            col1 , col2 = contenedor.columns(2)
            with col1:
                if contenedor.button("Comprar boletas"):
                    st.session_state['cont_view'].activate_formulario_cliente()
            with col2:
                if contenedor.button("Volver"):
                    st.session_state['cont_view'].activate_menu()
                    st.session_state['cont_view'].desactivate_comprando()
            if st.session_state['cont_view'].get_formulario_cliente():
                self.comprar(evento_seleccionado, categoria_seleccionada)

    def reportes(self):
        st.sidebar.title("Bienvenido a los reportes")
        print("Desea consultar por evento o por artista [1]Evento [2]Artista [3]Salir")
        opcion = int(input())
        if opcion == 1:
            print("Estos son los eventos disponibles a consultar: ")
            for evento in self._eventos:
                print(evento.get_nombre())
            print("Que evento deseas consultar:")
            nombre_evento = input()
            print("Que reporte deseas ver [1]Reporte de ventas [2]Reporte financiero [3]Reporte de clientes  [4]Salir")
        elif opcion == 2:
            print("Estos son los artistas disponibles a consultar: ")
            for artista in self._artistas:
                print(artista)
            print("Que artista deseas consultar:")
            nombre_artista = input()
            for artista in self._artistas:
                if artista.get_nombre() == nombre_artista:
                    artista.mostar_eventos()
        self.menu_principal()

    # modifica un evento -- funcional
    def modificar_evento(self):
        st.title("Eventos Disponibles:")
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            st.write("No hay eventos disponibles")
            st.session_state['cont_view'].desactivate_modificando()
        else:
            nombres_eventos = [evento.get_nombre() for evento in controller.lista_eventos()]
            evento_seleccionado = st.selectbox('Selecciona un evento:', nombres_eventos)
            opcion = st.radio("¿Qué deseas modificar?", ["Estado", "Etapa", "Eliminar"])
            # Modificar estado -- funcional
            if opcion == "Estado":
                estado = st.radio("Selecciona el nuevo estado:", ["por realizar", "realizado", "cancelado", "aplazado", "cerrado"])
                if st.button("Modificar"):
                    if controller.moficar_estado_evento(evento_seleccionado, estado):
                        st.success("Estado modificado con éxito")
                        tm.sleep(2)
                        st.session_state['cont_view'].desactivate_modificando()
                    else:
                        st.error("No se puede modificar el estado de un evento ya realizado")
            # Modificar etapa -- funcional
            elif opcion == "Etapa":
                etapa = st.radio("Selecciona la nueva etapa:", ["PREVENTA", "REGULAR"])
                if st.button("Modificar"):
                    if controller.modificar_etapa_evento(evento_seleccionado, etapa):
                        st.success("Etapa modificada con éxito")
                        tm.sleep(2)
                        st.session_state['cont_view'].desactivate_modificando()
                    else:
                        st.error("No se pudo modificar la etapa del evento.")
            # Eliminar evento -- funcional
            elif opcion == "Eliminar":
                if st.button("Eliminar"): # Si se presiona el botón
                    if controller.eliminar_evento(evento_seleccionado):
                        st.success("Evento eliminado con éxito")
                        tm.sleep(2)
                        st.session_state['cont_view'].desactivate_modificando()
                    else:
                        st.error("No se puede eliminar un evento con boletas vendidas")
    def comprar(self, evento_seleccionado, categoria_seleccionada):
        st.title("Formulario de compra de boletas")
        container = st.container()
        col1, col2 = container.columns(2)
        with container.form("comprar_boletas"):
            with col1:
                nombre = st.text_input("Nombre:")
                apellido = st.text_input("Apellido:")
                id = st.text_input("Identificación:")
                telefono = st.text_input("Teléfono:")
                como_se_entero = st.text_input("¿Cómo se enteró del evento?")
            with col2:
                cantidad = st.number_input("Cantidad de boletas:", min_value=1)
                metodo_pago = st.selectbox("Método de pago:", ["Efectivo", "Tarjeta"])
            comprado = st.form_submit_button("Comprar")
            if comprado:
                controller = st.session_state['controlador']
                if controller.disponibilidad(evento_seleccionado, cantidad):
                    if controller.comprar_boletas(evento_seleccionado, categoria_seleccionada, cantidad, nombre, apellido, id, telefono, como_se_entero, metodo_pago):
                        st.success("Boletas compradas con éxito")
                else:
                    st.error(f"No se pudo concretar la compra con exito, las diponibilidad actual es: {controller.cantidad_disponible(evento_seleccionado)} ")
                    tm.sleep(3)
                    st.session_state['cont_view'].desactivate_formulario_cliente()
                    st.rerun()

    def funciones_vista(self):
        # Define el estilo CSS para los botones
        st.markdown("""
                   <style>
                       .stButton>button {
                           width: 100%;
                           font-weight: bold;
                           font-size: 20px;
                           padding: 10px;
                           margin: 10px;
                           border-radius: 10px;
                           background-color: #00008b;
                           color: white;
                       }
                       .stButton>button:hover {
                           color: #00008b;
                           background-color: #ffffff;
                           border: 2px solid #00008b;
                       }

                   </style>
               """, unsafe_allow_html=True)
        if st.session_state['cont_view'].get_menu():
            self.menu_principal()
        if st.session_state['cont_view'].get_creando_evento():
            self.crear_evento()
        if st.session_state['cont_view'].get_modificando():
            self.modificar_evento()
        if st.session_state['cont_view'].get_comprando():
            self.tiquetera()
        if st.session_state['cont_view'].get_validando():
            self.validar_ingreso()

        footer_html = """
              <style>
                  .footer {
                      position: fixed;
                      left: 0;
                      bottom: 0;
                      width: 100%;
                      background-color: #0071CE;
                      color: white;
                      text-align: center;
                      padding: 10px 0;
                  }
              </style>
              <div class="footer">
                  <p>Made by: Joshua Mendez y Sebastián Izquierdo.</p>
              </div>
              """
        # Mostrar el footer
        st.markdown(footer_html, unsafe_allow_html=True)
    def validar_ingreso(self):
        st.title("Validar ingreso")
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            st.error("No hay eventos disponibles")

        else:
            nombres_eventos = [evento.get_nombre() for evento in controller.lista_eventos()]
            evento_seleccionado = st.selectbox('Selecciona un evento:', nombres_eventos)
            codigo = st.text_input("Ingrese el código de la boleta:")
            if st.button("Validar"):
                if controller.validar_boletas(evento_seleccionado, codigo):
                    st.success("Entrada valida")
                else:
                    st.error("Entrada invalida")
        if st.button("Volver"):
            st.session_state['cont_view'].activate_menu()
            st.session_state['cont_view'].desactivate_validando()
            st.rerun()