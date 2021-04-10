
from Parser import RaceHandler
from Parser import TraitHandler
from Parser import SubRaceHandler
from Parser import LanguageHandler
from Parser import ProficienciesHandler
from Parser import monster
from Parser import GeneralHandler
from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime
import json


class MonsterManager:

    @staticmethod
    def GeneralMonster(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/monsters/{}'.format(name))
        value = json.loads(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title='Monster Information - {}'.format(value['name']),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Name', value=value['name'], inline=False)

            embed.add_field(name='Size', value=value['size'], inline=False)
            embed.add_field(name='Type', value=value['type'], inline=False)
            embed.add_field(
                name='Subtype', value=value['subtype'], inline=False)
            embed.add_field(name='Alignment',
                            value=value['alignment'], inline=False)

            embed.add_field(
                name='AC', value=value['armor_class'], inline=False)
            embed.add_field(name='HP', value=value['hit_points'], inline=False)
            embed.add_field(
                name='Hit Die', value=value['hit_dice'], inline=False)
            embed.add_field(name='Speed', value=monster.moveHandler(
                value['speed']), inline=False)

            embed.add_field(name='Ability Scores - $AbilityScore {name}', value='STR: ' + str(value['strength']) + ', DEX: ' + str(value['dexterity']) + ', CON: ' + str(
                value['constitution']) + ', INT: ' + str(value['intelligence']) + ', WIS: ' + str(value['wisdom']) + ', CHA: ' + str(value['charisma']), inline=False)
            embed.add_field(name='Proficiencies', value=monster.profHandler(
                value['proficiencies']), inline=False)
            embed.add_field(name='DMG Vulnerabilities - $Mechanic/DamageType {value}',
                            value=monster.arrayhandle(value['damage_vulnerabilities']), inline=False)
            embed.add_field(name='DMG Resistances - $Mechanic/DamageType {value}',
                            value=monster.arrayhandle(value['damage_resistances']), inline=False)
            embed.add_field(name='DMG Immunities - $Mechanic/DamageType {value}',
                            value=monster.arrayhandle(value['damage_immunities']), inline=False)

            embed.add_field(name='Condition Immunities - $Mechanic/Condition {name}', value=RaceHandler.proficienciesHandler(
                value['condition_immunities']), inline=False)

            embed.add_field(name='Senses', value=monster.sensesHandler(
                value['senses']), inline=False)

            embed.add_field(name='Languages - $Language {name}',
                            value=GeneralHandler.emptyHandler(value['languages']), inline=False)

            embed.add_field(
                name='CR', value=value['challenge_rating'], inline=False)
            if('special_abilities' in value):
                if(len(monster.specialHandler(
                        value['special_abilities'])) >= 2048):
                    embed.add_field(name='Special Abilites', value=monster.specialHandler(
                        value['special_abilities'])[0:1024], inline=False)
                    embed.add_field(name='Cont..', value=monster.specialHandler(
                        value['special_abilities'])[1024:2048], inline=False)
                    embed.add_field(name='Cont..', value=monster.specialHandler(
                        value['special_abilities'])[2048:], inline=False)
                elif(len(monster.specialHandler(
                        value['special_abilities'])) >= 1024):
                    embed.add_field(name='Actions', value=monster.specialHandler(
                        value['special_abilities'])[0:1024], inline=False)
                    embed.add_field(name='Cont..', value=monster.specialHandler(
                        value['special_abilities'])[1024:], inline=False)
                else:
                    embed.add_field(name='Special Abilites', value=monster.specialHandler(
                        value['special_abilities']), inline=False)

            if(len(monster.attackHandler(value['actions'])) >= 2048):
                embed.add_field(name='Actions', value=monster.attackHandler(
                    value['actions'])[0:1024], inline=False)
                embed.add_field(name='Cont..', value=monster.attackHandler(
                    value['actions'])[1024:2048], inline=False)
                embed.add_field(name='Cont..', value=monster.attackHandler(
                    value['actions'])[2048:], inline=False)
            elif(len(monster.attackHandler(value['actions'])) >= 1024):
                embed.add_field(name='Actions', value=monster.attackHandler(
                    value['actions'])[0:1024], inline=False)
                embed.add_field(name='Cont..', value=monster.attackHandler(
                    value['actions'])[1024:], inline=False)
            else:
                embed.add_field(name='Actions', value=monster.attackHandler(
                    value['actions']), inline=False)
            if('legendary_actions' in value):

                if(len(monster.specialHandler(
                        value['legendary_actions'])) >= 1024):
                    embed.add_field(name='Legendary Actions', value=monster.specialHandler(
                        value['legendary_actions'])[0:1024], inline=False)
                    embed.add_field(name='Cont..', value=monster.specialHandler(
                        value['legendary_actions'])[1024:], inline=False)
                else:
                    embed.add_field(name='Legendary Actions', value=monster.specialHandler(
                        value['legendary_actions']), inline=False)

            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            return embed

        else:
            embed = CommsManager.failedRequest(name)
            return embed

    @ staticmethod
    def MonsterCR(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api//monsters?challenge_rating={}'.format(name))
        value = eval(value.text)
        if('error' not in value):
            embed = discord.Embed(
                title='Monsters by CR List - CR {}'.format(name),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Monsters - $Monster {MonsterName}', value=RaceHandler.proficienciesHandler(value['results']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def IndexMonster(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/monsters/')

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
