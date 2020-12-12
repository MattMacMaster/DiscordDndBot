
import requests
import discord
from datetime import datetime
from Managers.CommManager import CommsManager
from Parser import RaceHandler
from Parser import ProficienciesHandler
from Parser import SpellsHandler
from Parser import start_equip


class FeatureManager:
    @staticmethod
    def GeneralFeature(name):
        name = CommsManager.paramHandler(name)

        value = requests.get('https://www.dnd5eapi.co/api/features/{}'.format(name))
        value = eval(value.text)

        embed = discord.Embed(
           title = 'Feature Information - {}'.format(name),
           colour = discord.Colour.red()
        )
        if('error' not in value):
            embed.add_field(name='Name', value=value['name'], inline=False)
            embed.add_field(name='Class', value=value['class']['name'], inline=False)
            embed.add_field(name='Level', value=str(value['level']), inline=False)
            embed.add_field(name='Prerequisites', value=value['prerequisites'], inline=False)
            embed.add_field(name='Description', value= RaceHandler.DescHandler(value['desc']), inline=False)
        else:
            embed = CommsManager.failedRequest(name)    
        embed.timestamp = datetime.utcnow()
        embed.set_footer(text='MattMaster Bots: Dnd')

        return embed