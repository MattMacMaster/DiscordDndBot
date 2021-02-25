from Managers.CommManager import CommsManager
import discord
import requests
from Parser import RaceHandler
from Parser import GeneralHandler

from datetime import datetime
import json


class MechanicManager:
    @staticmethod
    def GeneralCondition(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/conditions/{}'.format(name))
        value = json.loads(value.text)
        print(value)
        if('error' not in value):
            embed = discord.Embed(
                title='Condition Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Name',
                            value=value['name'], inline=False)

            embed = GeneralHandler.Desc_Handler(
                embed, RaceHandler.DescHandler(value['desc']), name)

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def GeneralDamageType(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/damage-types/{}'.format(name))
        value = json.loads(value.text)
        print(value)
        if('error' not in value):
            embed = discord.Embed(
                title='Damage Type Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
        else:
            embed = CommsManager.failedRequest(name)
            return embed

    @staticmethod
    def GeneralSchool(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/magic-schools/{}'.format(name))
        value = json.loads(value.text)
        print(value)
        if('error' not in value):
            embed = discord.Embed(
                title='Magic School Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
        else:
            embed = CommsManager.failedRequest(name)
            return embed
