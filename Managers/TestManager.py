import discord
from datetime import datetime
from Parser import RaceHandler
import math
import requests
from Parser import GeneralHandler
from Managers.CommManager import CommsManager
import json


class Tester:

    @staticmethod
    def Test_Func(embed, description, name):
        text_length = 1024
        json_length = len(description)
        # Total needed embeds to fit the text
        total_embeds = math.ceil(json_length / text_length)

        if(json_length >= text_length):
            counter = 0
            # Need to account for one embed, many, and the last
            while total_embeds > counter:

                if(counter == 0):
                    embed.add_field(
                        name='Description', value=description[0:text_length*(counter+1)],
                        inline=False
                    )

                    counter = counter + 1
                else:
                    embed.add_field(
                        name='Cont..', value=description[text_length*counter:text_length*(counter+1)],
                        inline=False
                    )
                    counter = counter + 1
            return embed
        else:
            embed.add_field(
                name='Testing', value=description
            )
            return embed

    @staticmethod
    def Desc_FuncTest(name):
        name = CommsManager.paramHandler(name)
        value = requests.get(
            'https://www.dnd5eapi.co/api/features/')

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
