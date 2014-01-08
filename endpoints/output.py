import webapp2
import logging
import json
from models.character import Character
from google.appengine.ext import ndb

import endpoints
from models.character import Character


class OutputCharacter(endpoints.BaseEndpoint):
    def get(self):
        key = self.request.get('KEY')
        ndb_key = ndb.Key(urlsafe=key)
        logging.info("NDB KEY: %r" % ndb_key)
        character = ndb_key.get()

        stat_dict = character.to_dict()

        json_str = json.dumps(stat_dict)
        self.response.headers['Content-Type'] = 'application/json'
        self.response.out.write(json_str)
        
        
handler = webapp2.WSGIApplication([
    ('/output/character.*', OutputCharacter)
], debug=True)