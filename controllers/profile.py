import webapp2
import os

from models.account import user_info
from google.appengine.ext.webapp import template
from google.appengine.ext import ndb
from google.appengine.api import users

class RenderProfile(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
        if user:
            userExists = False
            newUser= user_info()
            usersList= user_info.query(user_info.email == user.email()).fetch(1)
            if len(usersList)>0:
                newUser= usersList[0]
                userExists = True
           
            if not userExists:
                
                newUser.name= user.nickname()
                newUser.email= user.email()
                newUser.friend_;ist.append(user.email())
                newUser.friend_list.append("golight.app@gmail.com")
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
            userExists = False
            newUser= user_info()
            usersList= user_info.query(user_info.email == user.email()).fetch(1)
            if len(usersList)>0:
                newUser= usersList[0]
                userExists = True
            if not userExists:
                
                newUser.name= user.nickname()
                newUser.email= user.email()
                newUser.friend_list.append(user.email())
                newUser.friend_list.append("golight.app@gmail.com")
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

            #get the updated status
            statusMessage= self.request.get("statusMessage")
            if statusMessage:
                newUser.message = statusMessage
                newUser.put() 


        template_params = {
            "logout_link": users.create_logout_url('/'),
            "usernickname": newUser.name,
            "status": newUser.availability            
        }
        self.response.out.write(template.render("templates/profile.html", template_params))
