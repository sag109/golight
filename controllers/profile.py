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
            user_exists = False
            new_user= user_info()
            users_list= user_info.query(user_info.email == user.email()).fetch(1)
            if len(users_list)>0:
                new_user= users_list[0]
                user_exists = True
           
            if not user_exists:
                
                new_user.name= user.nickname()
                new_user.email= user.email()
                new_user.friend_;ist.append(user.email())
                new_user.friend_list.append("golight.app@gmail.com")
                new_user.availability= "1"
                new_user.put()
        template_params = {
            "usernickname": new_user.name,
            "status": new_user.availability            
        }
        self.response.out.write(template.render("templates/profile.html", template_params))

    def post(self):
        user= users.get_current_user()
        if user:
            user_exists = False
            new_user= user_info()
            users_list= user_info.query(user_info.email == user.email()).fetch(1)
            if len(users_list)>0:
                new_user= users_list[0]
                user_exists = True
            if not user_exists:
                
                new_user.name= user.nickname()
                new_user.email= user.email()
                new_user.friend_list.append(user.email())
                new_user.friend_list.append("golight.app@gmail.com")
                new_user.availability= "1"
                new_user.put()

            input= self.request.get("status");
            if input == "update":
                if new_user.availability == "1":
                    new_user.availability= "0"
                elif new_user.availability == "0":
                    new_user.availability= "-1"
                elif new_user.availability == "-1":
                    new_user.availability= "1"
                else:
                    new_user.availability= "1"
                new_user.put()

            #get the updated status
            statusMessage= self.request.get("statusMessage")
            if statusMessage:
                new_user.message = statusMessage
                new_user.put() 


        template_params = {
            "logout_link": users.create_logout_url('/'),
            "usernickname": new_user.name,
            "status": new_user.availability            
        }
        self.response.out.write(template.render("templates/profile.html", template_params))
