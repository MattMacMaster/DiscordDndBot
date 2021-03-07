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


class AbilityScoreManager:
    @staticmethod
    def AbilityScores(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/ability-scores/{}'.format(name))
        value = eval(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title='Ability Score Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
            # value['starting_proficiencies']
            embed.add_field(name='Short Name',
                            value=value['name'], inline=False)
            embed.add_field(name='Full Name',
                            value=value['full_name'], inline=False)
            embed.add_field(name='Description', value=RaceHandler.DescHandler(
                value['desc']), inline=False)
            embed.add_field(
                name='Skills - $Skill {value}', value=RaceHandler.SkillHandler(value['skills']), inline=False)

            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def AbilityScoresIndex(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/ability-scores/')
        value = eval(value.text)
        print(value)
        if('error' not in value):
            embed = discord.Embed(
                title='Ability Score Index ',
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
