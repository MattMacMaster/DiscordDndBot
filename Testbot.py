# bot.py
import os
import random
import ResponseManager
import discord
from discord.ext import commands
import requests
import json
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = commands.Bot(command_prefix='$')
client.remove_command('help')

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
    r =requests.get('https://www.dnd5eapi.co/api/ability-scores/cha')   
    print(r.text)

    embed = discord.Embed(
        title = 'Help - $help',
        description = ResponseManager.Response.help(),
        colour = discord.Colour.red()
    )
    embed.add_field(name='Character Info', value="$Character_info/help", inline=True)
    embed.add_field(name='Classes', value='$Classes/help', inline=True)
    embed.add_field(name='Races', value='$Races/help', inline=True)
    embed.add_field(name='Equipment', value='$Equipment/help', inline=True)
    embed.add_field(name='Spells', value='$Spells/help', inline=True)
    embed.add_field(name='Monsters', value='$Monsters/help', inline=True)
    embed.add_field(name='Mechanics', value='$Mechanics/help', inline=True)
    embed.add_field(name='Rules', value='$Rules/help', inline=True)
    embed.add_field(name='Homebrews', value='$Homebrews/help', inline=True)

    await ctx.send(embed=embed)


@client.command(name='Character_info/help')
async def Character_info_help(ctx):
    embed = discord.Embed(
        title = 'Character Info Help',
        description = ResponseManager.Response.character_def_help(),
        colour = discord.Colour.red()
    )
    embed.add_field(name='Ability Scores', value=str(ResponseManager.Response.Character_Data["Ability Scores"]), inline=True)
    embed.add_field(name='Skills', value=ResponseManager.Response.Character_Data["Skills"], inline=True)
    embed.add_field(name='Proficiencies', value=ResponseManager.Response.Character_Data["Proficiencies"], inline=True)
    embed.add_field(name='Languages', value=ResponseManager.Response.Character_Data["Languages"], inline=True)
    await ctx.send(embed=embed)

           
client.run(TOKEN)