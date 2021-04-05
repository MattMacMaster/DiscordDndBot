# bot.py
import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from discord.utils import find
import json
from datetime import datetime
from dotenv import load_dotenv
from Managers.RaceManager import RaceManager
from Managers.TraitManager import TraitManager
from Managers.ResponseManager import Response
from Managers.CommManager import CommsManager
from Managers.ProfManager import ProfManager
from Managers.LanguageManager import LanguageManager
from Managers.Ab_ScoreManager import AbilityScoreManager
from Managers.SkillManger import SkillsManager
from Managers.SubraceManager import SubraceManger
from Managers.SpellManager import SpellsManager
from Managers.EquipManager import EquipManager
from Managers.ClassManager import ClassManager
from Managers.MonsterManager import MonsterManager
from Managers.FeatureManager import FeatureManager
from Managers.TestManager import Tester
from Managers.MechanicManager import MechanicManager
from Managers.RulesManager import RulesHandler


class BotMain:
    def main(self):
        load_dotenv()
        TOKEN = os.getenv('DISCORD_TOKEN')

        client = commands.Bot(command_prefix='$', case_insensitive=True)
        client.remove_command('help')

        # TODO Update Read me, explain how it works - setup, env needs
        # TODO Features Index is not working for some reason
        # TODO Feature options dont all work - fix is show index's

        # TODO Error handling/ coverage
        # TODO Spell Check, recommendations

        # TODO Add a means to show all potions of a command
        # TODO Clean up command help sheets and naming conventions, consistancy
        # TODO Command Cooldowns

        # TODO Clean up codebase to be less monolithic
        # TODO Flesh out database and homebrew interaction

        # TODO Update Readme for easy setup, most likely without a database - or sqlite setup
        # TODO Data base built with two migration scripts, windows and ubuntu
        # TODO Test out web scraper for missing dataw
        # TODO Move to pi for 24/7 activity

        # Notes
        """
        Discord api will most of the time just not throw errors for embed issues
        Usually is a missing key or the length goes past 1024 characters
        """

        """
        General Basic greeting commands that may be run on boot, add, etc...
        """

        @client.event
        async def on_ready():
            print('Bot is connected.')

        @client.command()
        async def DnD(ctx):
            embed = discord.Embed(
                title='Greetings',
                description=Response.intro(self),
                colour=discord.Colour.red()
            )
            await ctx.send(embed=embed)

        @client.event
        async def on_guild_join(guild):
            general = find(lambda x: x.name == 'general',  guild.text_channels)
            if general and general.permissions_for(guild.me).send_messages:
                await general.send(Response.guild_join(guild.name))

        @client.event
        async def on_command_error(ctx, error):
            if isinstance(error, CommandNotFound):
                await ctx.send(embed=CommsManager.failedRequest(error))

        """
        This section is for the varying help commands for all functions of the bot
        References: This section references response managers help lists for all help commands
                    any new commands will need to be added to their respoctive list
        """
        @client.command()
        async def help(ctx):

            embed = discord.Embed(
                title='Help - $help',
                description=Response.help(self),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Character Info',
                            value="$Character_info/help", inline=True)
            embed.add_field(name='Class', value='$Class/help', inline=True)
            embed.add_field(name='Races', value='$Races/help', inline=True)
            embed.add_field(name='Equipment',
                            value='$Equipment/help', inline=True)
            embed.add_field(name='Spells', value='$Spell/help', inline=True)
            embed.add_field(name='Monsters',
                            value='$Monsters/help', inline=True)
            embed.add_field(name='Mechanics',
                            value='$Mechanic/help', inline=True)
            embed.add_field(name='Rules', value='$Rules/help', inline=True)
            embed.add_field(name='Homebrews', value='Coming Soon', inline=True)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Character_info/help')
        async def Character_info_help(ctx):
            embed = discord.Embed(
                title='Character Info Help - $Character_info/help',
                description=Response.com_help(self, 'Character Info'),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Ability Scores', value=str(
                Response.Character_Data["Ability Scores"]).strip('[]'), inline=False)
            embed.add_field(name='Skills', value=str(
                Response.Character_Data["Skills"]).strip('[]'), inline=False)
            embed.add_field(name='Proficiencies', value=str(
                Response.Character_Data["Proficiencies"]).strip('[]'), inline=False)
            embed.add_field(name='Languages', value=str(
                Response.Character_Data["Languages"]).strip('[]'), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Races/help')
        async def Race_help(ctx):
            embed = discord.Embed(
                title='Race Info Help - $Races/help',
                description=Response.com_help(self, 'Race'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.Race_Data["General"], inline=False)
            embed.add_field(name='Specific',
                            value=Response.Race_Data["Specific"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Monsters/help')
        async def Monster_help(ctx):
            embed = discord.Embed(
                title='Monster Info Help - $Monsters/help',
                description=Response.com_help(self, 'Monster'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.Monster_Data["General"], inline=False)
            embed.add_field(
                name='Main', value=Response.Monster_Data["Main"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Class/help')
        async def Classes_help(ctx):
            embed = discord.Embed(
                title='Classes Info Help - $Classes/help',
                description=Response.com_help(self, 'Class'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.Class_Data["General"], inline=False)
            embed.add_field(
                name='Main', value=Response.Class_Data["Main"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Equipment/help')
        async def Equipment_help(ctx):
            embed = discord.Embed(
                title='Equipment Info Help - $Equipment/help',
                description=Response.com_help(self, 'Equipment'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.Equipment_Data["General"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Spell/help')
        async def Spell_help(ctx):
            embed = discord.Embed(
                title='Spell Info Help - $Spell/help',
                description=Response.com_help(self, 'Spell'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.Spell_Data["General"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Rules/help')
        async def Rules_help(ctx):
            embed = discord.Embed(
                title='Rules Info Help - $Rules/help',
                description='Rules that are core set only',
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Rules', value=Response.Rules_Data["Rules"], inline=False)
            embed.add_field(
                name='Rules Section', value=Response.Rules_Data["Rules-Sections"], inline=False)

            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Mechanic/help')
        async def Mechanics_help(ctx):
            embed = discord.Embed(
                title='Mechanics Info Help - $Mechanics/help',
                description='This Section Covers Game Mechanics - Conditions, Damage Types, and Schools',
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Condition', value=Response.Mechanic_Data["Conditions"], inline=False)
            embed.add_field(
                name='Dmg_Type', value=Response.Mechanic_Data["Damage_Types"], inline=False)
            embed.add_field(
                name='School', value=Response.Mechanic_Data["Schools"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Homebrews/help')
        async def Homebrew_help(ctx):
            embed = discord.Embed(
                title='Homebrew Info Help - $Homebrews/help',
                description='Coming Soon',
                colour=discord.Colour.red()
            )
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)
        """
        General Statements
        TODO Update Character data calls to this info, cause its done via this
        """
        @client.command(name='Language')
        async def Main_Language(ctx, *arg):
            if(len(arg) == 0):
                embed = LanguageManager.LanguageIndex(name='Index')
            else:
                embed = LanguageManager.Languages(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='AbilityScore')
        async def Main_Score(ctx, *arg):
            if(len(arg) == 0):
                embed = AbilityScoreManager.AbilityScoresIndex(name=arg)
            else:
                embed = AbilityScoreManager.AbilityScores(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Skill')
        async def Main_Skill(ctx, *arg):
            if(len(arg) == 0):
                embed = SkillsManager.SkillsIndex(name=arg)
            else:
                embed = SkillsManager.GeneralSkills(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Proficiencies')
        async def Main_Prof(ctx, *arg):
            if(len(arg) == 0):
                embed = ProfManager.ProficienciesIndex(name='index')
            else:
                embed = ProfManager.Proficiencies(name=' '.join(arg))
            await ctx.send(embed=embed)
        """
        Classified as Character Data ^
        Still Genereal Statements
        """

        @client.command(name='Monster')
        async def Main_Monster(ctx, *arg):
            embed = MonsterManager.GeneralMonster(name=arg)
            print('completed embeding')
            await ctx.send(embed=embed)

        @client.command(name='Race')
        async def Main_Race(ctx, arg):
            embed = RaceManager.GeneralRace(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Subrace')
        async def Main_Subrace(ctx, *arg):
            embed = SubraceManger.Subrace(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Trait')
        async def Main_Trait(ctx, *arg):
            if(len(arg) == 0):
                embed = TraitManager.TraitIndex(name='Index')
            else:
                embed = TraitManager.Traits(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Feature')
        async def Main_Feature(ctx, *arg):
            embed = FeatureManager.GeneralFeature(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Spell')
        async def Main_Spell(ctx, *arg):
            if(len(arg) == 0):
                embed = SpellsManager.IndexSpell(name='Index')
            else:
                embed = SpellsManager.GeneralSpell(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Class')
        async def Main_Class(ctx, *arg):
            if(len(arg) == 0):
                print('reaeeee')
                embed = ClassManager.IndexClasses(name='Index')
            else:
                print('ran')
                embed = ClassManager.GeneralClass(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Equip')
        async def Main_Equip(ctx, *arg):
            if(len(arg) == 0):
                embed = EquipManager.EquipmentIndex(name='Index')

            else:
                embed = EquipManager.Equipment(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='MagicItem')
        async def Main_MagicItem(ctx, *arg):
            if(len(arg) == 0):
                embed = EquipManager.MagicItemIndex(name='Index')
            else:
                print('ran')
                embed = EquipManager.MagicItem(name=' '.join(arg))

            await ctx.send(embed=embed)

        """
        This section will be the general argument call, with their respective sub commands
        First will be race and its sub commands
        """

        @client.command(name='Race/Proficiencies')
        async def Race_Prof(ctx, arg):
            embed = RaceManager.Proficiencies(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Race/Traits')
        async def Race_Trait(ctx, arg):
            embed = RaceManager.Traits(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Race/SubRaces')
        async def Race_Subrace(ctx, arg):
            embed = RaceManager.Subraces(name=arg)
            await ctx.send(embed=embed)

        """
        Spells Subsiduaries
        """

        @client.command(name='Spell/Level')
        async def Spell_Level(ctx, arg):
            embed = SpellsManager.Level(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Spell/School')
        async def Spell_School(ctx, arg):
            if(len(arg) == 0):
                embed = MechanicManager.IndexSchools(name='Index')
            else:
                embed = SpellsManager.School(' '.join(arg))
            await ctx.send(embed=embed)

        """
        Classes Subsiduaries
        TODO Subclasses gets about all of these
        TODO Finsih features and further

        """
        @client.command(name='Class/SubClasses')
        async def Class_Sub(ctx, *arg):
            if(len(arg) == 0):
                embed = ClassManager.IndexSubClasses(name='Index')
            else:
                embed = ClassManager.SubClass(' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Class/Spells')
        async def Class_Spell(ctx, *arg):
            if(len(arg) == 0):
                embed = SpellsManager.IndexSpell(name='Index')
            else:
                embed = ClassManager.ClassSpell(' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Class/Features')
        async def Class_Features(ctx, *arg):
            embed = ClassManager.ClassFeat(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Class/Prof')
        async def Class_Prof(ctx, *arg):
            embed = ClassManager.ClassProf(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Class/Start-Equip')
        async def Class_Start_Equip(ctx, *arg):
            embed = ClassManager.ClassEquip(name=arg)
            await ctx.send(embed=embed)

        """
        One subset for monsters, filter by CR value
        """
        @client.command(name='Monsters/CR')
        async def Monster_CR(ctx, *arg):
            embed = MonsterManager.MonsterCR(name=arg)
            await ctx.send(embed=embed)

        """
        Mechanics Subset 
        Condition, school, and damage type
        """
        @client.command(name='Mechanic/Condition')
        async def Mech_Con(ctx, *arg):
            if(len(arg) == 0):
                embed = MechanicManager.IndexConditions(name='Index')
            else:
                embed = MechanicManager.GeneralCondition(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='Mechanic/Damage_Type')
        async def Mech_Type(ctx, *arg):
            if(len(arg) == 0):
                embed = MechanicManager.IndexDamageType(name='Index')
            else:
                embed = MechanicManager.GeneralDamageType(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='Mechanic/School')
        async def Mech_School(ctx, *arg):
            if(len(arg) == 0):
                embed = MechanicManager.IndexSchools(name='Index')
            else:
                embed = MechanicManager.GeneralSchool(name=' '.join(arg))

            await ctx.send(embed=embed)

        """
        Rules Subset
        """
        @client.command(name='Rules')
        async def Rules(ctx, *arg):
            if(len(arg) == 0):
                embed = RulesHandler.RuleIndex(name='Index')
            else:
                embed = RulesHandler.GeneralRule(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='Rules_Sec')
        async def Rules_Sec(ctx, *arg):
            if(len(arg) == 0):
                embed = RulesHandler.RuleSecIndex(name='Index')
            else:
                embed = RulesHandler.RuleSec(name=' '.join(arg))

            await ctx.send(embed=embed)

        """
        Test Function - Used to test json 
        """
        @client.command(name='Test')
        async def Test_Func(ctx, *arg):
            """
            # This is for trying to get Features index to work - TODO fix it
            if(len(arg) == 0):
                print("This one")
                embed = Tester.Desc_FuncTest(name='Index')
            else:
                embed = Tester.Desc_FuncTest(name=arg)
            for x in embed:
                await ctx.send(embed=x)
            """
            if(len(arg) == 0):
                embed = Tester.Desc_FuncTest(name='Index')
            else:
                embed = Tester.Desc_FuncTest(name=arg)
            await ctx.send(embed=embed)

        """
        General Error Handle
        """
        @Class_Start_Equip.error
        async def info_error(ctx, error):
            await ctx.send('Something went horribly wrong: {}'.format(error))

        client.run(TOKEN)


if __name__ == "__main__":
    bot = BotMain()
    bot.main()