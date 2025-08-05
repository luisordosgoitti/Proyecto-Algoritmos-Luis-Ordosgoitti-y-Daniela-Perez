from artista import Artista

class Obra:
    def __init__(self, titulo_obra, id_obra, tipo, año_creacion, url_imagen_obra, artista):
        self.titulo_obra = titulo_obra
        self.id_obra = id_obra
        self.tipo = tipo
        self.año_creacion = año_creacion
        self.url_imagen_obra = url_imagen_obra
        self.artista = artista

    def detalles_obra(self):
        print("Características de la Obra:")
        print(f"Título de la Obra: {self.titulo_obra}")
        print(f"ID: {self.id_obra}")
        print(f"Clasificación de la Obra: {self.tipo}")
        print(f"Año de Elaboración de la Obra: {self.año_creacion}")
        print(f"Imagen: {self.url_imagen_obra}")

        if self.artista:
            print("Detalles Personales del Artista:")
            print(self.artista.get_info())
        else:
            print("No disponible.")

    def resumen_por_obra(self):
        print(f"Título de la Obra: {self.titulo_obra}")
        print(f"ID: {self.id_obra}")
        print(f"Nombre del Autor: {self.artista.nombre_artista}")
