from Managers.CommManager import CommsManager
import discord
import requests
from Parser import RaceHandler
from Parser import SpellsHandler
from Parser import GeneralHandler
import json
from datetime import datetime


class SpellsManager:
    @staticmethod
    def GeneralSpell(name):
        name = CommsManager.paramHandler(name)

        value = requests.get(
            'https://www.dnd5eapi.co/api/spells/{}'.format(name))
        value = json.loads(value.text)
        print(value)

        if('error' not in value):
            embed = discord.Embed(
                title='Spell Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Level - $Spell/Level {value}', value=value['level'], inline=False)
            embed.add_field(name='Name', value=value['name'], inline=False)
            embed = GeneralHandler.Desc_Handler(embed, RaceHandler.DescHandler(
                value['desc']), name)
            if('higher_level' in value):
                embed.add_field(name='Increased Level', value=RaceHandler.DescHandler(
                    value['higher_level']), inline=False)
            if('damage' in value):
                embed.add_field(name='Damage', value=SpellsHandler.damageHandler(
                    value['damage']['damage_at_slot_level']), inline=False)
                embed.add_field(
                    name='Damage Type', value=value['damage']['damage_type']['name'], inline=False)
            embed.add_field(name='Range', value=value['range'], inline=False)
            embed.add_field(name='Components',
                            value=value['components'], inline=False)
            if('material' in value):
                embed.add_field(name='Material',
                                value=value['material'], inline=False)
            embed.add_field(
                name='Ritual?', value=value['ritual'], inline=False)
            embed.add_field(name='Duration',
                            value=value['duration'], inline=False)
            embed.add_field(name='Concentration',
                            value=value['concentration'], inline=False)
            embed.add_field(name='Casting Time',
                            value=value['casting_time'], inline=False)
            embed.add_field(
                name='School - $Spell/School {value}', value=value['school']['name'], inline=False)
            embed.add_field(
                name='Classes - $Class {value}', value=SpellsHandler.spellHandler(value['classes']), inline=False)
            embed.add_field(name='Subclasses', value=SpellsHandler.spellHandler(
                value['subclasses']), inline=False)

            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def School(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/spells?school={}'.format(name))
        value = eval(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title='{} School '.format(name) + '- $Spell {value}',
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Spells - $Spell {value}', value=RaceHandler.traitHandler(value['results']))
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def Level(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/spells?level={}'.format(name))
        value = eval(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title='{} Level Spells '.format(name) + '- $Spell {value}',
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Spells - $Spell {value}', value=RaceHandler.traitHandler(value['results']))
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def IndexSpell(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/spells/')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)
        # CommsManager.jsonHandler(value)
        # Actual Call of discord
        if('error' not in value):
            embed = discord.Embed(
                title='Spells - {}'.format(name),
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

    # Skipping Level and school will route to earlier made school
