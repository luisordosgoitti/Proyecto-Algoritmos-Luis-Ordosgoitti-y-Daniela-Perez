from artista import Artista
from obra import Obra
from Departamentos import Departamento
from db import *
import os

class Galeria:
    def start(self):
        self.cargar_departamentos()
        """Aca va el menu"""
        
        self.mostrar_departamentos()
        
    def mostrar_departamentos(self):
        for dep in self.departamentos:
            dep.show()

    """Este Método extrae desde el endpoint de Departamentos cada uno de ellos y los guarda en una lista de objetos de tipo Departamento"""
    def cargar_departamentos(self):
        self.departamentos=[]
        departamentos_from_db=departamentos_db()
        for departamento in departamentos_from_db["departments"]:
            self.departamentos.append(Departamento(departamento["departmentId"], departamento["displayName"]))

