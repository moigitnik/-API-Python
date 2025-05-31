
import requests
import pytest


urlgettr = 'https://api.pokemonbattle.ru/v2/trainers/33816'
    
    # тест дз_1

def test_status_code_trainer():
    response_get_tr = requests.get(urlgettr)
    assert response_get_tr.status_code == 200


    # тест дз_2

def test_name_trainer():
    response_get_name_tr = requests.get(urlgettr)
    assert response_get_name_tr.json()['trainer_name'] == "Малой"
 