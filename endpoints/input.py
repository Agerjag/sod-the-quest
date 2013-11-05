import webapp2
import endpoints
from models.character import Character


class InputCharacter(endpoints.BaseEndpoint):
    def get(self):
        self.name = self.request.get('NAME')
        self.strength = self.request.get('STR')
        self.dexterity = self.request.get('DEX')
        self.constitution = self.request.get('CON')
        self.intelligence = self.request.get('INT')
        self.wisdom = self.request.get('WIS')
        self.charisma = self.request.get('CHA')

        character = Character()
        character.name = self.name
        character.base_strength = int(self.strength)
        character.base_dexterity = int(self.dexterity)
        character.base_constitution = int(self.constitution)
        character.base_intelligence = int(self.intelligence)
        character.base_wisdom = int(self.wisdom)
        character.base_charisma = int(self.charisma)

        key = character.put()
        self.response.out.write('<h3>{}</h3>'.format(key.urlsafe()))

handler = webapp2.WSGIApplication([
    ('/input/character.*', InputCharacter)
], debug=True)