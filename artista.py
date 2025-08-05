class Artista:
    def __init__(self, nombre_artista, nacionalidad_artista, fecha_nacimiento, fecha_muerte):
        self.nombre_artista = nombre_artista
        self.nacionalidad_artista = nacionalidad_artista
        self.fecha_nacimiento = fecha_nacimiento
        self.fecha_muerte = fecha_muerte

    def mostrar_info(self):
        print(f"Nombre del Artista: {self.nombre_artista}.")
        print(f"Nacionalidad del Artista: {self.nacionalidad_artista}.")
        print(f"Nacido: {self.fecha_nacimiento}.")
        print(f"Fallecido: {self.fecha_muerte}.")
