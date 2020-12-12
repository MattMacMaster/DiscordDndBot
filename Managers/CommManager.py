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
        if(type(arg) is tuple):
            print('tuple')
            value = ' '.join(arg)
            value = value.replace('\'', "")
            value = value.lower()
            value = value.replace(' ','-')
            return value
        else:
            print('nah')
            value = ''.join(arg)
            value = value.replace('\'', "")
            value = value.lower()
            value = value.replace(' ','-')
            return value

    @staticmethod
    def failedRequest(arg):
        embed = discord.Embed(
           title = '{} - Failed to call'.format(arg),
           description = 'Something went horribly wrong',
           colour = discord.Colour.red()
           )
        return embed


