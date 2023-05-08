from PIL import Image
import customtkinter as ctk
import tkinter as tk
from tkinter import PhotoImage
import generator
import webbrowser

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

window = ctk.CTk()
window.geometry("500x600")
window.resizable(False, False)
window.title("Random Pokemon Generator")
window.iconbitmap("assets/images/icon.ico")     # https://www.flaticon.com/free-icons/pokeball "pokeball icons" Pokeball icons created by Darius Dan - Flaticon

rpgFrame = ctk.CTkFrame(window)

headerFont = ctk.CTkFont("FOT-RodinNTLG Pro EB", size=40)
bodyFont = ctk.CTkFont("Arial Bold", size=13)

pokeName = ctk.CTkLabel(rpgFrame, text="", font=headerFont)
pokeEntry = ctk.CTkLabel(rpgFrame, text="", font=bodyFont, wraplength=300)
pokeImage = ctk.CTkLabel(rpgFrame, text="")

currentPokemonName = ""
currentPokemonEntries = ""

def openGoogle():
    url = "https://www.google.com.tr/search?q={}".format(pokeName._text)
    webbrowser.open_new_tab(url)

def openBulbapedia():
    print(pokeName._text.lower())
    if pokeName._text == "nidoran-m":
        url = "https://bulbapedia.bulbagarden.net/wiki/{}_(Pokémon)".format("Nidoran♂")
    if pokeName._text == "nidoran-f":
        url = "https://bulbapedia.bulbagarden.net/wiki/{}_(Pokémon)".format("Nidoran♀")
    else:
        url = "https://bulbapedia.bulbagarden.net/wiki/{}_(Pokémon)".format(pokeName._text.lower())
        webbrowser.open_new_tab(url)


def updateLabels():

    pokeImage.configure(text="")

    currentPokemonName = generator.generateRandomPokemon()
    currentPokemonEntries = generator.generatePokedexEntry(currentPokemonName)
    currentPokemonImage = generator.generatePokemonFrontSprite(currentPokemonName)

    while currentPokemonEntries == "" or currentPokemonName == "" or currentPokemonImage=="something went wrong":
        currentPokemonName = generator.generateRandomPokemon()
        currentPokemonEntries = generator.generatePokedexEntry(currentPokemonName)
        currentPokemonImage = generator.generatePokemonFrontSprite(currentPokemonName)

    pokeName.configure(text = currentPokemonName.upper())
    pokeName.update()

    pokeImage.configure(image= currentPokemonImage)
    pokeImage.update()
    
    pokeEntry.configure(text= currentPokemonEntries.upper())
    pokeEntry.update()

generateButton = ctk.CTkButton(rpgFrame,
                               width= 300,
                               height= 60,
                               text="GENERATE A POKEMON",
                               font=bodyFont,
                               command=updateLabels)

GoogleButtonImage = Image.open("assets/images/google.png")
GoogleButtonImage = ctk.CTkImage(GoogleButtonImage, size=(30,30))
GoogleButton = ctk.CTkButton(rpgFrame,
                          width=50,
                          height=50,
                          text="",
                          image=GoogleButtonImage,
                          command= openGoogle)

BulbaButtonImage = Image.open("assets/images/bulbapedia.png")
BulbaButtonImage = ctk.CTkImage(BulbaButtonImage, size=(30,30))
BulbaButton = ctk.CTkButton(rpgFrame,
                          width=50,
                          height=50,
                          text="",
                          image=BulbaButtonImage,
                          command= openBulbapedia)

generateButton.grid(row = 1, column = 1, padx=10, pady=10, columnspan=2)
pokeImage.grid(row = 2, column = 1, padx= 50, pady=10, columnspan=2)
pokeName.grid(row = 3, column = 1, columnspan=2)
pokeEntry.grid(row = 4, column = 1, columnspan=2)
GoogleButton.grid(row=1, column=2)
BulbaButton.grid(row=2, column=2)

rpgFrame.grid_columnconfigure(1, weight=1)
rpgFrame.grid(row = 0, column = 0, sticky="nesw")


window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
window.mainloop()