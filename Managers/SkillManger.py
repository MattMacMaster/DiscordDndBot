
from Parser import RaceHandler
from Parser import TraitHandler
from Parser import SubRaceHandler
from Parser import LanguageHandler
from Parser import ProficienciesHandler
from Parser import GeneralHandler

from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime


class SkillsManager:

    @staticmethod
    def GeneralSkills(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/skills/{}'.format(name))
        value = eval(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title='Skill Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
            # value['starting_proficiencies']
            embed.add_field(name='Name', value=value['name'], inline=False)
            embed.add_field(name='Description', value=RaceHandler.DescHandler(
                value['desc']), inline=False)
            embed.add_field(
                name='Ability Score - $AbilityScore {value}', value=value['ability_score']['name'], inline=False)

            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def SkillsIndex(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/skills/')
        value = eval(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title='Skill Index ',
                colour=discord.Colour.red()
            )
            embed.add_field(name='Entries Found',
                            value=value['count'], inline=False)

            embed.add_field(
                name='Results', value=GeneralHandler.indexHandler(value['results']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed
