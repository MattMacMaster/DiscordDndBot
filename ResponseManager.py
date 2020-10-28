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

    Character_Data = {
        "Ability Scores": "$Character_info/ability-scores/con \n $Character_info/ability-scores/dex \n $Character_info/ability-scores/str \n $Character_info/ability-scores/int \n $Character_info/ability-scores/wis \n $Character_info/ability-scores/cha",
        "Skills":"",
        "Proficiencies":"",
        "Languages":""
    }


    def intro():
        return """Hello, I am D&D bot. I exist to help with all your D&D needs and questions. My currrent knowledge base includes but is not limited to,classes, races, equipment, spells, monsters, mechanics and rules. I also manage my masters homebrews which I keep incase anyone is ever wondering what they are or if master ever forgets them. If you think my information is incorrect or outdated please message my creater to fix my ways."""

    def help():
        return "Here is are the all the beginning level commands that are currently available, follow their respective helpers for more information!"

    def character_def_help():
        return "Here are the currently known commands for Character Information!"


