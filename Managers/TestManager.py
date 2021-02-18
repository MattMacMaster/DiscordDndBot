import discord
from datetime import datetime
import requests
from Managers.CommManager import CommsManager
import json


class Tester:

    @staticmethod
    def Test_Func(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/monsters/{}'.format(name))
        print(value)
        print('REEEEEEEEEEEEE')

        # Needs to use one or the other sometimes, -annoying
        # value = eval(value.text)
        value = json.loads(value.text)

        CommsManager.jsonHandler(value)
        print(value)
        # Actual Call of discord
        if('error' not in value):
            embed = discord.Embed(
                title='Test Function {}'.format(name),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Testing Json Val - $Test {MonsterName}', value=value['bean'], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
        else:
            embed = CommsManager.failedRequest(name)

        return embed
