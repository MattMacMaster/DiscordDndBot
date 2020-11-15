#This file will be the central point for all messages from the dnd Bot
#This may include simply strings or api calls if necessary

class Response:

    def __init__(self):
        print("Initializing Response Manager")

    Race_Data = {
        "General": """
        $Race {RaceName}
        """,
        "Specific": """
        $Race/Speed {RaceName},
          $Race/Ability_Bonuses {RaceName},
           $Race/Starting_Proficiencies {RaceName},
            $Race/Languages {RaceName},
             $Race/Traits {RaceName},
              $Race/Sub_Classes {RaceName},
               $Race/SubRaces {RaceName},
                $Race/Age {RaceName},
                 $Race/Size {RaceName},
                  $Race/Alignment {RaceName}
                  """
    }

    Monster_Data = {
        "General": """
        $Monster {MonsterName}
        """,
        "Main": 
        """
        $Monster/Speed {MonsterName},
        $Monster/Type {MonsterName},
        $Monster/Subtype {MonsterName},
        $Monster/Armor_Class {MonsterName},
        $Monster/Hit_Points {MonsterName},
        $Monster/Hit_Dice {MonsterName},
        $Monster/Ability_Scores {MonsterName},
        $Monster/Strength {MonsterName},
        $Monster/Dexterity {MonsterName},
        $Monster/Constitution {MonsterName},
        $Monster/Intelligence	 {MonsterName},
        $Monster/Wisdom {MonsterName},
        $Monster/Charisma {MonsterName},
    
        """,
        "Specific": 
        """ 
        $Monster/Proficiencies {MonsterName},
        $Monster/Size {MonsterName},
        $Monster/Alignment {MonsterName}
        $Monster/Damage_Vulnerabilities {MonsterName},
        $Monster/Damage_Immunities {MonsterName},
        $Monster/Damage_Resistances {MonsterName},
        $Monster/Condition_Immunities {MonsterName},
        $Monster/Senses {MonsterName},
        $Monster/Languages {MonsterName},
        $Monster/Legendary_Actions {MonsterName},
        $Monster/Special_Abilities {MonsterName},
        $Monster/Challenge_Rating {MonsterName},
        """
    }
    Class_Data = {
        "General": """
        $Class {ClassName}
        """,
        "Main": 
        """
        $Class/Hit_Die {ClassName},
        $Class/Proficiencies {ClassName},
        $Class/Spells {ClassName},
        $Class/Class_Levels {ClassName},
        $Class/Proficiency_Choices {ClassName},
        $Class/Saving_Throws {ClassName},
        $Class/Starting_Equipment {ClassName},
        $Class/SubClasses {ClassName},
        """
    }
    Equipment_Data = {
        "General": 
        """
        $Equipment {Name}
        """,


        "Armor": """ 
        $Armor {name},
        $Armor/Equipment_Category {name},
        $Armor/Armor_Category {name},
        $Armor/Armor_Class {name},
        $Armor/Str_Minimum {name},
        $Armor/Stealth_Disadvantage {name},
        $Armor/Weight {name},
        $Armor/Cost {name},
         """,


        "Weapon": 
        """ 
        $Weapon {name},
        $Weapon/Equipment_Category {name},
        $Weapon/Weapon_Category {name},
        $Weapon/Weapon_Range {name},
        $Weapon/Category_Range {name},
        $Weapon/Range {name},
        $Weapon/Cost {name},
        $Weapon/Damage {name},
        $Weapon/Weight {name},
        $Weapon/Properties {name},
        """,
        "Magic Items": 
        """ 
        $Magic_Item {name},
        $Magic_Item/Equipment_Category {name},
        $Magic_Item/Desc {name},
        """,
        "Adventuring Gear": 
        """
        $Adv_Gear {name},
        $Adv_Gear/Equipment_Category {name},
        $Adv_Gear/Gear_Category {name},
        $Adv_Gear/Cost {name},
        $Adv_Gear/Weight {name},
        """,
        "Equipment Packs": 
        """ 
        $Equip_Pack {name},
        $Equip_Pack/Equipment_Category {name},
        $Equip_Pack/Gear_Category {name},
        $Equip_Pack/Cost {name},
        $Equip_Pack/Contents {name},
        """,
        "Weapon Properties": "SOON"
 
    }
    Spell_Data = {
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
         $Spell/Classes {Spellname},
         $Spell/Subclasses {Spellname},
        """
    }
    Mechanic_Data = {
        "General":
        """
        $Mechanics/Conditions {name},
        $Mechanics/Damage_Types {name},
        $Mechanics/Schools {name},
        """
    }
    Rules_Data = {
        "General":
        """
        Soon
        """
    }
    

    #Please god find a better way to format this in the embed tool
    Character_Data = {
        "Ability Scores": """
        Ex: ($Character_info/ability-scores con),
        $Character_info/ability-scores {name},
         $Character_info/ability-scores/skills {name}
        """,
        "Skills":
        """
        Ex: ($Character_info/skills/ Arcana),
        $Character_info/skills {name},
        $Character_info/skills/ability-score {name},
        $Character_info/skills/desc {name},
           """,
        "Proficiencies":
        """
        Ex: ($Character_info/proficiencies medium-armor),
        $Character_info/proficiencies {name},
        $Character_info/proficiencies/classes {name},
        $Character_info/proficiencies/races {name},
           """,
        "Languages":
        """
        Ex: ($Character_info/languanges common),
         $Character_info/languanges {name},
         $Character_info/languanges/type {name} ,
         $Character_info/languanges/speakers {name},
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


