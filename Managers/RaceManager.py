from Parser import RaceHandler
from Parser import TraitHandler
from Parser import SubRaceHandler
from Parser import LanguageHandler
from Parser import ProficienciesHandler
from Managers.CommManager import CommsManager
import discord
import requests
from datetime import datetime



class RaceManager:
    #TODO ADD wikidot races to data base and pull from their in outlier cases of missing Data
    @staticmethod
    def GeneralRace(name):
        """
        This will call for a general race string from the api
        Api Currently available options are
        Dragonborne,Dwarf,Elf,Gnome,Half-Elf,Halfling,Human,Tiefling
        """
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/races/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Race Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )

            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Ability Bonuses - $AbilityScore {value}', value= RaceHandler.abilityHandler(value['ability_bonuses']), inline=False)
            embed.add_field(name='Starter Proficiencies - $Proficiencies {value}', value= RaceHandler.proficienciesHandler(value['starting_proficiencies']), inline=False)
            embed.add_field(name='Speed', value= value['speed'], inline=False)
            embed.add_field(name='Size', value= value['size'], inline=False)
            embed.add_field(name='Size Desc', value= value['size_description'], inline=False)
            embed.add_field(name='Languages - $Languages {value}', value= RaceHandler.languageHandler(value['languages']), inline=False)
            embed.add_field(name='Languages Desc', value= value['language_desc'], inline=False)
            embed.add_field(name='Age', value= value['age'], inline=False)
            embed.add_field(name='Alignment', value= value['alignment'], inline=False)
            embed.add_field(name='Traits - $Trait {value}', value= RaceHandler.traitHandler(value['traits']), inline=False)
            embed.add_field(name='Subraces - $Subrace {value}', value= RaceHandler.SubHandler(value['subraces']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)
        

        return embed


    @staticmethod
    def Subraces(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/races/{}/subraces/'.format(name))
        value = eval(value.text)
        print(value)
        if('results' in value):
            embed = discord.Embed(
           title = '{} Subraces'.format(name) + ' - $Subrace {value}',
           colour = discord.Colour.red()
           )
            embed.add_field(name='Subraces', value=RaceHandler.SubHandler(value['results']))
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def Traits(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/races/{}/traits/'.format(name))
        value = eval(value.text)
        if('results' in value):
            embed = discord.Embed(
           title = '{} Traits '.format(name) + '- $Traits {value}',
           colour = discord.Colour.red()
           )
            embed.add_field(name='Subraces', value=RaceHandler.traitHandler(value['results']))
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed


    @staticmethod
    def Proficiencies(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/races/{}/proficiencies/'.format(name))
        value = eval(value.text)
        if('results' in value):
            embed = discord.Embed(
           title = '{} Proficiencies '.format(name) + '- $Proficiencies {value}',
           colour = discord.Colour.red()
           )
            embed.add_field(name='Proficiencies', value=RaceHandler.proficienciesHandler(value['results']))
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed


   

    

 

    


    


  