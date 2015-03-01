import webapp2

from google.appengine.api import users
from google.appengine.ext import db

class user_info(db.Model):
    name= db.StringProperty()
    email= db.StringProperty()
    friendList= db.ListProperty(str)
    availability= db.StringProperty()
    message= db.StringProperty()
    #friendList will store user.User

class Render_user(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
      # there is an authenticated user
      #url = users.create_logout_url('/')
            #db.
            user1 = user_info()
            user1.name= user.nickname()
            user1.email= user.email()
            user1.friendList.append("friend's name")
            user1.availability= "freeee"
            user1.put()
            allUsers= user_info.all()
            self.response.out.write('<html><body>')
            self.response.out.write('Hello, ' + user.nickname() + '!<br><br>')
            for person in allUsers:
                self.response.out.write(person.name+'<br>'+person.email+'<br>'+person.availability+'<br>')
            self.response.out.write('</body></html>')
#store with object.put()

class add_user(webapp2.RequestHandler):
    def post(self):
        user = users.get_current_user()
        if user:
            user1 = user_info()
            user1.name= user.nickname()
            user1.email= user.email()
            user1.friendList.appen("friend's name")
            user1.availability= "freeee"
            user1.put()