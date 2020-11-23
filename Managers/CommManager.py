#This file is primarily for formatting and handling all further communication with either
#My server or the 5e API
import requests
import discord
from datetime import datetime



class CommsManager():
    def __init__(self):
        print("Initializing Comms Manager")

    #r =requests.get('https://www.dnd5eapi.co/api/ability-scores/cha')   
    #print(r.text)
    @staticmethod
    def paramHandler(arg):
        print(arg)
        value = ''.join(arg)
        value = value.replace('\'', "")
        print(value)
        value = value.lower()
        print(value)
        value = value.replace(' ','-')
        print(value)
        return value

    @staticmethod
    def failedRequest(arg):
        embed = discord.Embed(
           title = '{} - Failed to call'.format(arg),
           description = 'Something went horribly wrong',
           colour = discord.Colour.red()
           )
        return embed


    @staticmethod
    def GeneralSpell(name):
        name =  CommsManager.paramHandler(name)
        print(name)

        value = requests.get('https://www.dnd5eapi.co/api/spells/{}'.format(name))