import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

class group_members(ndb.Model):
    name= ndb.StringProperty()
    availability= ndb.StringProperty()
	status= ndb.StringProperty()
    member_key= ndb.KeyProperty()