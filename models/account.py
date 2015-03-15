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
    
    @staticmethod
    def retrieve_account(cls, email):
    """Get an account by the user's email"""
    accounts = user_info.query(user_info.email == email)
        if accounts:
            return accounts[0]
        else:
            return None   