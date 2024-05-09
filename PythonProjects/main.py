import requests

URL = 'https://api.pokemonbattle.me/v2'
TOKEN = 'de150e9ac36a811a753d113c28019b40'
HEADER =  {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}

body_create = {
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}
body_change = {
    "pokemon_id": "26680",
    "name": "Альберт"
}
body_add_pokeball = {
    "pokemon_id": "26680"
}

response_create = requests.post(url =  f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

message = response_create.json()['message']
print(message)

response_change = requests.patch(url = f'{URL}/pokemons', headers = HEADER, json = body_change)
print(response_change.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)
