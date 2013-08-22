__author__ = 'chrislococo'

from google.appengine.ext import ndb
from models.player import Player


class Character(ndb):
    # Reference Information
    player_id = ndb.KeyProperty(kind=Player)
    character_name = ndb.StringProperty(indexed=False)

    # Base Attributes
    strength = ndb.IntegerProperty(indexed=False)
    dexterity = ndb.IntegerProperty(indexed=False)
    constitution = ndb.IntegerProperty(indexed=False)
    intelligence = ndb.IntegerProperty(indexed=False)
    wisdom = ndb.IntegerProperty(indexed=False)
    charisma = ndb.IntegerProperty(indexed=False)

    @property
    def get_bonus(self, ability=None):
        """
        This property method calculates the bonus value of a given attribute.

        :param ability: The name of the ability being checked
        :type ability: str
        :return:
        """
        if not ability:
            return 0
        else:
            ability_score = getattr(self, ability, 0)
            return (ability_score - 10) / 2