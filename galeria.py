from artista import Artista
from obra import Obra
from Departamentos import Departamento
from db import *
import os
from PIL import Image

class Galeria:
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
"""Este método de os.system('cls') se aprendió en el video de Aulas Virtuales del prof. Guillén de RESTful APIs. En este caso, se adaptó el método de os.system('clear') de
Linux a la alternativa de Windows"""
                os.system('cls')
                self.mostrar_departamentos()
                try:
                    print("\n"+"="*80)
                    id_departamento = int(input("Por favor, ingrese un número válido de ID para Departamento: "))
                    os.system('cls')
                    print (f"Usted ha seleccionado el ID: {id_departamento}")
                    json = self.buscar_obras_por_departamento(id_departamento)
                    self.mostrar_obras_resumen(json)
                except:
                    print("Por favor, ingrese un número de la lista.")
                    
            elif menu == "2":
                os.system('cls')
                self.mostrar_nacionalidades()
                try:
                    nacionalidad = input("Por favor, ingrese una nacionalidad (ej. American): ")
                    if nacionalidad:
                        json=self.buscar_obras_por_nacionalidad(nacionalidad)
                        self.mostrar_obras_resumen(json)
                except:
                    print("Por favor, ingrese una nacionalidad de la lista.")

            elif menu == "3":
                os.system('cls')
                nombre_artista = input("Por favor, ingrese el nombre de un artista: ")
                json=self.buscar_artista(nombre_artista)
                self.mostrar_obras_resumen(json)
                
            elif menu == "4":
                print("¡Gracias por usar nuestro catálogo!")
                break
            else:
                print("\n"+"="*80)
                print("Opción inválida.")
                print()

    """Métodos de Búsqueda"""
    def buscar_artista(self, nombre):
        obras_artista = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre}")
        return obras_artista.json()

    def buscar_obras_por_departamento(self, id_departamento):
        obras_departamento = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={id_departamento}&q=*")
        return obras_departamento.json()

    def buscar_obras_por_nacionalidad(self, nacionalidad_seleccionada):
        obras_nacionalidad = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad_seleccionada}")
        return obras_nacionalidad.json()

    """Metodo para transformar las obras a objetos"""
    def mostrar_obras_resumen(self, json_data):
        if not json_data or json_data.get("total", 0) == 0:
            print("No se encontraron obras para su criterio de búsqueda. Volviendo al menú...")
            return

        n_obras = json_data["total"]
        print(f"Se encontraron: {n_obras} obras.")
        lista_de_obras = json_data["objectIDs"]
        indice = 0
        
        while True:
            self.mostrar_15(lista_de_obras, indice)
            indice += 15

            if indice >= len(lista_de_obras):
                print("Ya se han mostrado todas las obras encontradas.")
                break

            eleccion = input("¿Desea seguir? Si/No: ").lower()
            if eleccion == "si":
                os.system('cls')
                continue
            elif eleccion == "no":
                break
            else:
                print("Opción no válida.")
                break

        while True:
            eleccion_2 = input("¿Desea ver Alguna Obra en especifico? Si/No: ").lower()
            if eleccion_2 == "si":
                self.mostrar_detalles_obra()

            elif eleccion_2 == "no":
                print ("Volviendo al Menú...")
                return
            else:
                print("Opción no válida, por favor responda 'Si' o 'No'.")

    def mostrar_15 (self, lista_de_IDs, indice):
        indice_f=indice+15
        if indice>=len(lista_de_IDs):
            print ("Ya se mostraron todas las obras")
            return None, indice
        IDs_de_obras_mostradas=lista_de_IDs[indice:indice_f]
        print(f"mostrando elementos del {indice+1} al {indice_f}:")
        obras=[]

        for ID in IDs_de_obras_mostradas:
            try:
                obra_api = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{ID}")
                if obra_api.status_code == 200:
                    obra_dic = obra_api.json()
                    artista = Artista(
                        obra_dic.get("artistDisplayName", "Unknown"), 
                        obra_dic.get("artistNationality", "Unknown"),
                        obra_dic.get("artistBeginDate", "No se tiene la fecha."),
                        obra_dic.get("artistEndDate", "No se tiene la fecha.")
                    )
                    obra = Obra(
                        obra_dic.get("title", "Sin Título"),
                        obra_dic.get("objectID", "N/A"),
                        obra_dic.get("classification", "No clasificado"),
                        obra_dic.get("objectDate", "Sin fecha"),
                        obra_dic.get("primaryImage", ""),
                        artista
                    )
                    obra.resumen_por_obra()
            except:
                print(f"No se pudo obtener la información para la obra con ID: {ID}")

    def mostrar_detalles_obra(self):
        try:
            id_obra = int(input("Por favor, ingrese el ID de la obra que desea ver en detalle: "))
            
            obra_api = requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{id_obra}")
            
            if obra_api.status_code == 200:
                obra_dic = obra_api.json()
                artista = Artista(
                    obra_dic.get("artistDisplayName", "Desconocido"),
                    obra_dic.get("artistNationality", "Desconocida"),
                    obra_dic.get("artistBeginDate", "N/A"),
                    obra_dic.get("artistEndDate", "N/A")
                )
                obra = Obra(
                    obra_dic.get("title", "Sin Título"),
                    obra_dic.get("objectID", "N/A"),
                    obra_dic.get("classification", "No clasificado"),
                    obra_dic.get("objectDate", "Sin fecha"),
                    obra_dic.get("primaryImageSmall", ""),
                    artista
                )
                
                obra.detalles_obra()

                if obra.url_imagen_obra:
                    ver_imagen = input("¿Desea ver la imagen de esta obra? (Si/No): ").lower()
                    if ver_imagen == "si":
                        print("Cargando imagen de obra...")
                        self.mostrar_imagen_desde_url(obra.url_imagen_obra)
                else:
                    print("Esta obra no tiene una imagen disponible en nuestra base de datos.")
            else:
                print(f"No se encontró ninguna obra con el ID {id_obra}.")

        except:
            print("Error.")

    def mostrar_imagen_desde_url(self, url):
        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                img = Image.open(response.raw)
                img.show()
            else:
                print("No se pudo descargar la imagen.")
        except:
            print("Ocurrió un error al mostrar la imagen.")

    """Este Método extrae desde el endpoint de Departamentos cada uno de ellos y los guarda en una lista de objetos de tipo Departamento"""
    def cargar_departamentos(self):
            self.departamentos = []
            departamentos_from_db = departamentos_db()
            for departamento in departamentos_from_db["departments"]:
                self.departamentos.append(Departamento(departamento["departmentId"], departamento["displayName"]))

    """Este metodo aplica el metodo show a cada uno de los objetos departamento en la lista creada en cargar departamentos"""
    def mostrar_departamentos(self):
            print("Lista de Departamentos Disponibles:")
            for dep in self.departamentos:
                dep.show()
            
    """Esta funcion crea una lista de nacionalidades y le añade un indice, con el fin de mostrarle al usuario una lista comoda de las nacionalidades"""
    def mostrar_nacionalidades(self):
            print("Lista de Nacionalidades Disponibles:")
            nacionalidades=nacionalidades_db()
            index=1
            for nacionalidad in nacionalidades:
                print(f"{index} - {nacionalidad}")
                index += 1
