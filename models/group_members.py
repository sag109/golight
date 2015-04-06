import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

class GroupMembers(ndb.Model):
    email = ndb.StringProperty()
    blurb = ndb.StringProperty()
    status = ndb.IntegerProperty()
    group_key = ndb.KeyProperty() #why do we use this here?
    name = ndb.StringProperty()