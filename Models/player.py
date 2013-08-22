__author__ = 'chrislococo'

from google.appengine.ext import ndb

class Player(ndb):
    user = ndb.UserProperty()
    email = ndb.StringProperty()
