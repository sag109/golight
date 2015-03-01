import webapp2

from google.appengine.api import users
from google.appengine.ext import db

class group(ndb.Model):
    name= ndb.StringProperty()
    members= ndb.JsonProperty(repeated=True)
    blurb= ndb.StringProperty()
    group_key= ndb.KeyProperty()

