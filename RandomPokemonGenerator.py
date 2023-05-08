import PIL
import customtkinter as ctk
import tkinter as tk
import generator

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
window = ctk.CTk()
window.geometry("500x600")
window.resizable(False, False)
window.title("Random Pokemon Generator")

rpgFrame = ctk.CTkFrame(window)

headerFont = ctk.CTkFont("FOT-RodinNTLG Pro EB", size=40)
bodyFont = ctk.CTkFont("Arial Bold", size=13)

pokeName = ctk.CTkLabel(rpgFrame, text="", font=headerFont)
pokeEntry = ctk.CTkLabel(rpgFrame, text="", font=bodyFont, wraplength=300)
pokeImage = ctk.CTkLabel(rpgFrame, text="", image=None)

currentPokemonName = ""
currentPokemonEntries = ""

def updateLabels():

    pokeImage.configure(text="")

    currentPokemonName = generator.generateRandomPokemon()
    currentPokemonEntries = generator.generatePokedexEntry(currentPokemonName)
    currentPokemonImage = generator.generatePokemonFrontSprite(currentPokemonName)

    while currentPokemonEntries == "" or currentPokemonName == "":
        currentPokemonName = generator.generateRandomPokemon()
        currentPokemonEntries = generator.generatePokedexEntry(currentPokemonName)

    pokeName.configure(text = currentPokemonName.upper())
    pokeName.update()

    if currentPokemonImage=="something went wrong":
        pokeImage.configure(text="something went wrong", image=None)
    else:
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

generateButton.grid(row = 1, column = 1, padx=10, pady=10, columnspan=3)
pokeImage.grid(row = 2, column = 1, padx= 50, pady=10, columnspan=3)
pokeName.grid(row = 3, column = 1)
pokeEntry.grid(row = 4, column = 1)

rpgFrame.grid_columnconfigure(1, weight=1)
rpgFrame.grid(row = 0, column = 0, sticky="nesw")


window.grid_columnconfigure(0, weight=1)
window.grid_rowconfigure(0, weight=1)
window.mainloop()