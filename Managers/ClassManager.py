
import requests
import discord
from datetime import datetime
from Managers.CommManager import CommsManager
from Parser import RaceHandler
from Parser import ProficienciesHandler
from Parser import SpellsHandler
from Parser import start_equip


class ClassManager:
    @staticmethod
    def GeneralClass(name):
        name = CommsManager.paramHandler(name)

        value = requests.get('https://www.dnd5eapi.co/api/classes/{}'.format(name))
        value = eval(value.text)

        value2 = requests.get('https://www.dnd5eapi.co/api/starting-equipment/{}'.format(name))
        value2 = eval(value2.text)


        if('name' in value):
            embed = discord.Embed(
           title = 'Class Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            embed.add_field(name='Name', value= value['name'], inline=False)
            embed.add_field(name='Hit Die', value= 'd' + str(value['hit_die']), inline=False)
            embed.add_field(name='Proficiency Choices', value= ProficienciesHandler.prof_choices(value['proficiency_choices']), inline=False)
            embed.add_field(name='Proficiencies', value= RaceHandler.proficienciesHandler(value['proficiencies']), inline=False)
            embed.add_field(name='Saving Throws', value=  RaceHandler.proficienciesHandler(value['saving_throws']), inline=False)
            embed.add_field(name='Starting Equipment', value= start_equip.startEquipmentHandler(value2['starting_equipment']), inline=False)
            embed.add_field(name='Starting Equipment Options', value= start_equip.equipmentHandler(value2['starting_equipment_options']), inline=False)
            embed.add_field(name='SpellCasting', value= 'Implemented Later', inline=False)
            if('spellcasting' in value):
                embed.add_field(name='SpellCasting Ability', value= value['spellcasting']['spellcasting_ability']['name'], inline=False)
                embed.add_field(name='SpellCasting Desc', value= SpellsHandler.dcHandler(value['spellcasting']['info']), inline=False)
            embed.add_field(name='Spells', value= '$Classes/{}/Spells'.format(name), inline=False)
            embed.add_field(name='SubClasses', value=RaceHandler.proficienciesHandler(value['subclasses']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed