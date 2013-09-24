__author__ = 'chrislococo'

from google.appengine.ext import ndb


class Campaign(ndb):
    start_date = ndb.DateProperty(indexed=False, auto_now_add=True)
    last_played = ndb.DateTimeProperty(indexed=True, auto_now=True)
    game_master = ndb.KeyProperty(kind="Account", indexed=True, required=True)
    players = ndb.KeyProperty(kind="Account", indexed=True, repeated=True)

