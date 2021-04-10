from Managers.CommManager import CommsManager
import discord
import requests
from Parser import RaceHandler
from Parser import GeneralHandler
import math
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

            if('subsections' in value):
                embed.add_field(name='SubSections - $RulesSec {Value}',
                                value=RaceHandler.proficienciesHandler(value['subsections']), inline=False)

        else:
            embed = CommsManager.failedRequest(name)
        return embed

    @staticmethod
    def RuleSec(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/rule-sections/{}'.format(name))
        value = json.loads(value.text)
        length = 5000
        rounds = math.ceil(len(value['desc']) / length)
        counter = 0
        embeds = []
        print(value)
        if('error' not in value):
            while(rounds > counter):

                embed = discord.Embed(
                    title='Damage Type Information - {}'.format(value['name']),
                    colour=discord.Colour.red()
                )
                temp = counter + 1
                embed = GeneralHandler.Desc_Handler(
                    embed, value['desc'][counter*length:temp*length], name)
                embeds.append(embed)
                counter = counter + 1
            return embeds
        else:
            embed = CommsManager.failedRequest(name)
        return [embed]

    @ staticmethod
    def RuleIndex(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/rules/')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)
        # CommsManager.jsonHandler(value)
        # Actual Call of discord
        if('error' not in value):
            embed = discord.Embed(
                title='Rules - {}'.format(name),
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

    @ staticmethod
    def RuleSecIndex(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/rule-sections/')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)
        # CommsManager.jsonHandler(value)
        # Actual Call of discord
        if('error' not in value):
            embed = discord.Embed(
                title='Test - {}'.format(name),
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
