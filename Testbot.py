# bot.py
import os
import random
from ResponseManager import Response
from CommManager import CommsManager
import discord
from discord.ext import commands
import json
from datetime import datetime
from dotenv import load_dotenv


class BotMain:
    def main(self):
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')

        client = commands.Bot(command_prefix='$')
        client.remove_command('help')


        ResponseManager = Response()
        ComManager = CommsManager()

        #TODO Need to have a means to place all these commands and import them in
        #TODO Needs a System to layer the commands out and their sub commands
        #TODO Data base built with two migration scripts
        #TODO Flesh out database and homebrew interaction
        #TODO Error handling
        #TODO Spell Check, recommendations
        #TODO Command Cooldowns

        """
        General Basic greeting commands that may be run on boot, add, etc...
        """

        @client.event
        async def on_ready():
            print('Bot is connected.')

        @client.command()
        async def DnD(ctx):
            embed = discord.Embed(
            title = 'Greetings',
            description = Response.intro(self),
            colour = discord.Colour.red()
            )
            await ctx.send(embed=embed)


        """
        This section is for the varying help commands for all functions of the bot
        References: This section references response managers help lists for all help commands
                    any new commands will need to be added to their respoctive list
        """
        @client.command()
        async def help(ctx):

            embed = discord.Embed(
            title = 'Help - $help',
            description = Response.help(self),
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
            description = Response.com_help(self,'Character Info'),
            colour = discord.Colour.red()
            )
            embed.add_field(name='Ability Scores', value=str(Response.Character_Data["Ability Scores"]).strip('[]'), inline=False)
            embed.add_field(name='Skills', value=str(Response.Character_Data["Skills"]).strip('[]'), inline=False)
            embed.add_field(name='Proficiencies', value=str(Response.Character_Data["Proficiencies"]).strip('[]'), inline=False)
            embed.add_field(name='Languages', value=str(Response.Character_Data["Languages"]).strip('[]'), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)


        @client.command(name='Races/help')
        async def Race_help(ctx):
            embed = discord.Embed(
            title = 'Race Info Help - $Races/help',
            description = Response.com_help(self,'Race'),
            colour = discord.Colour.red()
            )
            embed.add_field(name='General', value=Response.Race_Data["General"], inline=False)
            embed.add_field(name='Specific', value=Response.Race_Data["Specific"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Monsters/help')
        async def Monster_help(ctx):
            embed = discord.Embed(
            title = 'Monster Info Help - $Monsters/help',
            description = Response.com_help(self,'Monster'),
            colour = discord.Colour.red()
            )
            embed.add_field(name='General', value=Response.Monster_Data["General"], inline=False)
            embed.add_field(name='Main', value=Response.Monster_Data["Main"], inline=False)
            embed.add_field(name='Specific', value=Response.Monster_Data["Specific"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Classes/help')
        async def Classes_help(ctx):
            embed = discord.Embed(
            title = 'Classes Info Help - $Classes/help',
            description = Response.com_help(self,'Class'),
            colour = discord.Colour.red()
            )
            embed.add_field(name='General', value=Response.Class_Data["General"], inline=False)
            embed.add_field(name='Main', value=Response.Class_Data["Main"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Equipment/help')
        async def Equipment_help(ctx):
            embed = discord.Embed(
            title = 'Equipment Info Help - $Equipment/help',
            description = Response.com_help(self,'Equipment'),
            colour = discord.Colour.red()
            )
            embed.add_field(name='General', value=Response.Equipment_Data["General"], inline=False)
            embed.add_field(name='Armor', value=Response.Equipment_Data["Armor"], inline=False)
            embed.add_field(name='Weapon', value=Response.Equipment_Data["Weapon"], inline=False)
            embed.add_field(name='Magic Items', value=Response.Equipment_Data["Magic Items"], inline=False)
            embed.add_field(name='Adventuring Gear', value=Response.Equipment_Data["Adventuring Gear"], inline=False)
            embed.add_field(name='Equipment Packs', value=Response.Equipment_Data["Equipment Packs"], inline=False)
            embed.add_field(name='Weapon Properties', value=Response.Equipment_Data["Weapon Properties"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Spell/help')
        async def Spell_help(ctx):
            embed = discord.Embed(
            title = 'Spell Info Help - $Spell/help',
            description = Response.com_help(self,'Spell'),
            colour = discord.Colour.red()
            )
            embed.add_field(name='General', value=Response.Spell_Data["General"], inline=False)
            embed.add_field(name='Main', value=Response.Spell_Data["Main"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Rules/help')
        async def Rules_help(ctx):
            embed = discord.Embed(
            title = 'Rules Info Help - $Rules/help',
            description = Response.com_help(self,'Rule'),
            colour = discord.Colour.red()
            )
            embed.add_field(name='General', value=Response.Rules_Data["General"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Mechanics/help')
        async def Mechanics_help(ctx):
            embed = discord.Embed(
            title = 'Mechanics Info Help - $Mechanics/help',
            description = Response.com_help(self,'Mechanics'),
            colour = discord.Colour.red()
            )
            embed.add_field(name='General', value=Response.Mechanic_Data["General"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Homebrews/help')
        async def Homebrew_help(ctx):
            embed = discord.Embed(
            title = 'Homebrew Info Help - $Homebrews/help',
            description = 'Coming Soon',
            colour = discord.Colour.red()
            )
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)
        """
        This section will be the general argument call, with their respective sub commands
        First will be race
        """

        @client.command(name='Race')
        async def Main_Race(ctx, arg):
            embed = ComManager.GeneralRace(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Subrace')
        async def Main_Subrace(ctx, *arg):
            embed = ComManager.Subrace(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Trait')
        async def Main_Trait(ctx, *arg):
            embed = ComManager.Traits(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Language')
        async def Main_Language(ctx, *arg):
            embed = ComManager.Languages(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='AbilityScore')
        async def Main_Score(ctx, *arg):
            embed = ComManager.AbilityScores(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Skill')
        async def Main_Skill(ctx, *arg):
            embed = ComManager.Skills(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Proficiencies')
        async def Main_Prof(ctx, *arg):
            embed = ComManager.Proficiencies(name=' '.join(arg))
            await ctx.send(embed=embed)

        client.run(TOKEN)

if __name__ == "__main__":
    bot = BotMain()
    bot.main()
    