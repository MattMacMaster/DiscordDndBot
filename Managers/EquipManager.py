from Parser import RaceHandler
from Parser import TraitHandler
from Parser import SubRaceHandler
from Parser import LanguageHandler
from Parser import ProficienciesHandler
from Parser import start_equip
from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime
import json

"""
For some reason this is empty
"""


class EquipManager:
    @staticmethod
    def Equipment(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/equipment/{}'.format(name))
        value = json.loads(value.text)
        embed = discord.Embed(
        title = 'Equipment Information - {}'.format(name),
        colour = discord.Colour.red()
        )
        if('error' in value):
            embed = CommsManager.failedRequest(name)
        else:
            if(value['equipment_category']['name'] == 'Weapon'):
                embed.add_field(name='Equipment Category', value= value['equipment_category']['name'], inline=False)
                embed.add_field(name='Weapon Category', value= value['weapon_category'], inline=False)
                embed.add_field(name='Range', value= start_equip.rangeHandler(value['range']), inline=False)
                embed.add_field(name='Category', value= value['equipment_category']['name'], inline=False)
                embed.add_field(name='Cost', value= str(value['cost']['unit']) + ': ' + str(value['cost']['quantity']), inline=False)
                embed.add_field(name='Damage', value= start_equip.damageHandler(value['damage']), inline=False)
            if(value['equipment_category']['name'] == 'Armor'):
                embed.add_field(name='Equipment Category', value= value['equipment_category']['name'], inline=False)
                embed.add_field(name='Armor Category', value= value['armor_category'], inline=False)
                embed.add_field(name='Armor Class', value= start_equip.acHandler(value['armor_class']), inline=False)
                embed.add_field(name='Strength Requirement', value= value['str_minimum'], inline=False)
                embed.add_field(name='Stealth Disadvantage?', value= value['stealth_disadvantage'], inline=False)
                embed.add_field(name='cost', value= str(value['cost']['unit']) + ':' + str(value['cost']['quantity']), inline=False)
            if(value['equipment_category']['name'] == 'Adventuring Gear'):
                embed.add_field(name='Equipment Category', value= value['equipment_category']['name'], inline=False)
                embed.add_field(name='Gear Category', value= value['gear_category']['name'], inline=False)
                embed.add_field(name='Cost', value= str(value['cost']['unit']) + ': ' + str(value['cost']['quantity']), inline=False)
            if('contents' in value):
                embed.add_field(name='Contents', value= start_equip.contentHandler(value['contents']), inline=False)
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text='MattMaster Bots: Dnd')
        return embed



    @staticmethod
    def MagicItem(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/magic-items/{}'.format(name))
        value = eval(value.text)
        print(value)
        embed = discord.Embed(
        title = 'Magic Item Information - {}'.format(name),
        colour = discord.Colour.red()
        )
        if('error' in value):
            embed = CommsManager.failedRequest(name)
        else:
            if(value['equipment_category']['name'] == 'Weapon'):
                embed.add_field(name='Equipment Category', value= value['equipment_category']['name'], inline=False)
                embed.add_field(name='Weapon Category', value= value['weapon_category'], inline=False)
                embed.add_field(name='Range', value= start_equip.rangeHandler(value['range']), inline=False)
                embed.add_field(name='Category', value= value['equipment_category']['name'], inline=False)
                embed.add_field(name='Cost', value= str(value['cost']['unit']) + ': ' + str(value['cost']['quantity']), inline=False)
                embed.add_field(name='Damage', value= start_equip.damageHandler(value['damage']), inline=False)
            if(value['equipment_category']['name'] == 'Wondrous Item'):
                embed.add_field(name='Type', value= value['equipment_category']['name'], inline=False)
                if(len(RaceHandler.DescHandler(value['desc']))  >= 1024):
                    embed.add_field(name='Desc', value= RaceHandler.DescHandler(value['desc'])[1:1024], inline=False)
                    embed.add_field(name='Cont..', value= RaceHandler.DescHandler(value['desc'])[1024:], inline=False)
                else:
                    embed.add_field(name='Desc', value= RaceHandler.DescHandler(value['desc']), inline=False)
            if(value['equipment_category']['name'] == 'Armor'):
                embed.add_field(name='Equipment Category', value= value['equipment_category']['name'], inline=False)
                embed.add_field(name='Equipment Category', value= RaceHandler.DescHandler(value['equipment_category']['desc']), inline=False)
            if(value['equipment_category']['name'] == 'Adventuring Gear'):
                embed.add_field(name='Equipment Category', value= value['equipment_category']['name'], inline=False)
                embed.add_field(name='Gear Category', value= value['gear_category']['name'], inline=False)
                embed.add_field(name='Cost', value= str(value['cost']['unit']) + ': ' + str(value['cost']['quantity']), inline=False)
            if('contents' in value):
                embed.add_field(name='Contents', value= start_equip.contentHandler(value['contents']), inline=False)

        return embed