from google.appengine.ext import db

class user_info(db.Model):
    name= db.StringProperty()
    email= db.StringProperty()
    friendList= db.ListProperty(user.User())
    #friendList will store user.User

#store with object.put()