#This file will be the central point for all messages from the dnd Bot
#This may include simply strings or api calls if necessary

class Response:
    ClassList = [
            "$Classes/{ClassName}",
            "$Classes/{ClassName}/Hit_Die",
            "$Classes/{ClassName}/Proficiencies",
            "$Classes/{ClassName}/Proficiency_choices",
            "$Classes/{ClassName}/Saving_Throws",
            "$Classes/{ClassName}/Sub_Classes",    
            "$Classes/{ClassName}/Starting_Equipment",
            "$Classes/{ClassName}/Class_Levels",
            "$Classes/{ClassName}/Spellcasting",
            "$Classes/{ClassName}/Spells",
    ]

    RaceList = [
            "$Race/{RaceName}",
            "$Race/{RaceName}/Speed",
            "$Race/{RaceName}/Ability_Bonuses",
            "$Race/{RaceName}/Starting_Proficiencies",
            "$Race/{RaceName}/Languages",
            "$Race/{RaceName}/Traits",
            "$Race/{RaceName}/Sub_Classes",    
            "$Race/{RaceName}/SubRaces",
            "$Race/{RaceName}/Age",
            "$Race/{RaceName}/Size",
            "$Race/{RaceName}/Alignment",
    ]
    Race_Data = {

    }


    #Please god find a better way to format this in the embed tool
    Character_Data = {
        "Ability Scores": "$Character_info/ability-scores/con \n $Character_info/ability-scores/dex \n $Character_info/ability-scores/str \n $Character_info/ability-scores/int \n $Character_info/ability-scores/wis \n $Character_info/ability-scores/cha",
        "Skills":"Ex:($Character_info/skills/Arcana) \n $Character_info/skills/{name} \n $Character_info/skills/{name}/ability-score \n $Character_info/skills/{name}/desc",
        "Proficiencies":"Ex:($Character_info/proficiencies/medium-armor) \n $Character_info/proficiencies/{name} \n $Character_info/proficiencies/{name}/classes \n $Character_info/proficiencies/{name}/races",
        "Languages":"Ex:($Character_info/languanges/common) \n $Character_info/languanges/{name} \n $Character_info/languanges/{name}/type \n $Character_info/languanges/{name}/speakers"
    }


    def intro():
        return """Hello, I am D&D bot. I exist to help with all your D&D needs and questions. My currrent knowledge base includes but is not limited to,classes, races, equipment, spells, monsters, mechanics and rules. I also manage my masters homebrews which I keep incase anyone is ever wondering what they are or if master ever forgets them. If you think my information is incorrect or outdated please message my creater to fix my ways."""

    def help():
        return "Here is are the all the beginning level commands that are currently available, follow their respective helpers for more information!"

    def character_def_help():
        return "Here are the currently known commands for Character Information!"


