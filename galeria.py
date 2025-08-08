from artista import Artista
from obra import Obra
from Departamentos import Departamento
from db import *
import os

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
                os.system('cls')
                self.mostrar_departamentos()
                try:
                    print("\n"+"="*80)
                    id_departamento = int(input("Por favor, ingrese un número válido de ID para Departamento: "))
                    os.system('cls')
                    print (f"Usted ha seleccionado el Id: {id_departamento}")
                    json=self.buscar_obras_por_departamento(id_departamento)
                    self.mostrar_obras_resumen(json)
                except:
                    print("Por favor, ingrese un número de la lista.")
                    
            elif menu == "2":
                os.system('cls')
                nacionalidades = nacionalidades_db()
                if nacionalidades:
                    self.mostrar_nacionalidades()
                    try:
                        nacionalidad = input("Por favor, ingrese una nacionalidad (ej. American): ")
                        if nacionalidad:
                            json=self.buscar_obras_por_nacionalidad(nacionalidad)
                            self.mostrar_obras_resumen(json)
                    except:
                        print("Por favor, ingrese una nacionalidad de la lista.")
                else:
                    print(f"No se encontraron obras de la nacionalidad: {nacionalidad_seleccionada}. Vuelva a intentarlo otra vez.")
      
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
    def buscar_artista (self,nombre):
        obras_artista=requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nombre}")
        return obras_artista.json()

    def buscar_obras_por_departamento (self,id_departamento):
        obras_departamento=requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?departmentId={id_departamento}&q=*")
        return obras_departamento.json()

    def buscar_obras_por_nacionalidad (self,nacionalidad_seleccionada):
        obras_nacionalidad=requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/search?artistOrCulture=true&q={nacionalidad_seleccionada}")
        return obras_nacionalidad.json()


"""Metodo para transformar las obras a objetos"""
    def mostrar_obras_resumen(self, json):
        indice=0
        N_obras=json["total"]
        if N_obras==0:
            return print("No se encontraron obras")
        print(f"Se encontraron: {N_obras} obras")
        lista_de_obras=json["objectIDs"]
        while True:
            mostrados, indice = self.mostrar_15(lista_de_obras, indice)
            if mostrados is None:
                return None
            eleccion=input("desea seguir? Si/No: ")
            if eleccion == "Si":
                os.system('cls')
                obras=[]
            elif eleccion == "No":
                print()
                eleccion_2=input("Desea ver Alguna Obra en especifico? Si/No: ")
                if eleccion_2 == "Si":
                        os.system('cls')
                        ID_Seleccionado=input("Ingrese el Id deseado: ")
                        #Aca iria la funcion
                elif eleccion == "No":
                    print ("\n"+"Volviendo al Menu..."+"\n")
                    return None


    def mostrar_15 (self, lista_de_IDs, indice):
        indice_f=indice+15
        if indice>=len(lista_de_IDs):
            print ("Ya se mostraron todas las obras")
            return None, indice
        IDs_de_obras_mostradas=lista_de_IDs[indice:indice_f]
        print(f"mostrando elementos del {indice+1} al {indice_f}:")
        obras=[]
        for ID in IDs_de_obras_mostradas:
            obra_api=requests.get(f"https://collectionapi.metmuseum.org/public/collection/v1/objects/{ID}")
            if obra_api.status_code == 200:
                try:
                    obra_dic=obra_api.json()
                    obras.append(Obra(obra_dic["title"], obra_dic["objectID"], obra_dic["classification"], obra_dic["objectDate"], obra_dic["primaryImage"], Artista(obra_dic["artistDisplayName"], obra_dic["artistNationality"], obra_dic["artistBeginDate"], obra_dic["artistEndDate"])))
                except requests.exceptions.JSONDecodeError:
                    print(f"El Id no corresponde a ninguna obra")
                    return None
        for obra in obras:
            obra.resumen_por_obra()
        return obras, indice_f

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

