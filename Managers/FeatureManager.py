
import requests
import discord
from datetime import datetime
from Managers.CommManager import CommsManager
from Parser import RaceHandler
from Parser import ProficienciesHandler
from Parser import SpellsHandler
from Parser import start_equip
from Parser import GeneralHandler
import json


class FeatureManager:
    @staticmethod
    def GeneralFeature(name):
        name = CommsManager.paramHandler(name)

        value = requests.get(
            'https://www.dnd5eapi.co/api/features/{}'.format(name))
        value = eval(value.text)

        embed = discord.Embed(
            title='Feature Information - {}'.format(name),
            colour=discord.Colour.red()
        )
        if('error' not in value):
            embed.add_field(name='Name', value=value['name'], inline=False)
            embed.add_field(
                name='Class - $Class {ClassName}', value=value['class']['name'], inline=False)
            embed.add_field(name='Level - $Spell/Level {Level}', value=str(
                value['level']), inline=False)
            embed.add_field(name='Prerequisites',
                            value=value['prerequisites'], inline=False)
            embed.add_field(name='Description', value=RaceHandler.DescHandler(
                value['desc']), inline=False)
        else:
            embed = CommsManager.failedRequest(name)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text='MattMaster Bots: Dnd')

        return embed

    @staticmethod
    def IndexFeatures1(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/features/')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)
        # Actual Call of discord
        if('error' not in value):
            embed = discord.Embed(
                title='Features - {}'.format(name),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Entries Found',
                            value=value['count'], inline=False)

            embed = GeneralHandler.index_Handler3(
                embed, value['results'][:200], name)

            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)
        return embed

    @staticmethod
    def IndexFeatures2(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/features/')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)
        # Actual Call of discord
        if('error' not in value):
            embed = discord.Embed(
                title='Page 2 - {}'.format(name),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Entries Found',
                            value=value['count'], inline=False)

            embed = GeneralHandler.index_Handler3(
                embed, value['results'][200:], name)

            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)
        return embed
