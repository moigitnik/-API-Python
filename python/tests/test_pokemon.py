
import requests
import pytest


URL =  'https://api.pokemonbattle.ru/v2'
urlcatch = 'https://api.pokemonbattle.ru/v2/trainers/add_pokeball'
urlgettr = 'https://api.pokemonbattle.ru/v2/trainers/33816'
TOKEN = '752c9db7777a792931eeeec18b23ea24'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = 33816

    
    # тест дз_1

def test_status_code_trainer():
    response_get_tr = requests.get(urlgettr)
    assert response_get_tr.status_code == 200



    # тест дз_2

def test_name_trainer():
    response_get_name_tr = requests.get(urlgettr)
    assert response_get_name_tr.json()[0]['trainer_name'] == "Малой"
 
    
    
    # bad

    # тест дз_3

def test_status_code_trainer_bad():
    response_get_tr = requests.get(urlgettr)
    assert response_get_tr.status_code == 201



    # тест дз_4

def test_name_trainer_bad():
    response_get_name_tr = requests.get(urlgettr)
    assert response_get_name_tr.json()['trainer_name'] == "Mалой"