




class RaceHandler:

    @staticmethod
    def abilityHandler(arg):
        if not arg:
            return []
        Ability_Bonuses = ''
        Raw_Ability_Bonuses = arg
        for x in Raw_Ability_Bonuses:
            Ability_Bonuses += x['ability_score']['name'] + ': ' + str(x['bonus']) + '\n'


        return Ability_Bonuses

    @staticmethod
    def proficienciesHandler(arg):
        if not arg:
            return []
        Proficiencies = ''
        Raw_Proficiencies = arg
        print(Raw_Proficiencies)
        for x in Raw_Proficiencies:
            Proficiencies += x['name'] + '\n'

        return Proficiencies

    @staticmethod
    def languageHandler(arg):
        if not arg:
            return []
        Languages = ''
        Raw_Languages = arg
        for x in Raw_Languages:
            Languages += x['name'] + '\n'

        return Languages

    @staticmethod
    def traitHandler(arg):
        if not arg:
            return []
        Traits = ''
        Raw_Traits = arg
        for x in Raw_Traits:
            Traits += x['name'] + '\n'

        return Traits

    @staticmethod
    def SubHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x['name'] + '\n'

        return SubRace

    @staticmethod
    def DescHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x + '\n'

        return SubRace

    @staticmethod
    def SkillHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x['name'] + '\n'

        return SubRace

class SubRaceHandler(RaceHandler):

    @staticmethod
    def proficienciesHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x['name'] + '\n'

        return SubRace


class TraitHandler(RaceHandler):
    @staticmethod
    def raceHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x['name'] + '\n'

        return SubRace

class LanguageHandler:

    @staticmethod
    def raceHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x + '\n'

        return SubRace

class ProficienciesHandler:

    @staticmethod
    def classHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x['name'] + '\n'

        return SubRace

class SpellsHandler:

    @staticmethod
    def spellHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x['name'] + '\n'

        return SubRace

    @staticmethod
    def damageHandler(arg):
        if not arg:
            return []
        Ability_Bonuses = ''
        Raw_Ability_Bonuses = arg
        counter = 9
        i = 1
        while(i < counter):
            if(str(i) in Raw_Ability_Bonuses):
                Ability_Bonuses += str(i) + ': ' + Raw_Ability_Bonuses[str(i)] + '\n'
            i = i + 1
        return Ability_Bonuses
