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
    acrobatics = ndb.StructuredProperty(modelclass=Acrobatics, default=None)
    appraise = ndb.StructuredProperty(modelclass=Appraise, default=None)
    bluff = ndb.StructuredProperty(modelclass=Bluff, default=None)
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
        pass

    @property
    def dexterity(self):
        pass

    @property
    def constitution(self):
        pass

    @property
    def intelligence(self):
        pass

    @property
    def wisdom(self):
        pass

    @property
    def charisma(self):
        pass

    @property
    def strength_bonus(self):
        pass

    @property
    def dexterity_bonus(self):
        pass

    @property
    def constitution_bonus(self):
        pass

    @property
    def intelligence_bonus(self):
        pass

    @property
    def wisdom_bonus(self):
        pass

    @property
    def charisma_bonus(self):
        pass

    @property
    def primary_bonus(self):
        pass
    

class BaseSkill(ndb):
    ranks = ndb.IntegerProperty(indexed=False, default=0)
    misc_modifier = ndb.IntegerProperty(indexed=False, default=0)
    class_skill = ndb.BooleanProperty(indexed=False, default=False)
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    related_ability = ndb.StringProperty(indexed=False, default="")
    desc = ndb.StringProperty(indexed=False, default="")

    @property
    def skill_level(self):
        components = [
            int(self.ranks), int(self.misc_modifier),
            3 if self.class_skill else 0,
            int(getattr(self, unicode(self.related_ability), 0))
        ]
        return sum(components)


class Acrobatics(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Appraise(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="integer_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Bluff(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Craft(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="intelligence_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    name = ndb.StringProperty(indexed=False, required=True)


class Diplomacy(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class DisableDevice(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bouns")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)


class Disguise(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class EscapeArtist(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Fly(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class HandleAnimal(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)


class Heal(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Intimidate(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Knowledge(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="intelligence_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    name = ndb.StringProperty(indexed=False, required=True)


class Linguistics(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="intelligence_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)


class Perception(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Perform(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)
    name = ndb.StringProperty(indexed=False, required=True)


class Profession(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)
    name = ndb.StringProperty(indexed=False, required=True)


class Ride(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class SenseMotive(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class SlightOfHand(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)


class Spellcraft(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="primary_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)


class Stealth(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="dexterity_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Survival(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="wisdom_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class Swim(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="strength_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


class UseMagicDevice(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="charisma_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=True)


class Concentration(BaseSkill):
    related_ability = ndb.StringProperty(indexed=False, default="primary_bonus")
    trained_only = ndb.BooleanProperty(indexed=False, default=False)


