# This file will be the central point for all messages from the dnd Bot
# This may include simply strings or api calls if necessary

class Response:

    def __init__(self):
        print("Initializing Response Manager")

    race_data = {
        "General": """
        $Race {RaceName}
        """,
        "Specific": """
           $Race/Prof {RaceName},
             $Race/Trait {RaceName},
               $Race/SubRace {RaceName},

               $Subrace {SubRaceName}
                  """
    }

    monster_data = {
        "General": """
        $Monster {MonsterName}
        """,
        "Main":
        """
        $Monster/cr {CR}
        """
    }
    class_data = {
        "General": """
        $Class {ClassName}
        """,
        "Main":
        """
        $Class/Spell {ClassName},
        $Class/SubClass {ClassName},
        $Class/Feature {ClassName},
        $Class/Prof {ClassName},
        $Class/Start-Equip {ClassName},
        """
    }
    equipment_data = {
        "General":
        """
        $Equip {Name},
        $MagicItem {Name},

        """

    }
    spell_data = {
        "General":
        """
        $Spell {Spellname}
        $Spell/School {Schoolname}
        $Spell/Level {Level}
        """,

        "Main":
        """ 
         $Spell/Desc {Spellname},
         $Spell/Range {Spellname},
         $Spell/Higher_Level {Spellname},
         $Spell/Components {Spellname},
         $Spell/Material {Spellname},
         $Spell/Ritual {Spellname},
         $Spell/Duration {Spellname},
         $Spell/Concentration {Spellname},
         $Spell/Cast_Time {Spellname},
         $Spell/Level {Spellname},
         $Spell/Attack_Type {Spellname},
         $Spell/Damage {Spellname},
         $Spell/School {Spellname},
         $Spell/Class {Spellname},
         $Spell/Subclass {Spellname},
        """
    }
    mechanic_data = {
        "Conditions":
        """
        $Mechanic/Condition {name}
        """,
        "Damage_Types":
        """
        $Mechanic/DamageType {name}
        """,
        "Schools":
        """
        $Mechanic/School {name}
        """
    }
    rules_data = {
        "Rule":
        """
        $Rule {name}
        """,
        "Rule-Section":
        """
        $RuleSec {name}
        """
    }

    # Please god find a better way to format this in the embed tool
    character_data = {
        "Ability-Scores": """
        Ex: ($AbilityScore con),
         $AbilityScore {name},
        """,
        "Skills":
        """
        Ex: ($Skill Arcana),
        $Skill {name},
           """,
        "Proficiencies":
        """
        Ex: ($Prof medium-armor),
        $Prof {name},
           """,
        "Languages":
        """
        Ex: ($Language common),
         $Language {name},
        """,
        "Traits":
        """
        Ex: ($Trait tinker),
        $Trait {name},
        """,
        "Features":
        """
        Ex: ($Feature Divine Sense),
        $Feature {name},
        """
    }

    @staticmethod
    def intro(self):
        return """
        Hello,
         I am D&D bot.
          I exist to help with all your D&D needs and questions.
           My currrent knowledge base includes but is not limited to,
           classes, races, equipment, spells, monsters, mechanics and rules.
            I also manage my masters homebrews which I keep incase anyone is ever
             wondering what they are or if master ever forgets them.
              If you think my information is incorrect or outdated please message
               my creater to fix my ways.
               """

    @staticmethod
    def help(self):
        return """Here is are the all the beginning level commands that are currently available,
         follow their respective helpers for more information!"""

    @staticmethod
    def com_help(self, value):
        return 'Here are the currently known commands for {} Information!'.format(value)

    @staticmethod
    def guild_join(value):
        return 'Hello {}! \n I am in version 1.0.0. \n I am officially ready to be usefull but please be nice cause I\'m new here. \n For my command information type $help in your designated bot channel!'.format(value)
