import requests
import json

def Planeta_Arido():
    request = requests.get(f"https://swapi.dev/api/planets/1)
    data = json.loads(request.content)
    print("Peliculas de con aparicion de un planeta arido")
    print(data['films'])
    
    
def Cuantos_Wookies():
    request = requests.get(f"https://swapi.dev/api/species/3)
    data = json.loads(request.content)
    print("Wookies en sexta pelicula (Return of the Jedi)")
    print(data['people'])
    
    
def Gran Nave():
    request = requests.get(f"https://swapi.dev/api/starships/9)
    data = json.loads(request.content)
    print("Nave mas grande de la saga")
    print(data)
    
    
if name == 'main':
    Planeta_Arido()
    Cuantos_Wookies()
    Gran Nave()
