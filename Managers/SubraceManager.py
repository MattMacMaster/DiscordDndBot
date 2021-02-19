from Parser import RaceHandler
from Parser import TraitHandler
from Parser import SubRaceHandler
from Parser import LanguageHandler
from Parser import ProficienciesHandler
from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime


class SubraceManger:
    @staticmethod
    def Subrace(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/subraces/{}'.format(name))
        value = eval(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title='SubRace Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
            # value['starting_proficiencies']
            embed.add_field(
                name='Parent Race - $Race {value}', value=value['race']['name'], inline=False)
            embed.add_field(name='Description',
                            value=value['desc'], inline=False)
            embed.add_field(name='Starter Proficiencies - $Proficiencies {value}', value=RaceHandler.proficienciesHandler(
                value['starting_proficiencies']), inline=False)
            embed.add_field(name='Ability Bonuses - $AbilityScore {value}', value=SubRaceHandler.abilityHandler(
                value['ability_bonuses']), inline=False)
            embed.add_field(
                name='Languages - $Languages {value}', value=value['languages'], inline=False)
            embed.add_field(name='Traits - $Trait {value}', value=SubRaceHandler.traitHandler(
                value['racial_traits']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed
