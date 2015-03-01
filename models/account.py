import webapp2

from google.appengine.api import users
from google.appengine.ext import db

class user_info(ndb.Model):
    name= ndb.StringProperty()
    email= ndb.StringProperty()
    friend_list= ndb.StringProperty(repeated=True)
    status= ndb.StringProperty()
    message= ndb.StringProperty()
    group_keys= ndb.KeyProperty(repeated=True)

class add_user(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user:
            user1 = user_info()
            user1.name= user.nickname()
            user1.email= user.email()
            user1.friend_list.appen("friend's name")
            user1.status= "freeee"
            user1.put()