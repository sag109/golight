import webapp2
import os

from Account import user_info
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

class RenderProfile(webapp2.RequestHandler):
    def get(self):
       # controller = "login.py"
       # self.response.out.write(template.render("templates/test.html",{"controller": controller}))
       user= users.get_current_user()
       if user:
            self.response.out.write('<html><body>')
            allUsers= user_info.all()
            userExists= False
            newUser = user_info()
            for person in allUsers:
                if person.email == user.email():
                    userExists= True
                    newUser= person
            if not userExists:
                self.response.out.write('making a new user')
                newUser.name= user.nickname()
                newUser.email= user.email()
                newUser.friendList.append(user.email())
                newUser.friendList.append("golight.app@gmail.com")
                newUser.availability= "Success"
                newUser.put()

            
            self.response.out.write('Hello, ' + user.nickname() + '!<br><br>')
            self.response.out.write(newUser.email+'<br>')

            for pal in newUser.friendList:
                self.response.out.write(pal+'<br>')
            self.response.out.write('</body></html>')



