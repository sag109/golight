import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from Account import user_info

class RenderFriends(webapp2.RequestHandler):
    def get(self):
        #parameter is friends
        user= users.get_current_user()
        if user:
            userExists= False
            newUser = user_info()
            allUsers= user_info.all()
            for person in allUsers:
                if person.email == user.email():
                    userExists= True
                    newUser= person
            if not userExists:
                #self.response.out.write('making a new user')
                newUser.name= user.nickname()
                newUser.email= user.email()
                newUser.friendList.append(user.email())#they are their own friend
                newUser.friendList.append("golight.app@gmail.com")
                newUser.availability= "success"
                newUser.put()
            friends=[]
            for friend in newUser.friendList:
                for person in allUsers:
                    if person.email == friend:
                        #emails match
                        friends.append(person)
            #for pal in friends:
             #   self.response.out.write(pal.name+'<br>')
            self.response.out.write(template.render("templates/friends.html",{
                "friends": friends,
                "logout_link": users.create_logout_url('/')
            }))

