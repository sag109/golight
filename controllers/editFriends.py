import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from Account import user_info

class RenderEdit(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
        if user:
            self.response.out.write(template.render("templates/edit.html",{}))

    def post(self):
        user= users.get_current_user()
        if user:
            newFriend= self.request.get('newFriend')
            allUsers= user_info.all()
            currUser= user_info()
            friendExist = False
            for person in allUsers:
                if person.email == user.email():
                    currUser= person
                    currUser.friendList.append(newFriend)
                    currUser.put()
                    friendExist = True
            if friendExist:
                status = "You've successfully added a friend"
                self.response.out.write(template.render("templates/edit.html",{"status":status}))
            else:
                status = "This friend does not have an account"
                self.response.out.write(template.render("templates/edit.html",{"status":status}))
            #self.response.out.write('<html><body>'+newFriend+'</body></html>')

