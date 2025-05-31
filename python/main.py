import requests


URL =  'https://api.pokemonbattle.ru/v2'
urlcatch = 'https://api.pokemonbattle.ru/v2/trainers/add_pokeball'
TOKEN = '752c9db7777a792931eeeec18b23ea24'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
BODY =  {
    "trainer_token": "token",
    "email": "mymail@mail.ru",
    "password": "student"
}


body_creat = {
    "name": "Nona",
    "photo_id": 407
}


    # создание покемона
respons_creat = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creat)
print(respons_creat.text)

id_pokemon = respons_creat.json()['id']
print(id_pokemon)

pokemon_catch = {
    "pokemon_id": id_pokemon
    }

       # ловля покемона
to_catch_pokemons = requests.post(url = urlcatch, headers = HEADER, json = pokemon_catch)
print(to_catch_pokemons.text)
# выводит результат


body_change = {
    "pokemon_id": id_pokemon,
    "name": "third",
    "photo_id": 500
    }

    # изменить покемона

respons_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(respons_change.text)
# выводит результат