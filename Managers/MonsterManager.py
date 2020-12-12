
from Parser import RaceHandler
from Parser import TraitHandler
from Parser import SubRaceHandler
from Parser import LanguageHandler
from Parser import ProficienciesHandler
from Parser import monster
from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime
import json


class MonsterManager:

    @staticmethod
    def GeneralMonster(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/monsters/{}'.format(name))
        value = json.loads(value.text)
        if('error' not in value):
            embed = discord.Embed(
           title = 'Monster Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            embed.add_field(name='Name', value= value['name'], inline=False)
            embed.add_field(name='Size', value= value['size'], inline=False)

            embed.add_field(name='Type', value= value['type'], inline=False)
            embed.add_field(name='Subtype', value= value['subtype'], inline=False)
            embed.add_field(name='Alignment', value= value['alignment'], inline=False)
            embed.add_field(name='AC', value= value['armor_class'], inline=False)
            embed.add_field(name='HP', value= value['hit_points'], inline=False)
            embed.add_field(name='Hit Die', value= value['hit_dice'], inline=False)
            embed.add_field(name='Speed', value= monster.moveHandler(value['speed']), inline=False)
            embed.add_field(name='Ability Scores', value= 'STR: ' + str(value['strength']) + ', DEX: ' + str(value['dexterity']) + ', CON: ' + str(value['constitution']) + ', INT: ' + str(value['intelligence']) + ', WIS: ' + str(value['wisdom']) + ', CHA: ' + str(value['charisma']), inline=False)
            embed.add_field(name='Proficiencies', value= monster.profHandler(value['proficiencies']), inline=False)
            embed.add_field(name='DMG Vulnerabilities', value= value['damage_vulnerabilities'], inline=False)
            embed.add_field(name='DMG Resistances', value= value['damage_resistances'], inline=False)
            embed.add_field(name='DMG Immunities', value= value['damage_immunities'], inline=False)
            embed.add_field(name='Condition Immunities', value= value['condition_immunities'], inline=False)
            embed.add_field(name='Senses', value= monster.sensesHandler(value['senses']), inline=False)
            embed.add_field(name='Languages', value= value['languages'], inline=False)
            embed.add_field(name='CR', value= value['challenge_rating'], inline=False)
            embed.add_field(name='Special Abilites', value= monster.specialHandler(value['special_abilities']), inline=False)
            embed.add_field(name='Actions', value= monster.attackHandler(value['actions']), inline=False)
            if('legendary_actions' in value):
                embed.add_field(name='Legendary Actions', value= monster.specialHandler(value['legendary_actions']), inline=False)



            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed



    @staticmethod
    def MonsterCR(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api//monsters?challenge_rating={}'.format(name))
        value = eval(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title = 'Monsters by CR List - CR {}'.format(name),
                colour = discord.Colour.red()
            )
            embed.add_field(name='Monsters', value= RaceHandler.proficienciesHandler(value['results']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)

        return embed