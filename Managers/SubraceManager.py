from RaceClass import RaceHandler
from RaceClass import TraitHandler
from RaceClass import SubRaceHandler
from RaceClass import LanguageHandler
from RaceClass import ProficienciesHandler
from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime

class Subrace:
    @staticmethod
    def Subrace(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/subraces/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Trait Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Parent Race - $Race {value}', value= value['race']['name'], inline=False)
            embed.add_field(name='Description', value= value['desc'], inline=False)
            embed.add_field(name='Starter Proficiencies - $Proficiencies {value}', value= RaceHandler.proficienciesHandler(value['starting_proficiencies']), inline=False)
            embed.add_field(name='Ability Bonuses - $AbilityScore {value}', value= SubRaceHandler.abilityHandler(value['ability_bonuses']), inline=False)
            embed.add_field(name='Languages - $Languages {value}', value= value['languages'], inline=False)
            embed.add_field(name='Traits - $Trait {value}', value= SubRaceHandler.traitHandler(value['racial_traits']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed