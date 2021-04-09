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
        # TODO Refactor Text wrapping for responses
        # TODO $RuleSec fantasy-historical-pantheons breaks - Length is to long
        # TODO Add Subclass Goodness

        # TODO Add related commands to prompts

        # TODO Error handling/ coverage
        # TODO Spell Check, recommendations

        # TODO Clean up command help sheets and naming conventions, consistancy
        # TODO Command Cooldowns

        # TODO Clean up codebase to be less monolithic
        # TODO Flesh out database and homebrew interaction - Long Term

        # TODO Update Readme for easy setup, most likely without a database - or sqlite setup - Long Term
        # TODO Data base built with two migration scripts, windows and ubuntu - Long Term
        # TODO Test out web scraper for missing data - Long Term
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
            embed.add_field(name='Classes', value='$Class/help', inline=True)
            embed.add_field(name='Races', value='$Race/help', inline=True)
            embed.add_field(name='Equipment',
                            value='$Equipment/help', inline=True)
            embed.add_field(name='Spells', value='$Spell/help', inline=True)
            embed.add_field(name='Monsters',
                            value='$Monster/help', inline=True)
            embed.add_field(name='Mechanic',
                            value='$Mechanic/help', inline=True)
            embed.add_field(name='Rules', value='$Rule/help', inline=True)
            embed.add_field(name='Homebrews', value='Coming Soon', inline=True)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Character_info/help')
        async def character_info_help(ctx):
            embed = discord.Embed(
                title='Character Info Help - $character_info/help',
                description=Response.com_help(self, 'Character Info'),
                colour=discord.Colour.red()
            )
            embed.add_field(name='Ability Scores', value=str(
                Response.character_data["Ability-Scores"]).strip('[]'), inline=False)
            embed.add_field(name='Skills', value=str(
                Response.character_data["Skills"]).strip('[]'), inline=False)
            embed.add_field(name='Proficiencies', value=str(
                Response.character_data["Proficiencies"]).strip('[]'), inline=False)
            embed.add_field(name='Languages', value=str(
                Response.character_data["Languages"]).strip('[]'), inline=False)
            embed.add_field(name='Traits', value=str(
                Response.character_data["Traits"]).strip('[]'), inline=False)
            embed.add_field(name='Features', value=str(
                Response.character_data["Features"]).strip('[]'), inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Race/help')
        async def race_help(ctx):
            embed = discord.Embed(
                title='Race Info Help - $Race/help',
                description=Response.com_help(self, 'Race'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.race_data["General"], inline=False)
            embed.add_field(name='Specific',
                            value=Response.race_data["Specific"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Monster/help')
        async def monster_help(ctx):
            embed = discord.Embed(
                title='Monster Info Help - $Monster/help',
                description=Response.com_help(self, 'Monster'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.monster_data["General"], inline=False)
            embed.add_field(
                name='CR', value=Response.monster_data["Main"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')

            await ctx.send(embed=embed)

        @client.command(name='Class/help')
        async def classes_help(ctx):
            embed = discord.Embed(
                title='Classes Info Help - $Class/help',
                description=Response.com_help(self, 'Class'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.class_data["General"], inline=False)
            embed.add_field(
                name='Class Spell List', value=Response.class_data["Class Spell List"], inline=False)
            embed.add_field(
                name='Class Subclass List', value=Response.class_data["Class Subclass List"], inline=False)
            embed.add_field(
                name='Class Feature List', value=Response.class_data["Class Feature List"], inline=False)
            embed.add_field(
                name='Class Proficiencies List', value=Response.class_data["Class Proficiencies List"], inline=False)
            embed.add_field(
                name='Class Starting Equipment List', value=Response.class_data["Class Starting Equipment List"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Equipment/help')
        async def equipment_help(ctx):
            embed = discord.Embed(
                title='Equipment Info Help - $Equipment/help',
                description=Response.com_help(self, 'Equipment'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.equipment_data["General"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Spell/help')
        async def spell_help(ctx):
            embed = discord.Embed(
                title='Spell Info Help - $Spell/help',
                description=Response.com_help(self, 'Spell'),
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='General', value=Response.spell_data["General"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Rule/help')
        async def rules_help(ctx):
            embed = discord.Embed(
                title='Rules Info Help - $Rules/help',
                description='Rules that are core set only',
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Rules', value=Response.rules_data["Rule"], inline=False)
            embed.add_field(
                name='Rules Section', value=Response.rules_data["Rule-Section"], inline=False)

            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Mechanic/help')
        async def mechanics_help(ctx):
            embed = discord.Embed(
                title='Mechanics Info Help - $Mechanic/help',
                description='This Section Covers Game Mechanics - Conditions, Damage Types, and Schools',
                colour=discord.Colour.red()
            )
            embed.add_field(
                name='Condition', value=Response.mechanic_data["Conditions"], inline=False)
            embed.add_field(
                name='Damage_Type', value=Response.mechanic_data["Damage_Types"], inline=False)
            embed.add_field(
                name='School', value=Response.mechanic_data["Schools"], inline=False)
            embed.timestamp = datetime.utcnow()
            embed.set_footer(text='MattMaster Bots: Dnd')
            await ctx.send(embed=embed)

        @client.command(name='Homebrew/help')
        async def homebrew_help(ctx):
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
        async def main_language(ctx, *arg):
            if(len(arg) == 0):
                embed = LanguageManager.LanguageIndex(name='Index')
            else:
                embed = LanguageManager.Languages(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='AbilityScore')
        async def main_score(ctx, *arg):
            if(len(arg) == 0):
                embed = AbilityScoreManager.AbilityScoresIndex(name=arg)
            else:
                embed = AbilityScoreManager.AbilityScores(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Skill')
        async def main_skill(ctx, *arg):
            if(len(arg) == 0):
                embed = SkillsManager.SkillsIndex(name=arg)
            else:
                embed = SkillsManager.GeneralSkills(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Prof')
        async def main_prof(ctx, *arg):
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
        async def main_monster(ctx, *arg):
            if(len(arg) == 0):
                embed = MonsterManager.IndexMonster(name='Index')
            else:
                embed = MonsterManager.GeneralMonster(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Race')
        async def main_race(ctx, *arg):
            if(len(arg) == 0):
                embed = RaceManager.IndexRaces(name='Index')
            else:
                embed = RaceManager.GeneralRace(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='Subrace')
        async def main_subrace(ctx, *arg):
            if(len(arg) == 0):
                embed = SubraceManger.IndexSubRaces(name='Index')
            else:
                embed = SubraceManger.Subrace(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Trait')
        async def main_trait(ctx, *arg):
            if(len(arg) == 0):
                embed = TraitManager.TraitIndex(name='Index')
            else:
                embed = TraitManager.Traits(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Feature')
        async def main_feature(ctx, *arg):
            if(len(arg) == 0):
                embed = FeatureManager.IndexFeatures1(name='Index')
                embed2 = FeatureManager.IndexFeatures2(name='Index')
                await ctx.send(embed=embed)
                await ctx.send(embed=embed2)
            else:
                embed = FeatureManager.GeneralFeature(name=arg)
                await ctx.send(embed=embed)

        @client.command(name='Spell')
        async def main_spell(ctx, *arg):
            if(len(arg) == 0):
                embed = SpellsManager.IndexSpell(name='Index')
            else:
                embed = SpellsManager.GeneralSpell(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Class')
        async def main_class(ctx, *arg):
            if(len(arg) == 0):
                embed = ClassManager.IndexClasses(name='Index')
            else:
                embed = ClassManager.GeneralClass(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Equip')
        async def main_equip(ctx, *arg):
            if(len(arg) == 0):
                embed = EquipManager.EquipmentIndex(name='Index')

            else:
                embed = EquipManager.Equipment(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='MagicItem')
        async def main_magicItem(ctx, *arg):
            if(len(arg) == 0):
                embed = EquipManager.MagicItemIndex(name='Index')
            else:
                embed = EquipManager.MagicItem(name=' '.join(arg))

            await ctx.send(embed=embed)

        """
        This section will be the general argument call, with their respective sub commands
        First will be race and its sub commands
        """

        @client.command(name='Race/Prof')
        async def race_prof(ctx, *arg):
            if(len(arg) == 0):
                embed = ProfManager.ProficienciesIndex(name='Index')
            else:
                embed = RaceManager.Proficiencies(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Race/Trait')
        async def race_trait(ctx, *arg):
            if(len(arg) == 0):
                embed = TraitManager.TraitIndex(name='Index')
            else:
                embed = RaceManager.Traits(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Race/SubRace')
        async def race_subrace(ctx, *arg):
            if(len(arg) == 0):
                embed = SubraceManger.IndexSubRaces(name='Index')
            else:
                embed = RaceManager.Subraces(name=' '.join(arg))
            await ctx.send(embed=embed)

        """
        Spells Subsiduaries
        """

        @client.command(name='Spell/Level')
        async def spell_level(ctx, arg):
            embed = SpellsManager.Level(name=arg)
            await ctx.send(embed=embed)

        @client.command(name='Spell/School')
        async def spell_school(ctx, *arg):
            if(len(arg) == 0):
                embed = MechanicManager.IndexSchools(name='Index')
            else:
                embed = SpellsManager.School(' '.join(arg))
            await ctx.send(embed=embed)

        """
        Classes Subsiduaries

        """
        @client.command(name='Class/SubClass')
        async def class_sub(ctx, *arg):
            if(len(arg) == 0):
                embed = ClassManager.IndexSubClasses(name='Index')
            else:
                embed = ClassManager.SubClass(' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Class/Spell')
        async def class_spell(ctx, *arg):
            if(len(arg) == 0):
                embed = SpellsManager.IndexSpell(name='Index')
            else:
                embed = ClassManager.ClassSpell(' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Class/Feature')
        async def class_features(ctx, *arg):
            if(len(arg) == 0):
                embed = FeatureManager.IndexFeatures1(name='Index')
                embed2 = FeatureManager.IndexFeatures2(name='Index')
                await ctx.send(embed=embed)
                await ctx.send(embed=embed2)
            else:
                embed = ClassManager.ClassFeat(name=arg)
                await ctx.send(embed=embed)

        @client.command(name='Class/Prof')
        async def class_prof(ctx, *arg):
            if(len(arg) == 0):
                embed = ProfManager.ProficienciesIndex(name='index')
            else:
                embed = ClassManager.ClassProf(name=' '.join(arg))
            await ctx.send(embed=embed)

        @client.command(name='Class/Start-Equip')
        async def class_start_equip(ctx, *arg):
            embed = ClassManager.ClassEquip(name=arg)
            await ctx.send(embed=embed)

        """
        One subset for monsters, filter by CR value
        """
        @client.command(name='Monster/CR')
        async def monster_cr(ctx, *arg):
            embed = MonsterManager.MonsterCR(name=arg)
            await ctx.send(embed=embed)

        """
        Mechanics Subset 
        Condition, school, and damage type
        """
        @client.command(name='Mechanic/Condition')
        async def mech_con(ctx, *arg):
            if(len(arg) == 0):
                embed = MechanicManager.IndexConditions(name='Index')
            else:
                embed = MechanicManager.GeneralCondition(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='Mechanic/DamageType')
        async def mech_type(ctx, *arg):
            if(len(arg) == 0):
                embed = MechanicManager.IndexDamageType(name='Index')
            else:
                embed = MechanicManager.GeneralDamageType(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='Mechanic/School')
        async def mech_school(ctx, *arg):
            if(len(arg) == 0):
                embed = MechanicManager.IndexSchools(name='Index')
            else:
                embed = MechanicManager.GeneralSchool(name=' '.join(arg))

            await ctx.send(embed=embed)

        """
        Rules Subset
        """
        @client.command(name='Rule')
        async def rules(ctx, *arg):
            if(len(arg) == 0):
                embed = RulesHandler.RuleIndex(name='Index')
            else:
                embed = RulesHandler.GeneralRule(name=' '.join(arg))

            await ctx.send(embed=embed)

        @client.command(name='RuleSec')
        async def rules_sec(ctx, *arg):
            if(len(arg) == 0):
                embed = RulesHandler.RuleSecIndex(name='Index')
            else:
                embed = RulesHandler.RuleSec(name=' '.join(arg))

            await ctx.send(embed=embed)

        """
        Test Function - Used to test json 
        """
        @client.command(name='Test')
        async def test_func(ctx, *arg):
            if(len(arg) == 0):
                embed = Tester.Desc_FuncTest(name='Index')
                embed2 = Tester.Desc_FuncTest2(name='Index')

                await ctx.send(embed=embed)
                await ctx.send(embed=embed2)
            else:
                embed = Tester.Desc_FuncTest(name=arg)
                await ctx.send(embed=embed)

        client.run(TOKEN)


if __name__ == "__main__":
    bot = BotMain()
    bot.main()
