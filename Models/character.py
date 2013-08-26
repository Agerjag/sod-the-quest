__author__ = 'chrislococo'

from google.appengine.ext import ndb

class Character(ndb):
    name = ndb.StringProperty(indexed=False)
