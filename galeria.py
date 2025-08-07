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
                    id_departamento = int(input("Por favor, ingresa un número válido de ID para Departamento: "))
                except:
                    print("Ha ocurrido un error. Vuelva a intentarlo otra vez.")
            elif menu == "2":
                os.system('cls')
                self.mostrar_nacionalidades()
                try:
                    nacionalidad = input("Por favor, ingresa una nacionalidad: ")
                except:
                    print("Ha ocurrido un error. Vuelva a intentarlo otra vez.")
            elif menu == "3":
                os.system('cls')
                try:
                nombre_artista = input("Por favor, ingresa el nombre de un artista: ")
                except:
                    print("Ha ocurrido un error. Vuelva a intentarlo otra vez.")
            elif menu == "4":
                print("¡Gracias por usar nuestro catálogo!")
                break
            else:
                 print("Opción inválida.")

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

