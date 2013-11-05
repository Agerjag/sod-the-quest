import webapp2
import logging
from models.character import Character
from google.appengine.ext import ndb

import endpoints
from models.character import Character


class OutputCharacter(endpoints.BaseEndpoint):
    def get(self):
        key = self.request.get('KEY')
        ndb_key = ndb.Key(urlsafe=key)
        logging.info("NDB KEY: %r" % ndb_key)
        c = ndb_key.get()
        STR = int(c.strength)
        DEX = int(c.dexterity)
        CON = int(c.constitution)
        INT = int(c.intelligence)
        WIS = int(c.wisdom)
        CHA = int(c.charisma)
        html = "<html><body><h1>{0}</h1><br><table><tr><th>Attribute</th><th>Value</th></tr><tr><td>Strength</td><td>{1}</td></tr><tr><td>Dexterity</td><td>{2}</td></tr><tr><td>Constitution</td><td>{3}</td></tr><tr><td>Intelligence</td><td>{4}</td></tr><tr><td>Wisdom</td><td>{5}</td></tr><tr><td>Charisma</td><td>{6}</td></tr></table></body></html>".format(
            c.name, STR, DEX, CON, INT, WIS, CHA
        )
        self.response.out.write(html)
        
        
handler = webapp2.WSGIApplication([
    ('/output/character.*', OutputCharacter)
], debug=True)