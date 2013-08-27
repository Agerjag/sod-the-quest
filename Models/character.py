from google.appengine.ext import ndb


class Character(ndb):
    """

    """
    # TODO: DOCSTRING MY BITCH ASS.
    # System Data

    # Story data
    name = ndb.StringProperty(indexed=False)

    # Baseline Stats
    base_strength = ndb.IntegerProperty(indexed=False, default=0)
    base_dexterity = ndb.IntegerProperty(indexed=False, default=0)
    base_constitution = ndb.IntegerProperty(indexed=False, default=0)
    base_intelligence = ndb.IntegerProperty(indexed=False, default=0)
    base_wisdom = ndb.IntegerProperty(indexed=False, default=0)
    base_charisma = ndb.IntegerProperty(indexed=False, default=0)

    # Temporary Stat Changes
    temp_strength_bonus = ndb.IntegerProperty(indexed=False, default=0)
    temp_dexterity_bonus = ndb.IntegerProperty(indexed=False, default=0)
    temp_constitution_bonus = ndb.IntegerProperty(indexed=False, default=0)
    temp_intelligence_bonus = ndb.IntegerProperty(indexed=False, default=0)
    temp_wisdom_bonus = ndb.IntegerProperty(indexed=False, default=0)
    temp_charisma_bonus = ndb.IntegerProperty(indexed=False, default=0)

    #Skills


class BaseSkill(ndb):
    ranks = ndb.IntegerProperty(indexed=False, default=0)
    misc_modifier = ndb.IntegerProperty(indexed=False, default=0)
    class_skill = ndb.BooleanProperty(indexed=False, default=False)
    trained_only = False
    related_ability = ""


class Acrobatics(BaseSkill):
    related_ability = "DEX"
    trained_only = False


class Appraise(BaseSkill):
    related_ability = "INT"
    trained_only = False


class Bluff(BaseSkill):
    related_ability = "CHA"
    trained_only = False


class Craft(BaseSkill):
    related_ability = "INT"
    trained_only = False
    name = ndb.StringProperty(indexed=False, required=True)


class Diplomacy(BaseSkill):
    related_ability = "CHA"
    trained_only = False


class DisableDevice(BaseSkill):
    related_ability = "DEX"
    trained_only = True


class DisguiseX(BaseSkill):
    related_ability = "CHA"
    trained_only = False


class EscapeArtist(BaseSkill):
    related_ability = "DEX"
    trained_only = False


class Fly(BaseSkill):
    related_ability = "DEX"
    trained_only = False


class HandleAnimal(BaseSkill):
    related_ability = "CHA"
    trained_only = True


class Heal(BaseSkill):
    related_ability = "WIS"
    trained_only = False


class Intimidate(BaseSkill):
    related_ability = "CHA"
    trained_only = False


class Knowledge(BaseSkill):
    related_ability = "INT"
    trained_only = True
    name = ndb.StringProperty(indexed=False, required=True)


class Linguistics(BaseSkill):
    related_ability = "INT"
    trained_only = True


class Perception(BaseSkill):
    related_ability = "WIS"
    trained_only = False


class Perform(BaseSkill):
    related_ability = "CHA"
    trained_only = False
    name = ndb.StringProperty(indexed=False, required=True)


class Profession(BaseSkill):
    related_ability = "WIS"
    trained_only = True
    name = ndb.StringProperty(indexed=False, required=True)


class Ride(BaseSkill):
    related_ability = "DEX"
    trained_only = False


class SenseMotive(BaseSkill):
    related_ability = "WIS"
    trained_only = False


class SlightOfHand(BaseSkill):
    related_ability = "DEX"
    trained_only = True


class Spellcraft(BaseSkill):
    related_ability = "PRI"
    trained_only = True


class Stealth(BaseSkill):
    related_ability = "DEX"
    trained_only = False


class Survival(BaseSkill):
    related_ability = "WIS"
    trained_only = False


class Swim(BaseSkill):
    related_ability = "STR"
    trained_only = False


class UseMagicDevice(BaseSkill):
    related_ability = "CHA"
    trained_only = True


class Concentration(BaseSkill):
    related_ability = "PRI"
    trained_only = False


