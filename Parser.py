




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

    @staticmethod
    def prof_choices(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg[0]
        SubRace += 'Choose {}'.format(Raw_SubRace['choose']) + '\n'
        for x in Raw_SubRace['from']:
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

    @staticmethod
    def dcHandler(arg):
        if not arg:
            return []
        Ability_Bonuses = ''
        Raw_Ability_Bonuses = arg
        for x in Raw_Ability_Bonuses:
            if(x['name'] == 'Spellcasting Ability'):
                for y in x['desc']:
                    Ability_Bonuses += y + '\n'

        return Ability_Bonuses

class start_equip(RaceHandler):

    @staticmethod
    def equipmentHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += '\n' + 'Equipment Set:' + '\n'
            if(isinstance(x['from'],list)):
                for y in x['from']:
                    if(isinstance(y,list)):
                        for z in y:
                            if('equipment' in z):
                                SubRace += z['equipment']['name'] + '\n'
                            if('equipment_option' in z):
                                 SubRace += z['equipment_option']['from']['equipment_category']['name'] + '\n'
                    else:
                        if('equipment_option' in y):
                            SubRace += y['equipment_option']['from']['equipment_category']['name'] + '\n'
                        if('equipment' in y):
                            SubRace += y['equipment']['name'] + '\n'
                            
            else:
                SubRace += x['from']['equipment_category']['name'] + '\n'
                    
        return SubRace

    @staticmethod
    def startEquipmentHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        for x in Raw_SubRace:
            SubRace += x['equipment']['name'] + '\n'

        return SubRace

    @staticmethod
    def acHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg
        SubRace += 'Base AC: ' + str(Raw_SubRace['base']) + '\n'
        SubRace += 'Dex Bonus Applied: ' + str(Raw_SubRace['dex_bonus']) + '\n'
        SubRace += 'Max Bonus: ' + str(Raw_SubRace['max_bonus']) + '\n'
        return SubRace

    @staticmethod
    def rangeHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg

        SubRace += 'Normal Range: ' + str(Raw_SubRace['normal']) + '\n'
        SubRace += 'Long Range: ' + str(Raw_SubRace['long']) + '\n'

        return SubRace


    @staticmethod
    def damageHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_SubRace = arg

        SubRace += 'Damage Die: ' + str(Raw_SubRace['damage_dice']) + '\n'
        SubRace += 'Damage Type: ' + str(Raw_SubRace['damage_type']['name']) + '\n'

        return SubRace

    @staticmethod
    def contentHandler(arg):
        if not arg:
            return []
        SubRace = ''
        Raw_Contents = arg

        for x in Raw_Contents:
            SubRace += 'Quantity: ' + str(x['quantity']) + ' - ' + x['item']['name'] + '\n'

        return SubRace
