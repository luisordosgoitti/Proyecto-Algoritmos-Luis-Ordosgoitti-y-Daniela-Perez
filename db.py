import requests

def departamentos_db():
    departamentos_from_api=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
    return departamentos_from_api.json()

def nacionalidades_db():
    archivo_nac=open("Nacionalidades.txt", "r")
    archivo_nac.readline()
    nacionalidades=[]
    for pais in archivo_nac:
        nacionalidad=pais.strip()
        nacionalidades.append(nacionalidad)
    return nacionalidades
