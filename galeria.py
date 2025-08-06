from artista import Artista
from obra import Obra
from Departamentos import Departamentos
from db import *

class Galeria:
  None

"""Este Método extrae desde el endpoint de Departamentos cada uno de ellos y los guarda en una lista de objetos de tipo Departamento"""
def cargar_departamentos():
    departamentos=[]
    departamentos_from_db=departamentos_db()
    for departamento in departamentos_from_db["departments"]:
        departamentos.append(Departamento(departamento["departmentId"], departamento["displayName"]))

