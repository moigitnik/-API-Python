import requests


URL =  'https://api.pokemonbattle.ru/v2'
TOKEN = '752c9db7777a792931eeeec18b23ea24'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}


body_create = {
    "name": "Nona",
    "photo_id": 407
}


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

id_pokemon = response_create.json()['id']
print(id_pokemon)


pokemon_catch = {
    "pokemon_id": id_pokemon
    }


response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = pokemon_catch)
print(response_catch.text)


body_change = {
    "pokemon_id": id_pokemon,
    "name": "third",
    "photo_id": 500
    }


   response_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)
