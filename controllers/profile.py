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
                newUser.friendList.append("dontbelonely@pitt.edu")
                newUser.availability= "Success"
                newUser.put()

            template_params = {
                "usernickname": newUser.name()
                "status": newUser.availability
            }
            render_template(self, 'output.html', template_params)

    def post(self):
        # controller = "login.py"
        # self.response.out.write(template.render("templates/test.html",{"controller": controller}))
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
                newUser.friendList.append("dontbelonely@pitt.edu")
                newUser.availability= "Success"
                newUser.put()

            input= self.request.get("status");
            if(input == "update")
                if(newUser.availability() == "Success")
                    newUser.availability = "Danger"
                else if(newUser.availability() == "Danger")
                    newUser.availability = "Warning"
                else if(newUser.availability() == "Warning")
                    newUser.availability = "Success"
                else
                    newUser.availability = "Default"
                newUser.put()
                
            template_params = {
                "usernickname": newUser.nickname()
                "status": newUser.availability
            }
            render_template(self, 'output.html', template_params)
            

