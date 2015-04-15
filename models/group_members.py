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

    @staticmethod
    def make_new():
        member = GroupMembers()
        schedule = Schedule.make_new()
        member.schedule = schedule.key
        member.put()
        return member