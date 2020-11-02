# bot.py
import os
import random
import ResponseManager
import discord
from discord.ext import commands
import requests
import json
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')
client.remove_command('help')

    #r =requests.get('https://www.dnd5eapi.co/api/ability-scores/cha')   
    #print(r.text)

@client.event
async def on_ready():
    print('Bot is connected and working.')

@client.command()
async def DnD(ctx):
    embed = discord.Embed(
        title = 'Greetings',
        description = ResponseManager.Response.intro(),
        colour = discord.Colour.red()
    )
    await ctx.send(embed=embed)

@client.command()
async def help(ctx):

    embed = discord.Embed(
        title = 'Help - $help',
        description = ResponseManager.Response.help(),
        colour = discord.Colour.red()
    )
    embed.add_field(name='Character Info', value="$Character_info/help", inline=True)
    embed.add_field(name='Classes', value='$Classes/help', inline=True)
    embed.add_field(name='Races', value='$Races/help', inline=True)
    embed.add_field(name='Equipment', value='$Equipment/help', inline=True)
    embed.add_field(name='Spells', value='$Spell/help', inline=True)
    embed.add_field(name='Monsters', value='$Monsters/help', inline=True)
    embed.add_field(name='Mechanics', value='$Mechanics/help', inline=True)
    embed.add_field(name='Rules', value='$Rules/help', inline=True)
    embed.add_field(name='Homebrews', value='$Homebrews/help', inline=True)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')

    await ctx.send(embed=embed)


@client.command(name='Character_info/help')
async def Character_info_help(ctx):
    embed = discord.Embed(
        title = 'Character Info Help - $Character_info/help',
        description = ResponseManager.Response.character_def_help('Character Info'),
        colour = discord.Colour.red()
    )
    embed.add_field(name='Ability Scores', value=str(ResponseManager.Response.Character_Data["Ability Scores"]).strip('[]'), inline=False)
    embed.add_field(name='Skills', value=str(ResponseManager.Response.Character_Data["Skills"]).strip('[]'), inline=False)
    embed.add_field(name='Proficiencies', value=str(ResponseManager.Response.Character_Data["Proficiencies"]).strip('[]'), inline=False)
    embed.add_field(name='Languages', value=str(ResponseManager.Response.Character_Data["Languages"]).strip('[]'), inline=False)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')

    await ctx.send(embed=embed)


@client.command(name='Races/help')
async def Race_help(ctx):
    embed = discord.Embed(
        title = 'Race Info Help - $Races/help',
        description = ResponseManager.Response.character_def_help('Race'),
        colour = discord.Colour.red()
    )
    embed.add_field(name='General', value=ResponseManager.Response.Race_Data["General"], inline=False)
    embed.add_field(name='Specific', value=ResponseManager.Response.Race_Data["Specific"], inline=False)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')

    await ctx.send(embed=embed)

@client.command(name='Monsters/help')
async def Monster_help(ctx):
    embed = discord.Embed(
        title = 'Monster Info Help - $Monsters/help',
        description = ResponseManager.Response.character_def_help('Monster'),
        colour = discord.Colour.red()
    )
    embed.add_field(name='General', value=ResponseManager.Response.Monster_Data["General"], inline=False)
    embed.add_field(name='Main', value=ResponseManager.Response.Monster_Data["Main"], inline=False)
    embed.add_field(name='Specific', value=ResponseManager.Response.Monster_Data["Specific"], inline=False)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')

    await ctx.send(embed=embed)

@client.command(name='Classes/help')
async def Monster_help(ctx):
    embed = discord.Embed(
        title = 'Classes Info Help - $Classes/help',
        description = ResponseManager.Response.character_def_help('Class'),
        colour = discord.Colour.red()
    )
    embed.add_field(name='General', value=ResponseManager.Response.Class_Data["General"], inline=False)
    embed.add_field(name='Main', value=ResponseManager.Response.Class_Data["Main"], inline=False)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')
    await ctx.send(embed=embed)

@client.command(name='Equipment/help')
async def Equipment_help(ctx):
    embed = discord.Embed(
        title = 'Equipment Info Help - $Equipment/help',
        description = ResponseManager.Response.character_def_help('Equipment'),
        colour = discord.Colour.red()
    )
    embed.add_field(name='General', value=ResponseManager.Response.Equipment_Data["General"], inline=False)
    embed.add_field(name='Armor', value=ResponseManager.Response.Equipment_Data["Armor"], inline=False)
    embed.add_field(name='Weapon', value=ResponseManager.Response.Equipment_Data["Weapon"], inline=False)
    embed.add_field(name='Magic Items', value=ResponseManager.Response.Equipment_Data["Magic Items"], inline=False)
    embed.add_field(name='Adventuring Gear', value=ResponseManager.Response.Equipment_Data["Adventuring Gear"], inline=False)
    embed.add_field(name='Equipment Packs', value=ResponseManager.Response.Equipment_Data["Equipment Packs"], inline=False)
    embed.add_field(name='Weapon Properties', value=ResponseManager.Response.Equipment_Data["Weapon Properties"], inline=False)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')
    await ctx.send(embed=embed)

@client.command(name='Spell/help')
async def Spell_help(ctx):
    embed = discord.Embed(
        title = 'Spell Info Help - $Spell/help',
        description = ResponseManager.Response.character_def_help('Spell'),
        colour = discord.Colour.red()
    )
    embed.add_field(name='General', value=ResponseManager.Response.Spell_Data["General"], inline=False)
    embed.add_field(name='Main', value=ResponseManager.Response.Spell_Data["Main"], inline=False)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')
    await ctx.send(embed=embed)

@client.command(name='Rules/help')
async def Rules_help(ctx):
    embed = discord.Embed(
        title = 'Rules Info Help - $Rules/help',
        description = ResponseManager.Response.character_def_help('Rule'),
        colour = discord.Colour.red()
    )
    embed.add_field(name='General', value=ResponseManager.Response.Rules_Data["General"], inline=False)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')
    await ctx.send(embed=embed)

@client.command(name='Mechanics/help')
async def Rules_help(ctx):
    embed = discord.Embed(
        title = 'Mechanics Info Help - $Mechanics/help',
        description = ResponseManager.Response.character_def_help('Mechanics'),
        colour = discord.Colour.red()
    )
    embed.add_field(name='General', value=ResponseManager.Response.Mechanic_Data["General"], inline=False)
    embed.timestamp = datetime.utcnow()
    embed.set_footer(text='MattMaster Bots: Dnd')
    await ctx.send(embed=embed)

           
client.run(TOKEN)