from artista import Artista
from obra import Obra
from Departamentos import Departamento
from db import *
import os
import requests

class Galeria:
    def __init__(self):
        self.departamentos = []

    """Este metodo es el principal del sistema"""
    def start(self):
        self.cargar_departamentos()
        while True:
            menu=input("""Cátalogo de Obras de MetroArt. Elija una opción:
1 - Ver Obras por Departamento.
2 - Ver Obras por Nacionalidad.
3 - Ver Obras por Nombre de Artista.
4 - Salir
--->""")
            if menu == "1":
                os.system('cls')
                self.mostrar_departamentos()
                try:
                    id_departamento = int(input("Por favor, ingrese un número válido de ID para Departamento: "))
                    self.buscar_obras_por_departamento(id_departamento)
                except:
                    print("Por favor, ingrese un número de la lista.")
                    
            elif menu == "2":
                os.system('cls')
                nacionalidades = nacionalidades_db()
                if nacionalidades:
                    self.mostrar_nacionalidades()
                    try:
                        nacionalidad = input("Por favor, ingrese una nacionalidad (ej. American): ")
                                self.buscar_obras_por_nacionalidad(nacionalidad)
                        else:
                            print("Opción inválida. Vuelva a ingresar otro número.")
                    except:
                        print("Por favor, ingrese un número de la lista.")
                
            elif menu == "3":
                os.system('cls')
                nombre_artista = input("Por favor, ingrese el nombre de un artista: ")
                self.buscar_artista(nombre_artista)
                
            elif menu == "4":
                print("¡Gracias por usar nuestro catálogo!")
                break
            else:
                 print("Opción inválida.")

    """Métodos de Búsqueda"""
    def buscar_artista (self,nombre):
        obras_artista=requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre}")
        print(obras_artista.json())

    def buscar_obras_por_departamento (self,id_departamento):
        obras_departamento=requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={id_departamento}&q=true")
        print(obras_departamento.json())

    def buscar_obras_por_nacionalidad (self,nacionalidad_seleccionada):
        try:
            parametros_de_busqueda = {
        "q": nacionalidad_seleccionada
        "artistNationality": "true"
        }
        obras_pais = requests.get(
        "https://collectionapi.metmuseum.org/public/collection/v1/search",
        params=parametros_de_busqueda
        )
        obras_pais.raise_for_status() 
        resultados = obras_pais.json()
        
        if resultados.get("objectIDs"):
            print(f"Se encontraron {len(resultados['objectIDs'])} obras de artistas de nacionalidad '{nacionalidad_seleccionada}'.")
            for object_id in resultados["objectIDs"][:20]:
                 self.mostrar_detalles_de_obra(object_id)
        else:
            print(f"No se encontraron obras de la nacionalidad: {nacionalidad_seleccionada}.")

    """Este metodo aplica el metodo show a cada uno de los objetos departamento en la lista creada en cargar departamentos"""
    def mostrar_departamentos(self):
        for dep in self.departamentos:
            dep.show()

    """Esta funcion crea una lista de nacionalidades y le añade un indice, con el fin de mostrarle al usuario una lista comoda de las nacionalidades"""
    def mostrar_nacionalidades(self):
        nacionalidades=nacionalidades_db()
        index=1
        for nacionalidad in nacionalidades:
            print(f"{index} - {nacionalidad}")
            index += 1

    """Este Método extrae desde el endpoint de Departamentos cada uno de ellos y los guarda en una lista de objetos de tipo Departamento"""
    def cargar_departamentos(self):
        self.departamentos=[]
        departamentos_from_db=departamentos_db()
        for departamento in departamentos_from_db["departments"]:
            self.departamentos.append(Departamento(departamento["departmentId"], departamento["displayName"]))

