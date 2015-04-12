import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb

class GroupMembers(ndb.Model):
    blurb = ndb.StringProperty()
    status = ndb.IntegerProperty()
    group_key = ndb.KeyProperty() #why do we use this here?
    name = ndb.StringProperty()
    admin = ndb.BooleanProperty()
    user_info_key = ndb.KeyProperty()

    #must also manage info for users, including invites!
    def clean_delete(self):
        pass