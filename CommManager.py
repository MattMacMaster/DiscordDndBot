#This file is primarily for formatting and handling all further communication with either
#My server or the 5e API
import requests
import discord
from datetime import datetime
from RaceClass import RaceHandler
from RaceClass import TraitHandler
from RaceClass import SubRaceHandler
from RaceClass import LanguageHandler
from RaceClass import ProficienciesHandler



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
            embed.add_field(name='Traits - $Trait {value}', value= RaceHandler.traitHandler(value['traits']), inline=False)
            embed.add_field(name='Subraces - $Subrace {value}', value= RaceHandler.SubHandler(value['subraces']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)
        

        return embed


    @staticmethod
    def Subrace(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/subraces/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Trait Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Parent Race - $Race {value}', value= value['race']['name'], inline=False)
            embed.add_field(name='Description', value= value['desc'], inline=False)
            embed.add_field(name='Starter Proficiencies - $Proficiencies {value}', value= RaceHandler.proficienciesHandler(value['starting_proficiencies']), inline=False)
            embed.add_field(name='Ability Bonuses - $AbilityScore {value}', value= SubRaceHandler.abilityHandler(value['ability_bonuses']), inline=False)
            embed.add_field(name='Languages - $Languages {value}', value= value['languages'], inline=False)
            embed.add_field(name='Traits - $Trait {value}', value= SubRaceHandler.traitHandler(value['racial_traits']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def Traits(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/traits/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Subrace Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Name', value= value['name'], inline=False)
            embed.add_field(name='Description', value= value['desc'][0], inline=False)
            embed.add_field(name='Races - $Race {value}', value= TraitHandler.raceHandler(value['races']), inline=False)
            embed.add_field(name='Subraces - $Subrace {value}', value= RaceHandler.SubHandler(value['subraces']), inline=False)
            embed.add_field(name='Proficiencies', value= SubRaceHandler.proficienciesHandler(value['proficiencies']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def Languages(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/languages/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Language Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Name', value= value['name'], inline=False)
            embed.add_field(name='Type', value= value['type'], inline=False)
            embed.add_field(name='typical_speakers - $Race {value}', value= LanguageHandler.raceHandler(value['typical_speakers']), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed

    @staticmethod
    def AbilityScores(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/ability-scores/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Ability Score Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Short Name', value= value['name'], inline=False)
            embed.add_field(name='Full Name', value= value['full_name'], inline=False)
            embed.add_field(name='Description', value= RaceHandler.DescHandler(value['desc']), inline=False)
            embed.add_field(name='Skills - $Skill {value}', value= RaceHandler.SkillHandler(value['skills']), inline=False)


            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed


    @staticmethod
    def Skills(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/skills/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Skill Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Name', value= value['name'], inline=False)
            embed.add_field(name='Description', value= RaceHandler.DescHandler(value['desc']), inline=False)
            embed.add_field(name='Ability Score - $AbilityScore {value}', value= value['ability_score']['name'], inline=False)


            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed


    @staticmethod
    def Proficiencies(name):
        name = CommsManager.paramHandler(name)
        value = requests.get('https://www.dnd5eapi.co/api/proficiencies/{}'.format(name))
        value = eval(value.text)
        if('name' in value):
            embed = discord.Embed(
           title = 'Proficiencies Information - {}'.format(value['name']),
           colour = discord.Colour.red()
           )
            print(value)
            #value['starting_proficiencies']
            embed.add_field(name='Name', value= value['name'], inline=False)
            embed.add_field(name='Type', value= value['type'], inline=False)
            embed.add_field(name='Classes - $Class {value}', value= ProficienciesHandler.classHandler(value['classes']), inline=False)
            embed.add_field(name='Races - $Race {value}', value= TraitHandler.raceHandler(value['races']), inline=False)


            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

        else:
            embed = CommsManager.failedRequest(name)

        return embed


    @staticmethod
    def GeneralSpell(name):
        """
        This will call for a general race string from the api
        Api Currently available options are
        Dragonborne,Dwarf,Elf,Gnome,Half-Elf,Halfling,Human,Tiefling
        """
        name =  CommsManager.paramHandler(name)
        print(name)

        value = requests.get('https://www.dnd5eapi.co/api/spells/{}'.format(name))