import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '27df80243f2c9f0d72138f2375768fdb'
HEADER = {'Content-type':'application/json', 'trainer_token':TOKEN}
TRAINER_ID = 12469


def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/trainers', params = {'trainer_id' : TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'Saturn'