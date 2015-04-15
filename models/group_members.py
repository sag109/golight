import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb
from models.schedule import Schedule

class GroupMembers(ndb.Model):
    email = ndb.StringProperty()
    blurb = ndb.StringProperty()
    status = ndb.IntegerProperty()
    group_key = ndb.KeyProperty() #why do we use this here?
    name = ndb.StringProperty()
    schedule = ndb.KeyProperty()

    def remove_self(self):
        self.schedule.delete()
        self.key.delete()

    @staticmethod
    def make_new(guy):
        member = GroupMembers()
        schedule = Schedule.make_new()
        member.schedule = schedule.key
        member.email = guy.email
        member.name = guy.name
        member.put()
        return member