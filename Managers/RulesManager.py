from Managers.CommManager import CommsManager
import discord
import requests
from Parser import RaceHandler
from Parser import GeneralHandler

from datetime import datetime
import json


class RulesHandler:
    @staticmethod
    def GeneralRule(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/rules/{}'.format(name))
        value = json.loads(value.text)
        print(value)
        if('error' not in value):
            embed = discord.Embed(
                title='Damage Type Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Name',
                            value=value['name'], inline=False)

            embed = GeneralHandler.Desc_Handler(
                embed, value['desc'], name)
        else:
            embed = CommsManager.failedRequest(name)
        return embed

    @staticmethod
    def RuleSec(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/rule-sections/{}'.format(name))
        value = json.loads(value.text)
        print(value)
        if('error' not in value):
            embed = discord.Embed(
                title='Damage Type Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Name',
                            value=value['name'], inline=False)

            embed = GeneralHandler.Desc_Handler(
                embed, value['desc'], name)
        else:
            embed = CommsManager.failedRequest(name)
        return embed
