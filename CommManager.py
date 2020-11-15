#This file is primarily for formatting and handling all further communication with either
#My server or the 5e API
import requests
import discord
from datetime import datetime
from RaceClass import RaceHandler

class CommsManager():
    def __init__(self):
        print("Initializing Comms Manager")

    #r =requests.get('https://www.dnd5eapi.co/api/ability-scores/cha')   
    #print(r.text)
    @staticmethod
    def paramHandler(arg):
        print(arg)
        value = ''.join(arg)
        print(value)
        value = value.lower()
        print(value)
        value = value.replace(' ','-')
        print(value)
        return value
    #TODO ADD wikidot races to data base and pull from their in outlier cases of missing Data
    @staticmethod
    def GeneralRace(name):
        """
        This will call for a general race string from the api
        Api Currently available options are
        Dragonborne,Dwarf,Elf,Gnome,Half-Elf,Halfling,Human,Tiefling
        """
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/races/{}'.format(name))
        value = eval(value.text)

        embed = discord.Embed(
           title = 'Race Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
           #value['starting_proficiencies']
        embed.add_field(name='Ability Bonuses', value= RaceHandler.abilityHandler(value['ability_bonuses']), inline=False)
        embed.add_field(name='Starter Proficiencies', value= RaceHandler.proficienciesHandler(value['starting_proficiencies']), inline=False)
        embed.add_field(name='Speed', value= value['speed'], inline=False)
        embed.add_field(name='Size', value= value['size'], inline=False)
        embed.add_field(name='Size Desc', value= value['size_description'], inline=False)
        embed.add_field(name='Languages', value= RaceHandler.languageHandler(value['languages']), inline=False)
        embed.add_field(name='Languages Desc', value= value['language_desc'], inline=False)
        embed.add_field(name='Age', value= value['age'], inline=False)
        embed.add_field(name='Traits', value= RaceHandler.traitHandler(value['traits']), inline=False)
        embed.add_field(name='Subraces', value= RaceHandler.SubHandler(value['subraces']), inline=False)
    
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text='MattMaster Bots: Dnd')

        return embed

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