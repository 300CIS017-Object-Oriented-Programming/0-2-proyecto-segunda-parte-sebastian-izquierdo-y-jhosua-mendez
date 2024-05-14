import pytest
from model.controlador import Controlador

# Fixture para inicializar un Controlador vacío antes de cada prueba
@pytest.fixture
def controlador():
    return Controlador()

def test_crear_bar(controlador):
    assert controlador.crear_bar("Bar Test", "Lugar Test", "Direccion Test", "Fecha Test", "Hora Apertura Test", "Hora Show Test", "Estado Test", 100, "Etapa Test", 500) == True
    assert len(controlador.eventos) == 1

def test_agregar_artista(controlador):
    controlador.crear_bar("Bar Test", "Lugar Test", "Direccion Test", "Fecha Test", "Hora Apertura Test", "Hora Show Test", "Estado Test", 100, "Etapa Test", 500)
    assert controlador.agregar_artista("Artista Test") == True
    assert len(controlador.artistas) == 1

def test_crear_filantropico(controlador):
    assert controlador.crear_filantropico("Evento Filantropico Test", "Lugar Test", "Direccion Test", "Fecha Test", "Hora Apertura Test", "Hora Show Test", "Estado Test", 100, "Etapa Test") == True
    assert len(controlador.eventos) == 1

def test_crear_teatro(controlador):
    assert controlador.crear_teatro("Evento Teatro Test", "Lugar Test", "Direccion Test", "Fecha Test", "Hora Apertura Test", "Hora Show Test", "Estado Test", 100, "Etapa Test", 2000) == True
    assert len(controlador.eventos) == 1


def test_agregar_categoria(controlador):
    # Creamos un evento de tipo bar para poder agregar una categoría
    controlador.crear_bar("Bar Test", "Lugar Test", "Direccion Test", "Fecha Test", "Hora Apertura Test",
                          "Hora Show Test", "Estado Test", 100, "Etapa Test", 500)

    assert controlador.agregar_categoria("Categoria Test", 50) == True
    # Verificamos si la categoría fue agregada correctamente al evento
    assert "Categoria Test" in controlador.eventos[-1].obtener_categorias()
    # Verificamos el precio de la categoría agregada
    assert controlador.eventos[-1].obtener_precio_categoria("Categoria Test") == 50


def test_agregar_patrocinio(controlador):
    # Creamos un evento para poder agregar un patrocinio
    controlador.crear_filantropico("Bar Test", "Lugar Test", "Direccion Test", "Fecha Test", "Hora Apertura Test","Hora Show Test", "Estado Test", 100, "Etapa Test")
    assert controlador.agregar_patrocinio("Patrocinio Test", 1000) == True
    # Verificamos si el patrocinio fue agregado correctamente al evento
    assert "Patrocinio Test" in controlador.eventos[-1].obtener_patrocinios()
    # Verificamos el monto del patrocinio agregado
    assert controlador.eventos[-1].get_patrocinio("Patrocinio Test") == 1000