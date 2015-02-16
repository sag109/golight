import webapp2
import os

from Account import user_info
from google.appengine.ext.webapp import template
from google.appengine.ext import db
from google.appengine.api import users

class RenderProfile(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
        if user:
            allUsers= user_info.all()
            userExists= False
            newUser = user_info()
            for person in allUsers:
                if person.email == user.email():
                    userExists= True
                    newUser= person
            if not userExists:
                #self.response.out.write('making a new user')
                newUser.name= user.nickname()
                newUser.email= user.email()
                newUser.friendList.append(user.email())
                newUser.friendList.append("golight.app@gmail.com")
                newUser.availability= "success"
                newUser.put()
        template_params = {
            "usernickname": newUser.name,
            "status": newUser.availability            
        }
        self.response.out.write(template.render("templates/profile.html", template_params))

    def post(self):
        user= users.get_current_user()
        if user:
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
                newUser.availability= "success"
                newUser.put()

            input= self.request.get("status");
            if input == "update":
                if newUser.availability == "success":
                    newUser.availability= "warning"
                elif newUser.availability == "warning":
                    newUser.availability= "danger"
                elif newUser.availability == "danger":
                    newUser.availability= "success"
                else:
                    newUser.availability= "success"
                newUser.put()
        template_params = {
            "logout_link": users.create_logout_url('/'),
            "usernickname": newUser.name,
            "status": newUser.availability            
        }
        self.response.out.write(template.render("templates/profile.html", template_params))
