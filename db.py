import requests

def departamentos_db():
    departamentos_from_api=requests.get("https://collectionapi.metmuseum.org/public/collection/v1/departments")
    return departamentos_from_api.json()






