import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '27df80243f2c9f0d72138f2375768fdb'
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN}
body_create = {
    "name": "БульбазаврКОт",
    "photo_id": 1
}

body_name = {
    "pokemon_id": "189497",
    "name": "Бочка",
    "photo_id": 2
}

body_catch = {
    "pokemon_id": "189497"
}

'''response_create= requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)'''

'''response_name= requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_name)
print(response_name.text)'''

response_catch= requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch)
print(response_catch.text)