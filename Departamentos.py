class Departamento:

    def __init__(self, id, nombre):
        self.id=id
        self.nombre=nombre

    def show (self):
        print(f"ID: {self.id}")
        print (f"Nombre del departamento: {self.nombre}")
        print("\n"+"-"*80)

"""Aca se define la clase departamento, que observando el endpoint de departamentos solo se conforma
por esos atributos, y luego se define un metodo show para posteriormente mostrar la lista de departamentos"""
