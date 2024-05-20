
class Artista():
    def __init__(self, nombre_artista):
        self.nombre_artista = nombre_artista
        self.eventos = []

    def get_nombre(self):
        return self.nombre_artista
    def add_evento(self, evento):
        self.eventos.append(evento)
    def mostrar_eventos(self):
        ans = ""
        for evento in self.eventos:
            ans += "Evento: " + evento.get_nombre() + "\n"
            ans += "Fecha: " + str(evento.get_fecha()) + "\n"
            ans += "Lugar: " + str(evento.get_lugar()) + "\n"
            ans += "Cantidad boletas vendidas: " + str(evento.get_boletas_vendidas()) + "\n"
            ans += "aforo: " + str(evento.get_boletas_vendidas() * 100 / (evento.get_aforo() + evento.get_boletas_vendidas())) + "%\n"
            ans += "\n"
        return ans
