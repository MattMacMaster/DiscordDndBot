from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime
from Parser import RaceHandler
from Parser import TraitHandler
from Parser import SubRaceHandler
from Parser import LanguageHandler
from Parser import ProficienciesHandler


class TraitManager:

    @staticmethod
    def Traits(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/traits/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Subrace Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Name', value= value['name'], inline=False)
            embed.add_field(name='Description', value= value['desc'][0], inline=False)
            embed.add_field(name='Races - $Race {value}', value= TraitHandler.raceHandler(value['races']), inline=False)
            embed.add_field(name='Subraces - $Subrace {value}', value= RaceHandler.SubHandler(value['subraces']), inline=False)
            embed.add_field(name='Proficiencies', value= SubRaceHandler.proficienciesHandler(value['proficiencies']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed