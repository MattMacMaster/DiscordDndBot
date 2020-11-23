from RaceClass import RaceHandler
from RaceClass import TraitHandler
from RaceClass import SubRaceHandler
from RaceClass import LanguageHandler
from RaceClass import ProficienciesHandler
from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime

class ProfManager:


    @staticmethod
    def Proficiencies(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/proficiencies/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Proficiencies Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Name', value= value['name'], inline=False)
            embed.add_field(name='Type', value= value['type'], inline=False)
            embed.add_field(name='Classes - $Class {value}', value= ProficienciesHandler.classHandler(value['classes']), inline=False)
            embed.add_field(name='Races - $Race {value}', value= TraitHandler.raceHandler(value['races']), inline=False)


            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed