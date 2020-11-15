#This file is primarily for formatting and handling all further communication with either
#My server or the 5e API
import requests
import discord

class CommsManager():
    def __init__(self):
        print("Initializing Comms Manager")

    #r =requests.get('https://www.dnd5eapi.co/api/ability-scores/cha')   
    #print(r.text)
    @staticmethod
    def paramHandler(arg):
        value = ' '.join(arg)
        value = value.lower()
        value = value.replace(' ','-')
        return value

    @staticmethod
    def GeneralRace(name):
        """
        This will call for a general race string from the api
        Api Currently available options are
        Dragonborne,Dwarf,Elf,Gnome,Half-Elf,Halfling,Human,Tiefling
        """
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/races/{}'.format(name))
        #value = requests.get('https://www.dnd5eapi.co/api/traits/hellish-resistance')

    @staticmethod
    def GeneralSpell(name):
        """
        This will call for a general race string from the api
        Api Currently available options are
        Dragonborne,Dwarf,Elf,Gnome,Half-Elf,Halfling,Human,Tiefling
        """
        name =  CommsManager.paramHandler(name)
        print(name)

        value = requests.get('https://www.dnd5eapi.co/api/spells/{}'.format(name))
        print(value)
        print(value.text)