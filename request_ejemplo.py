import requests
import os

def initial_data_base():
    resp=requests.get("https://pokeapi.co/api/v2/pokemon/?offset=0&limit=2000")
    return resp.json()

def abilities_data_base (id):
    resp=requests.get(f"https://pokeapi.co/api/v2/pokemon/{id}/")
    return resp.json()

def search_abilities(db):
    print("Sus habilidades son: ")
    for abi in db["abilities"]:
        #print("Sus habilidades son: ")
        print(abi["ability"]["name"])
    
def search_pokemon(db,name):
    
    find_number=0   
    for pokemon in db['results']:
        if name in pokemon['name']:
            find_number+=1
            id=''
            for char in pokemon['url']:
                if char.isdigit():
                    id=id+char
            id=id[1:len(id)]
            print(pokemon["name"],"ID: ",id)
                        
    if find_number:
        print(f"\nSe encontraron {find_number} resultados.")
    else:
        print ("\nNo se encontraron coicidencias.") 
    


response=initial_data_base()
#print (response)
while True:
    
    option=int(input(""" 
________________________________
introduzca su opción:
   [0] salir
   [1] Buscar Pokemón.
   [2] Buscar Habilidades.
________________________________
--------> """))
    
    if option == 0:
        break
    elif option==1:
        os.system ("clear") 
        name=input("Introduzca el nombre: ") 
        search_pokemon(response,name)
        
    elif option==2:
        os.system ("clear") 
        id=input("Introduzca el ID: ") 
        db_json=abilities_data_base (id)
        search_abilities(db_json)
    else:
        print("Opción no válida. Intente nuevamente: ")

print("Hasta luego...")



