from View import view
import streamlit as st

def main():

    st.set_page_config(
        page_title="TuBoleta.com",  # Título de la pestaña
        page_icon="⭐",  # Icono de la pestaña
        layout="wide",
        initial_sidebar_state="auto")
    st.markdown("""
    <style>
    .header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 10px 16px;
        background-color: #0071CE;
        color: #333;
    }
    .header img {
        width: 300px;
        height: auto;
        margin-right: 10px;
    }
    .menu {
        display: flex;
        flex-grow: 1;
        justify-content: center;
    }
    .menu button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 10px 20px;
        margin: 0 10px;
        cursor: pointer;
    }
    .menu button:hover {
        background-color: #45a049; /* Darker Green */
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="header">'
                '<img src="https://www.tuboleta.com/img/ic_logotuboleta.svg">'
                '<div class="menu">'
                '<button>Home</button>'
                '<button>About</button>'
                '<button>Contact</button>'
                '<button>Settings</button>'
                '</div>'
                '</div>',
                unsafe_allow_html=True)
    # Contenido de la aplicación
    control = view.View()
    control.funciones_vista()
    return 0
main()