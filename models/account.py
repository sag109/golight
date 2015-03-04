import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

class user_info(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    friend_list = ndb.StringProperty(repeated=True)
    status = ndb.IntegerProperty()
    availability = ndb.StringProperty()
    message = ndb.StringProperty()
    group_keys = ndb.KeyProperty(repeated=True)