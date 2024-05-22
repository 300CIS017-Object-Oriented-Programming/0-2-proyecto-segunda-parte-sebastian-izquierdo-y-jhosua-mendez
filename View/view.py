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
import plotly.express as px
from datetime import date
from streamlit_extras.stylable_container import stylable_container
import os
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
                estado = st.selectbox("Estado del evento:",options=["Por realizar", "Realizado", "Cancelado", "Aplazado", "Cerrado"])
                aforo = st.number_input("Aforo del evento:", min_value=1)
                etapa = st.selectbox("Etapa del evento:", options=["Preventa", "Regular"])
            creado = st.form_submit_button("Crear evento")
            if creado:
                if nombre and lugar and direccion and fecha and hora_apertura and hora_show and estado and aforo and etapa and pago_artistas:
                    if st.session_state['controlador'].crear_bar(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa, pago_artistas):
                        container.success("Evento creado con éxito ")
                        st.session_state['cont_view'].activate_agregando_items()
                else:
                    st.error("Por favor llene todos los campos")

        if  st.session_state['cont_view'].get_agregando_items():
            with st.sidebar.form("agregar_categoria"):
                nombre = st.text_input("Nombre de la categoria:")
                precio = st.number_input("Precio de la categoria:", min_value=0)
                creado1 = st.form_submit_button("Agregar categoria")
                if creado1:
                    if nombre and precio:
                        if st.session_state['controlador'].agregar_categoria(nombre, precio):
                            st.sidebar.success("Categoria agregada con éxito")
                    else:
                        st.error("Por favor llene todos los campos")

            with st.sidebar.form("agregar_artista"):
                nombre = st.text_input("Nombre del artista:")
                creado2 = st.form_submit_button("Agregar artista")
                if creado2:
                    if nombre:
                        if st.session_state['controlador'].agregar_artista(nombre):
                            st.sidebar.success("Artista agregado con éxito")
                    else:
                        st.error("Por favor llene todos los campos")

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
                etapa = st.selectbox("Etapa del evento:", options=["Preventa", "Regular"])
            creado = st.form_submit_button("Crear evento")
            if creado:
                if nombre and lugar and direccion and fecha and hora_apertura and hora_show and estado and aforo and etapa and arriendo:
                    if st.session_state['controlador'].crear_teatro(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa, arriendo):
                        container.success("Evento creado con éxito ")
                        st.session_state['cont_view'].activate_agregando_items()
                else:
                    st.error("Por favor llene todos los campos")

        if st.session_state['cont_view'].get_agregando_items():
            with st.sidebar.form("agregar_categoria"):
                nombre = st.text_input("Nombre de la categoria:")
                precio = st.number_input("Precio de la categoria:", min_value=0)
                creado1 = st.form_submit_button("Agregar categoria")
                if creado1:
                    if nombre and precio:
                        if st.session_state['controlador'].agregar_categoria(nombre, precio):
                            st.sidebar.success("Categoria agregada con éxito")
                    else:
                        st.error("Por favor llene todos los campos")
                with st.sidebar.form("agregar_artista"):
                    nombre = st.text_input("Nombre del artista:")
                    creado2 = st.form_submit_button("Agregar artista")
                    if creado2:
                        if nombre:
                            if st.session_state['controlador'].agregar_artista(nombre):
                                st.sidebar.success("Artista agregado con éxito")
                        else:
                            st.error("Por favor llene todos los campos")

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
                etapa = st.selectbox("Etapa del evento:", options=["Preventa", "Regular"])
            creado = st.form_submit_button("Crear evento")
            if creado:
                if nombre and lugar and direccion and fecha and hora_apertura and hora_show and estado and aforo and etapa:
                    if st.session_state['controlador'].crear_filantropico(nombre, lugar, direccion, fecha, hora_apertura, hora_show, estado, aforo, etapa):
                        container.success("Evento creado con éxito ")
                        st.session_state['cont_view'].activate_agregando_items()
                else:
                    st.error("Por favor llene todos los campos")
        if st.session_state['cont_view'].get_agregando_items():
            with st.sidebar.form("agregar_patrocinio"):
                nombre = st.text_input("Nombre del patrocinador:")
                valor = st.number_input("Valor del patrocinio:", min_value=0)
                creado1 = st.form_submit_button("Agregar patrocinio")
                if creado1:
                    if nombre and valor:
                        if st.session_state['controlador'].agregar_patrocinio(nombre, valor):
                            st.sidebar.success("Patrocinio agregado con éxito")
                    else:
                        st.error("Por favor llene todos los campos")
            with st.sidebar.form("agregar_artista"):
                nombre = st.text_input("Nombre del artista:")
                creado2 = st.form_submit_button("Agregar artista")
                if creado2:
                    if nombre:
                        if st.session_state['controlador'].agregar_artista(nombre):
                            st.sidebar.success("Artista agregado con éxito")
                    else:
                        st.error("Por favor llene todos los campos")

    # crea un evento -- funcional
    def crear_evento(self):
        cont_view = st.session_state['cont_view']
        #Sidebar
        rounded_image_html = f"""
                <div style="display: flex; justify-content: center; align-items: center;">
                    <img src="{"https://img001.prntscr.com/file/img001/uXUflxGISjWRIjH2sE4Qtg.png"}" style="border-radius: 15px; width: 100%; margin-bottom: 25px">
                </div>
                """

        # Mostramos la imagen en el contenedor
        st.sidebar.markdown(rounded_image_html, unsafe_allow_html=True)
        genre = st.sidebar.radio("Selecciona el tipo de evento:", ["Bar", "Teatro", "Filantropico"], index=None)
        if genre:
            cont_view.desactivate_crear_evento_pagina()
        if genre == "Bar":
            st.session_state['cont_view'].desactivate_crear_evento_pagina()
            self.crear_bar()

        if genre == "Teatro":
            st.session_state['cont_view'].desactivate_crear_evento_pagina()
            self.crear_teatro()

        if genre == "Filantropico":
            st.session_state['cont_view'].desactivate_crear_evento_pagina()
            self.crear_filantropico()

        if st.sidebar.button("Volver"):
            st.session_state['cont_view'].desactivate_agregando_items()
            st.session_state['cont_view'].desactivate_creando_evento()
            st.session_state['cont_view'].activate_menu()
            st.session_state['cont_view'].desactivate_crear_evento_pagina()
            st.rerun()
        # Página

        if cont_view.get_crear_evento_pagina():
            st.markdown(
                """
                <style>
                .stApp {
                    background-color: #0071CE;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            with st.title("Hola"):
                st.title("Bienvenido a la creacion de eventos")
                st.image("https://img001.prntscr.com/file/img001/JmNmgn5dRHeKRvu1AqnhcA.png", use_column_width=True)


    # muestra el menu principal -- funcional parcialmente
    def menu_principal(self):
        # Crear un contenedor con la clase 'blue-background'
        with stylable_container(
                key="container_with_border",
                css_styles="""
                        {
                            border: 1px solid rgba(49, 51, 63, 0.2);
                            border-radius: 0.5rem;
                            padding: calc(1em - 1px);
                            background-color: #0071CE;
                        }
                        """,
        ):
            # Crear las columnas dentro del contenedor
            col1, col2, col3, col4, col5, col6 = st.columns(6)

            with col1:
                st.markdown(
                    '<img src="https://www.tuboleta.com/img/ic_logotuboleta.svg" style="width: 230px;" class="header-img">',
                    unsafe_allow_html=True)

            with col2:
                if st.button("Crear Evento"):
                    st.session_state['cont_view'].activate_creando_evento()
                    st.session_state['cont_view'].activate_crear_evento_pagina()
                    st.session_state['cont_view'].desactivate_menu()
                    st.experimental_rerun()

            with col3:
                if st.button("Tiquetera"):
                    st.session_state['cont_view'].activate_tiqueteria_pagina()
                    st.session_state['cont_view'].activate_comprando()
                    st.session_state['cont_view'].desactivate_menu()
                    st.experimental_rerun()

            with col4:
                if st.button("Reportes"):
                    st.session_state['cont_view'].activate_reportes()
                    st.session_state['cont_view'].desactivate_menu()
                    st.experimental_rerun()

            with col5:
                if st.button("Modificar evento"):
                    st.session_state['cont_view'].activate_modificando()
                    st.session_state['cont_view'].desactivate_menu()
                    st.experimental_rerun()

            with col6:
                if st.button("Validar ingreso"):
                    st.session_state['cont_view'].activate_validando()
                    st.session_state['cont_view'].desactivate_menu()
                    st.experimental_rerun()
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
            height=650,
        )

        # Dividir el espacio en 4 columnas
        col11, col21, col31, col41 = st.columns(4)

        # En cada columna puedes agregar contenido independiente
        with col11:
            st.image("https://img001.prntscr.com/file/img001/lLnshW2vTJ6LEGt4BPQV1g.png", use_column_width=True)

        with col21:
            st.image("https://img001.prntscr.com/file/img001/8mPX8H0WT2yxcvht9YbNVw.png", use_column_width=True)

        with col31:
            st.image("https://img001.prntscr.com/file/img001/sRhpaV1wQQmGQE4PC0KM_A.png", use_column_width=True)

        with col41:
            st.image("https://img001.prntscr.com/file/img001/BuSoqDd_RG663E1VganPcQ.png", use_column_width=True)

        components.html(
            """
            """,
            height=25,
        )
        # Dividir el espacio en 4 columnas
        col12, col22, col32, col42 = st.columns(4)

        # En cada columna puedes agregar contenido independiente
        with col12:
            st.image("https://img001.prntscr.com/file/img001/fX6VnsIlT-mU5JbEYlUQyg.png", use_column_width=True)

        with col22:
            st.image("https://img001.prntscr.com/file/img001/MAJ8Isc0ShCXRfcHmEcorQ.png", use_column_width=True)

        with col32:
            st.image("https://img001.prntscr.com/file/img001/_ngkqOXWScaqI7SxTl8tMA.png", use_column_width=True)

        with col42:
            st.image("https://img001.prntscr.com/file/img001/H-F79RDqT0mwJChlIVfFZA.png", use_column_width=True)

        components.html(
            """
            """,
            height=50,
        )

        self.dashboard()

    def tiquetera(self):
        # Sidebar
        contenedor = st.sidebar.container()
        rounded_image_html = f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="{"https://img001.prntscr.com/file/img001/IUlSufvZTuWtKoR876hPog.png"}" style="border-radius: 15px; width: 100%; margin-bottom: 50px">
        </div>
        """

        # Mostramos la imagen en el contenedor
        contenedor.markdown(rounded_image_html, unsafe_allow_html=True)
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
            contenedor.write(f"El precio de la categoria seleccionada es: ${valor} ")
            col1 , col2 = contenedor.columns(2)
            with col1:
                if contenedor.button("Comprar boletas"):
                    st.session_state['cont_view'].activate_formulario_cliente()
                    st.session_state['cont_view'].desactivate_tiqueteria_pagina()

            with col2:
                # this does not show, just to make some space for the columns
                print(".")
            if st.session_state['cont_view'].get_formulario_cliente() and not st.session_state['cont_view'].get_tiqueteria_pagina():
                self.comprar(evento_seleccionado, categoria_seleccionada)
        if contenedor.button("Volver"):
            st.session_state['cont_view'].activate_menu()
            st.session_state['cont_view'].desactivate_comprando()
            st.session_state['cont_view'].desactivate_tiqueteria_pagina()
            st.rerun()
        # Página

        if st.session_state['cont_view'].get_tiqueteria_pagina():
            st.markdown(
                """
                <style>
                .stApp {
                    background-color: #0071CE;
                }
                </style>
                """,
                unsafe_allow_html=True
            )

            with st.title("Hola"):
                st.title("Bienvenido a la creacion de eventos")
                st.image("https://img001.prntscr.com/file/img001/WnnxdVPZRF2Uf7Gcb0Zb4g.png", use_column_width=True)

    def reportes(self):
        rounded_image_html = f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="{"https://img001.prntscr.com/file/img001/tAMoOhUCRIutX1fXeaHR5Q.png"}" style="border-radius: 15px; width: 100%; margin-bottom: 50px">
        </div>
        """

        # Mostramos la imagen en el contenedor
        st.markdown(rounded_image_html, unsafe_allow_html=True)
        col1, col2, col3, col4, col5 = st.columns(5)
        cont_view = st.session_state['cont_view']
        with col1:
            if st.button("Reporte de ventas"):
                cont_view.activate_reporte_ventas()
                cont_view.desactivate_reporte_financiero()
                cont_view.desactivate_reporte_clientes()
                cont_view.desactivate_consulta_artista()

        with col2:
            if st.button("Reporte financiero"):
                cont_view.desactivate_reporte_ventas()
                cont_view.desactivate_reporte_clientes()
                cont_view.desactivate_consulta_artista()
                cont_view.activate_reporte_financiero()
        with col3:
            if st.button("Reporte de clientes"):
                cont_view.activate_reporte_clientes()
                cont_view.desactivate_reporte_ventas()
                cont_view.desactivate_consulta_artista()
                cont_view.desactivate_reporte_financiero()
        with col4:
            if st.button("Consultar artista"):
                cont_view.desactivate_reporte_ventas()
                cont_view.desactivate_reporte_clientes()
                cont_view.desactivate_reporte_financiero()
                cont_view.activate_consulta_artista()
        with col5:
            if st.button("Volver"):
                st.session_state['cont_view'].activate_menu()
                st.session_state['cont_view'].desactivate_reportes()
                st.rerun()
        if cont_view.get_reporte_ventas():
            self.reporte_ventas()
        if cont_view.get_reporte_financiero():
            self.reporte_financiero()
        if cont_view.get_reporte_clientes():
            self.reporte_clientes()
        if cont_view.get_consulta_artista():
            self.consultar_artista()


    # modifica un evento -- funcional
    def modificar_evento(self):
        rounded_image_html = f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="{"https://img001.prntscr.com/file/img001/NS6RMqhRRXSpvXqB7EHHpw.png"}" style="border-radius: 15px; width: 100%; margin-bottom: 50px">
        </div>
        """

        # Mostramos la imagen en el contenedor
        st.markdown(rounded_image_html, unsafe_allow_html=True)
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            st.error("No hay eventos disponibles")

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
                    else:
                        st.error("No se puede modificar el estado de un evento ya realizado")
            # Modificar etapa -- funcional
            elif opcion == "Etapa":
                etapa = st.radio("Selecciona la nueva etapa:", ["PREVENTA", "REGULAR"])
                if st.button("Modificar"):
                    if controller.modificar_etapa_evento(evento_seleccionado, etapa):
                        st.success("Etapa modificada con éxito")
                    else:
                        st.error("No se pudo modificar la etapa del evento.")
            # Eliminar evento -- funcional
            elif opcion == "Eliminar":
                if st.button("Eliminar"): # Si se presiona el botón
                    if controller.eliminar_evento(evento_seleccionado):
                        st.success("Evento eliminado con éxito")
                        st.rerun()
                    else:
                        st.error("No se puede eliminar un evento con boletas vendidas")
        if st.button("Volver"):
            st.session_state['cont_view'].desactivate_modificando()
            st.session_state['cont_view'].activate_menu()
            st.rerun()

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
                edad = st.number_input("Edad:", min_value=14)
                metodo_pago = st.radio("Método de pago:", ["Efectivo", "Tarjeta", "Transferencia"])
            comprado = st.form_submit_button("Comprar")
            if comprado:
                controller = st.session_state['controlador']
                if controller.disponibilidad(evento_seleccionado, cantidad):
                    if controller.comprar_boletas(evento_seleccionado, categoria_seleccionada, cantidad, nombre, apellido, id, telefono, como_se_entero, metodo_pago,edad):
                        st.success("Boletas compradas con éxito")
                else:
                    st.error(f"No se pudo concretar la compra con exito, las diponibilidad actual es: {controller.cantidad_disponible(evento_seleccionado)} ")


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
                           background-color: #0071CE;
                           color: white;
                       }
                       .stButton>button:hover {
                           font-weight: bold;
                           font-size: 25px;
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
        if st.session_state['cont_view'].get_reportes():
            self.reportes()

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
        rounded_image_html = f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="{"https://img001.prntscr.com/file/img001/fFVaTSwIRsW0kUJbpAmmDQ.png"}" style="border-radius: 15px; width: 100%; margin-bottom: 50px">
        </div>
        """

        # Mostramos la imagen en el contenedor
        st.markdown(rounded_image_html, unsafe_allow_html=True)
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            st.error("No hay eventos disponibles")

        else:
            nombres_eventos = [evento.get_nombre() for evento in controller.lista_eventos()]
            evento_seleccionado = st.selectbox('Selecciona un evento:', nombres_eventos)
            codigo = st.text_input("Ingrese el código de la boleta:")
            if st.button("Validar"):
                if controller.validar_boletas(evento_seleccionado, codigo):
                    st.success("Se registro el ingreso con éxito")
                else:
                    st.error("No se pudo registrar el ingreso")
        if st.button("Volver"):
            st.session_state['cont_view'].activate_menu()
            st.session_state['cont_view'].desactivate_validando()
            st.rerun()
    def reporte_ventas(self):
        st.title("Reporte de Ventas 🛒")
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            st.error("No hay eventos disponibles")
        else:
            nombres_eventos = [evento.get_nombre() for evento in controller.lista_eventos()]
            evento_seleccionado = st.selectbox('Selecciona un evento:', nombres_eventos)
            report = controller.reporte_de_ventas(evento_seleccionado)
            st.text(report)
    def reporte_financiero(self):
        st.title("Reporte Financiero 📈")
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            st.error("No hay eventos disponibles")
        else:
            nombres_eventos = [evento.get_nombre() for evento in controller.lista_eventos()]
            evento_seleccionado = st.selectbox('Selecciona un evento:', nombres_eventos)
            st.title("Reporte financiero de " + evento_seleccionado)
            evento = controller.get_evento(evento_seleccionado)
            tiquet = controller.get_tiqueteria(evento_seleccionado)
            for ciclo_categoria in tiquet.get_categorias():
                st.subheader(f"Categoria: {ciclo_categoria}")
                st.write("Ingresos por Efectivo:" + str(tiquet.get_cantidad_boletas_efectivo(ciclo_categoria)))
                st.write("Ingresos por Tarjeta:" + str(tiquet.get_cantidad_boletas_tarjeta(ciclo_categoria)))
                st.write("Ingresos por Transferencia:" + str(tiquet.get_cantidad_boletas_transferencia(ciclo_categoria)))
                st.write("Ingresos Totales:" + str(tiquet.get_cantidad_boletas(ciclo_categoria)))
    def reporte_clientes(self):
        st.title("Reporte de Clientes 👥")
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            st.error("No hay eventos disponibles")
        else:
            nombres_eventos = [evento.get_nombre() for evento in controller.lista_eventos()]
            evento_seleccionado = st.selectbox('Selecciona un evento:', nombres_eventos)
            st.text(controller.reporte_clientes_datos_basicos(evento_seleccionado))
            edades = controller.reporte_clientes_datos_edades(evento_seleccionado)
            # Convert the dictionary to a DataFrame
            df = pd.DataFrame(list(edades.items()), columns=['edades', 'N° Clientes'])
            # Create the bar chart using Plotly
            fig = px.bar(df, x='edades', y='N° Clientes', title='Distribucion edades de los clientes')
            # Display the figure in Streamlit
            st.plotly_chart(fig)
            tipo_pagos = controller.reporte_clientes_tipo_pago(evento_seleccionado)
            df = pd.DataFrame(list(tipo_pagos.items()), columns=['Tipo de pago', 'N° Clientes'])
            fig = px.bar(df, x='Tipo de pago', y='N° Clientes', title='Distribucion tipo de pago de los clientes')
            st.plotly_chart(fig)
            categorias = controller.reporte_clientes_preferencia_categoria(evento_seleccionado)
            df = pd.DataFrame(list(categorias.items()), columns=['Categoria', 'N° Clientes'])
            fig = px.bar(df, x='Categoria', y='N° Clientes', title='Distribucion de preferencia de categoria de los clientes')
            st.plotly_chart(fig)
            if st.button("Generar excel"):
                controller.generar_excel_clientes(evento_seleccionado)

    def consultar_artista(self):
        st.title("Consultar Artista 🎙️")
        controller = st.session_state['controlador']
        if controller.get_tamanio_eventos() == 0:
            st.error("No hay artistas disponibles")
        else:
            nombres_artistas = [artista for artista in controller.lista_artistas()]
            artista_seleccionado = st.selectbox('Selecciona un artista:', nombres_artistas)
            st.title("Eventos en los que ha participado el artista")
            st.text(controller.mostrar_eventos(artista_seleccionado))
    def dashboard(self):
        controller = st.session_state['controlador']
        rounded_image_html = f"""
        <div style="display: flex; justify-content: center; align-items: center;">
            <img src="{"https://img001.prntscr.com/file/img001/8XV8AzniROukdr1nk3c2wA.png"}" style="border-radius: 15px; width: 100%; margin-bottom: 50px">
        </div>
        """

        # Mostramos la imagen en el contenedor
        st.markdown(rounded_image_html, unsafe_allow_html=True)

        col1, col2 = st.columns(2)

        with col1:
            fecha_inicial = st.date_input("Fecha inicial", value=date.today())
        with col2:
            fecha_final = st.date_input("Fecha final", value=date.today())

        # Validar que las fechas sean correctas
        if fecha_inicial > fecha_final:
            st.error("La fecha inicial no puede ser mayor que la fecha final")
        else:
            try:
                lista = controller.mostrar_eventos_fecha(fecha_inicial, fecha_final)
                df_eventos = pd.DataFrame(lista)

                if df_eventos.empty:
                    st.warning("No se encontraron eventos en el rango de fechas proporcionado.")
                else:
                    # Mostrar el DataFrame en una tabla en Streamlit
                    st.table(df_eventos)
            except Exception as e:
                st.error(f"Ocurrió un error al obtener los eventos: {e}")