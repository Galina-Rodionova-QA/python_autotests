import requests
import pytest

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'de150e9ac36a811a753d113c28019b40'
HEADER =  {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '3649'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params =  {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params =  {'trainer_id' : TRAINER_ID})
    assert response_get.json()['data'][0]['name'] == 'Бульбазавр'


