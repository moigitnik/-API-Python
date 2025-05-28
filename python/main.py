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
    "name": "Tini",
    "photo_id": 345
}
body_change = {
    "pokemon_id": "327081",
    "name": "flover",
    "photo_id": 411
    }

pokemon_catch = {
    "pokemon_id": "327341"
    }


    # создание покемона
respons_creat = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_creat)   
print(respons_creat.text)                                                                     


       # ловля покемона
to_catch_pokemons = requests.post(url = urlcatch, headers = HEADER, json = pokemon_catch)  
print(to_catch_pokemons.text)
# выводит результат


    # изменить покемона

respons_change = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(respons_change.text)
# выводит результат