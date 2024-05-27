from View import view
import streamlit as st

def main():

    st.set_page_config(
        page_title="TuBoleta.com",  # Título de la pestaña
        page_icon="⭐",  # Icono de la pestaña
        layout="wide",
        initial_sidebar_state="auto")

    # Contenido de la aplicación
    control = view.View()
    control.funciones_vista()
    return 0
main()