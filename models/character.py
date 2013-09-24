from google.appengine.ext import ndb


class Character(ndb):
    """

    """
    # TODO: DOCSTRING MY BITCH ASS.
    # System Data

    # Story data
    name = ndb.StringProperty(indexed=False)
    alignment = ndb.StringProperty(indexed=False)

    # Generic Information
    base_hitpoints = ndb.IntegerProperty(indexed=False, default=0)
    base_hitpoints = ndb.IntegerProperty(indexed=False, default=0)
    current_hitpoints = ndb.IntegerProperty(indexed=False, default=0)

    # Baseline Stats
    base_strength = ndb.IntegerProperty(indexed=False, default=0)
    base_dexterity = ndb.IntegerProperty(indexed=False, default=0)
    base_constitution = ndb.IntegerProperty(indexed=False, default=0)
    base_intelligence = ndb.IntegerProperty(indexed=False, default=0)
    base_wisdom = ndb.IntegerProperty(indexed=False, default=0)
    base_charisma = ndb.IntegerProperty(indexed=False, default=0)

    # Temporary Stat Changes
    temp_strength = ndb.IntegerProperty(indexed=False, default=0)
    temp_dexterity = ndb.IntegerProperty(indexed=False, default=0)
    temp_constitution = ndb.IntegerProperty(indexed=False, default=0)
    temp_intelligence = ndb.IntegerProperty(indexed=False, default=0)
    temp_wisdom = ndb.IntegerProperty(indexed=False, default=0)
    temp_charisma = ndb.IntegerProperty(indexed=False, default=0)

    # Class Data
    primary_stat = ndb.StringProperty(indexed=False, default="")

    # Skills
    acrobatics = ndb.StructuredProperty(modelclass=Acrobatics, default=None)
    appraise = ndb.StructuredProperty(modelclass=Appraise, default=None)
    bluff = ndb.StructuredProperty(modelclass=Bluff, default=None)
    climb = ndb.StructuredProperty(modelclass=Climb, default=None)
    craft = ndb.StructuredProperty(modelclass=Craft, default=None, repeated=True)
    diplomacy = ndb.StructuredProperty(modelclass=Diplomacy, default=None)
    disable_device = ndb.StructuredProperty(modelclass=DisableDevice, default=None)
    disguise = ndb.StructuredProperty(modelclass=Disguise, default=None)
    escape_artist = ndb.StructuredProperty(modelclass=EscapeArtist, default=None)
    fly = ndb.StructuredProperty(modelclass=Fly, default=None)
    handle_animal = ndb.StructuredProperty(modelclass=HandleAnimal, default=None)
    heal = ndb.StructuredProperty(modelclass=Heal, default=None)
    intimidate = ndb.StructuredProperty(modelclass=Intimidate, default=None)
    knowledge = ndb.StructuredProperty(modelclass=Knowledge, default=None, repeated=True)
    linguistics = ndb.StructuredProperty(modelclass=Linguistics, default=None)
    perception = ndb.StructuredProperty(modelclass=Perception, default=None)
    perform = ndb.StructuredProperty(modelclass=Perform, default=None, repeated=True)
    profession = ndb.StructuredProperty(modelclass=Profession, default=None, repeated=True)
    ride = ndb.StructuredProperty(modelclass=Ride, default=None)
    sense_motive = ndb.StructuredProperty(modelclass=SenseMotive, default=None)
    slight_of_hand = ndb.StructuredProperty(modelclass=SlightOfHand, default=None)
    spellcraft = ndb.StructuredProperty(modelclass=Spellcraft, default=None)
    stealth = ndb.StructuredProperty(modelclass=Stealth, default=None)
    survival = ndb.StructuredProperty(modelclass=Survival, default=None)
    swim = ndb.StructuredProperty(modelclass=Swim, default=None)
    use_magic_device = ndb.StructuredProperty(modelclass=UseMagicDevice, default=None)
    concentration = ndb.StructuredProperty(modelclass=Concentration, default=None)
    
    @property
    def strength(self):
        return int(self.base_strength) + int(self.temp_strength)

    @property
    def dexterity(self):
        return int(self.base_dexterity) + int(self.temp_dexterity)

    @property
    def constitution(self):
        return int(self.base_constitution) + int(self.temp_constitution)

    @property
    def intelligence(self):
        return int(self.intelligence) + int(self.temp_intelligence)

    @property
    def wisdom(self):
        return int(self.wisdom) + int(self.temp_wisdom)

    @property
    def charisma(self):
        return int(self.charisma) + int(self.temp_charisma)

    @property
    def strength_bonus(self):
        return _stat_bonus(self.strength)

    @property
    def dexterity_bonus(self):
        return _stat_bonus(self.dexterity)

    @property
    def constitution_bonus(self):
        return _stat_bonus(self.constitution)

    @property
    def intelligence_bonus(self):
        return _stat_bonus(self.intelligence)

    @property
    def wisdom_bonus(self):
        return _stat_bonus(self.wisdom)

    @property
    def charisma_bonus(self):
        return _stat_bonus(self.charisma)

    @property
    def primary_bonus(self):
        return _stat_bonus(getattr(self, unicode(self.primary_stat), 0))


