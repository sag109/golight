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
    def get_by_email(email):
        account_query = user_info.query(user_info.email == str(email))
        # Get executes the query and returns the first result, or None
        # if no results were generated.
        return account_query.get()
