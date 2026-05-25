import requests

base = "https://pokeapi.co/api/v2/"
def get_pokeman(info):
    url = f"{base}/pokemon/{info}"
    response = requests.get(url)
    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrive data {response.status_code}")
pokemon_name = "pikachu"
pokemon_info = get_pokeman(pokemon_name)

if pokemon_info:
    print(f"name: {pokemon_info["name"].capitalize()}")
    print(f"id : {pokemon_info["id"]}")
    print(f"height : {pokemon_info["height"]}")
    print(f"weight : {pokemon_info["weight"]}")