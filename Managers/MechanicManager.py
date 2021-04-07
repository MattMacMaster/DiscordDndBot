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
            embed.add_field(name='Name',
                            value=value['name'], inline=False)

            embed = GeneralHandler.Desc_Handler(
                embed, RaceHandler.DescHandler(value['desc']), name)
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
            embed.add_field(name='Name',
                            value=value['name'], inline=False)

            embed = GeneralHandler.Desc_Handler(
                embed, value['desc'], name)
        else:
            embed = CommsManager.failedRequest(name)
        return embed
    # Indexes

    @staticmethod
    def IndexDamageType(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/damage-types/')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)
        # CommsManager.jsonHandler(value)
        # Actual Call of discord
        if('error' not in value):
            embed = discord.Embed(
                title='Dmg Types - {}'.format(name),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Entries Found',
                            value=value['count'], inline=False)
            embed = GeneralHandler.index_Handler2(
                embed, value['results'], name)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def IndexSchools(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/magic-schools/')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)
        # CommsManager.jsonHandler(value)
        # Actual Call of discord
        print(value)
        if('error' not in value):
            embed = discord.Embed(
                title='Magic Schools - {}'.format(name),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Entries Found',
                            value=value['count'], inline=False)
            embed = GeneralHandler.index_Handler2(
                embed, value['results'], name)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def IndexConditions(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/conditions/')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)
        # CommsManager.jsonHandler(value)
        # Actual Call of discord
        if('error' not in value):
            embed = discord.Embed(
                title='Conditions - {}'.format(name),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Entries Found',
                            value=value['count'], inline=False)
            embed = GeneralHandler.index_Handler2(
                embed, value['results'], name)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)

        return embed
