# This file is primarily for formatting and handling all further communication with either
# My server or the 5e API
import requests
import discord
from datetime import datetime


class CommsManager():
    def __init__(self):
        print("Initializing Comms Manager")

    #r =requests.get('https://www.dnd5eapi.co/api/ability-scores/cha')
    @staticmethod
    def paramHandler(arg):
        if(type(arg) is tuple):
            value = ' '.join(arg)
            value = value.replace('\'', "")
            value = value.lower()
            value = value.replace(' ', '-')
            return value
        else:
            value = ''.join(arg)
            value = value.replace('\'', "")
            value = value.lower()
            value = value.replace(' ', '-')
            value = value.replace('/', '-')
            return value
    # Arg will always be an array or a dictionary

    @staticmethod
    def jsonHandler(arg):
        # Look at json and look into a recursion on json return
        # The purpose of this function is to deal with the monolithic
        # Data Types - String, Number and arrays and objects
        # This needs to iterate through all options and associate keys->to data
        # Recursive to get through all options
        # Prints endpoint types, being NOT arrays and dictionaries

        # Check if args is a list first otherwise assume its a dictionary
        if((type(arg) == type([]))):
            # Can be further arrays or objects, or data types
            for b in arg:
                if(type(b) == type([])):
                    # Iterate through each in case a dictionary exists
                    CommsManager.jsonHandler(b)

                elif(type(b) == type({})):
                    # Keep working way down until a bottom is reached
                    CommsManager.jsonHandler(b)
                else:
                    print(b)
        # Assumed object furthuring
        else:
            for i in arg.keys():
                # Assuming args is an object now, using iteratives as keys
                if(type(arg[i]) == type([])):
                    # Iterate through each in case a dictionary exists
                    CommsManager.jsonHandler(arg[i])

                elif(type(arg[i]) == type({})):
                    # Keep working way down until a bottom is reached
                    CommsManager.jsonHandler(arg[i])
                else:
                    print(arg[i])

    @staticmethod
    def failedRequest(arg):
        embed = discord.Embed(
            title='{} - Failed to call'.format(arg),
            description='Something went horribly wrong',
            colour=discord.Colour.red()
        )
        return embed
