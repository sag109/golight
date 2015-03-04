import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class Friends(webapp2.RequestHandler):
    def get(self):
        #parameter is friends
        user= users.get_current_user()
        if user:
            userExists = False
            worked = "worked"
            newUser = user_info()
            #allUsers= user_info.all()
            allUsers= user_info.query(user_info.email == user.email()).fetch(1)
            #newUser= user_info.get_or_insert(user.email())
            if allUsers:
                newUser= allUsers[0]
            #for person in allUsers:
            #    if person.email == user.email():
            #        userExists= True
            #        newUser= person
            #newUser = user_info.
            if not allUsers:
                #self.response.out.write('making a new user')
                worked = "broken"
                newUser.name= user.nickname()
                newUser.email= user.email()
                newUser.friend_list.append(user.email())#they are their own friend
                newUser.friend_list.append("golight.app@gmail.com")
                newUser.availability= "success"
                newUser.put()
            
            friends=[]
            addFriend= user_info()
            for friend in newUser.friend_list:
                addFriend = user_info.query(user_info.email == friend).fetch(1)[0]
                if addFriend:
                    #addFriend.availability = "success"
                    #addFriend.put()
                    friends.append(addFriend)
                    worked= "dafuq"
                #for person in allUsers:
                #    if person.email == friend:
                        #emails match
                #        friends.append(person)
            #for pal in friends:
             #   self.response.out.write(pal.name+'<br>')
            self.response.out.write(template.render("templates/friends.html",{
                "friends": friends,
                "logout_link": users.create_logout_url('/'),
                "worked": worked,
                "allUsers": allUsers,
                "addFriend": addFriend
            }))