class BaseSkill(ndb):
    ranks = ndb.IntegerProperty(indexed=False, default=0)
    misc_modifier = ndb.IntegerProperty(indexed=False, default=0)
    class_skill = ndb.BooleanProperty(indexed=False, default=False)
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    related_ability = ndb.StringProperty(indexed=False, default="")

    @property
    def skill_level(self):
        """
        Property method which returns the total value of a skill.

        :return: The value of the skill with the ranks, modifiers, class bonuses, and stat bonuses.
        :rtype: int
        """
        components = [
            int(self.ranks), int(self.misc_modifier),
            3 if self.class_skill else 0,
            int(getattr(self, unicode(self.related_ability), 0))
        ]
        return sum(components)


class Acrobatics(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You can keep your balance while traversing narrow or treacherous surfaces. " \
                  "You can also dive, flip, jump, and roll to avoid attacks and overcome " \
                  "obstacles."


class Appraise(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="integer_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You can evaluate the monetary value of an object."


class Bluff(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You know how to tell a lie."


class Climb(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="strength_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You are skilled at scaling vertical surfaces, from smooth city walls to " \
                  "rocky cliffs."

class Craft(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="intelligence_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    name = ndb.StringProperty(indexed=False, required=True)
    description = "You are skilled in the creation of a specific group of items, such as armor " \
                  "or weapons. Like Knowledge, Perform, and Profession, Craft is actually a " \
                  "number of separate skills. You could have several Craft skills, each with its" \
                  " own ranks. The most common Craft skills are alchemy, armor, baskets, books," \
                  " bows, calligraphy, carpentry, cloth, clothing, glass, jewelry, leather, " \
                  "locks, paintings, pottery, sculptures, ships, shoes, stonemasonry, traps, " \
                  "and weapons."

class Diplomacy(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You can use this skill to persuade others to agree with your arguments, to " \
                  "resolve differences, and to gather valuable information or rumors from " \
                  "people. This skill is also used to negotiate conflicts by using the proper " \
                  "etiquette and manners suitable to the problem."


class DisableDevice(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bouns")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    description = "You are skilled at disarming traps and opening locks. In addition, this " \
                  "skill lets you sabotage simple mechanical devices, such as catapults, wagon " \
                  "wheels, and doors."


class Disguise(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You are skilled at changing your appearance."


class EscapeArtist(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "Your training allows you to slip out of bonds and escape from grapples."


class Fly(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You are skilled at flying, through either the use of wings or magic, and can " \
                  "perform daring or complex maneuvers while airborne. Note that this skill does" \
                  " not give you the ability to fly."


class HandleAnimal(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    description = "You are trained at working with animals, and can teach them tricks, get them " \
                  "to follow your simple commands, or even domesticate them."


class Heal(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You are skilled at tending to wounds and ailments."


class Intimidate(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You can use this skill to frighten an opponent or to get them to act in a way" \
                  " that benefits you. This skill includes verbal threats and displays of prowess."


class Knowledge(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="intelligence_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    name = ndb.StringProperty(indexed=False, required=True)
    description = "You are educated in a field of study and can answer both simple and complex" \
                  " questions. Like the Craft, Perform, and Profession skills, Knowledge " \
                  "actually encompasses a number of different specialties. Below are listed " \
                  "typical fields of study."


class Linguistics(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="intelligence_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    description = "You are skilled at working with language, in both its spoken and written " \
                  "forms. You can speak multiple languages, and can decipher nearly any tongue " \
                  "given enough time. Your skill in writing allows you to create and detect " \
                  "forgeries as well."


class Perception(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "Your senses allow you to notice fine details and alert you to danger. " \
                  "Perception covers all five senses, including sight, hearing, touch, " \
                  "taste, and smell."


class Perform(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    name = ndb.StringProperty(indexed=False, required=True)
    description = "You are skilled at one form of entertainment, from singing to acting to " \
                  "playing an instrument. Like Craft, Knowledge, and Profession, Perform is " \
                  "actually a number of separate skills. You could have several Perform skills, " \
                  "each with its own ranks."


class Profession(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    name = ndb.StringProperty(indexed=False, required=True)
    description = "You are skilled at one form of entertainment, from singing to acting to " \
                  "playing an instrument. Like Craft, Knowledge, and Profession, Perform is " \
                  "actually a number of separate skills. You could have several Perform skills, " \
                  "each with its own ranks."


class Ride(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You are skilled at riding mounts, usually a horse, but possibly something " \
                  "more exotic, like a griffon or pegasus."


class SenseMotive(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You are skilled at detecting falsehoods and true intentions."


class SlightOfHand(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    description = "Your training allows you to pick pockets, draw hidden weapons, and take a " \
                  "variety of actions without being noticed."


class Spellcraft(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="primary_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    description = "You are skilled at the art of casting spells, identifying magic items, " \
                  "crafting magic items, and identifying spells as they are being cast."


class Stealth(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You are skilled at avoiding detection, allowing you to slip past foes or " \
                  "strike from an unseen position. This skill covers hiding and moving silently."


class Survival(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    description = "You are skilled at surviving in the wild and at navigating in the " \
                  "wilderness. You also excel at following trails and tracks left by others."


class Swim(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="strength_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    descriptions = "You know how to swim and can do so even in stormy water."


class UseMagicDevice(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    description = "You are skilled at activating magic items, even if you are not " \
                  "otherwise trained in their use."


class Concentration(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="primary_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


def _stat_bonus(value):
    """
    This helper function returns the bonus value of a basic stat.

    :param value: Value of the basic stat being used to determine the bonus value.
    :type value: int
    :return: The bonus value of the stat value in question.
    :rtype: int
    """
    return (value - 10) / 2 if value > 0 else -5