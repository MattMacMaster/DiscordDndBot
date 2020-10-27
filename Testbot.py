# bot.py
import os
import random
import ResponseManager
import discord
from discord.ext import commands
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
    embed = discord.Embed(
        title = 'Help',
        description = ResponseManager.Response.help(),
        colour = discord.Colour.red()
    )
    embed.add_field(name='Classes', value='test', inline=True)
    await ctx.send(embed=embed)

           
client.run(TOKEN)