
class Artista():
    def __init__(self, nombre_artista):
        self.nombre_artista = nombre_artista
        self.eventos = []

    def get_nombre(self):
        return self.nombre_artista
    def add_evento(self, evento):
        self.eventos.append(evento)
    def mostrar_eventos(self):
        print(f"Artista {self.nombre_artista} ha participado en estos eventos:")
        for evento in self.eventos:
            print(self.evento.get_nombre())
