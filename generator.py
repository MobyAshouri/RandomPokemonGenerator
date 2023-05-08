import requests
import random
import customtkinter
from PIL import Image
import re
from io import BytesIO

def generateRandomPokemon():
    try:
        value = random.randint(1, 1015)
        response = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(value)+"/")
        pokemon = response.json()["species"]["name"]
        return pokemon
    except:
        return "something went wrong"

def generatePokedexEntry(pokemonName):
    try:
        response = requests.get("https://pokeapi.co/api/v2/pokemon-species/"+str(pokemonName)+"/")
        data = response.json()["flavor_text_entries"]

        pokedexEntry = ""

        for entry in data:
            if entry["language"]["name"] == "en":
                pokedexEntry = entry["flavor_text"]
                break
        
        pokedexEntry = re.sub(r"[^A-Za-z.é',0-9]", " ", pokedexEntry)

        return pokedexEntry
    except:
        return "something went wrong"
    
def generatePokemonFrontSprite(pokemonName):
    try:
        response = requests.get("https://pokeapi.co/api/v2/pokemon/"+str(pokemonName)+"/")
        url = response.json()["sprites"]["front_default"]

        imageFromURL = requests.get(url)
        image = Image.open(BytesIO(imageFromURL.content))

        image = customtkinter.CTkImage(image, size=(300,300))

        return image
        
    except:
        return "something went wrong"
