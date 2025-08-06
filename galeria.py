from artista import Artista
from obra import Obra
from Departamentos import Departamentos
from db import *

class Galeria:
  None
  
def cargar_departamentos():
    departamentos=[]
    departamentos_from_db=departamentos_db()
    for departamento in departamentos_from_db["departments"]:
        departamentos.append(Departamento(departamento["departmentId"], departamento["displayName"]))

