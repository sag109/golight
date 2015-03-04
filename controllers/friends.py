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
            
            allUsers= user_info.query(user_info.email == user.email()).fetch(1)
            if len(allUsers)>0:
                newUser= allUsers[0]
            
            if not allUsers:
                
                worked = "broken"
                newUser.name= user.nickname()
                newUser.email= user.email()
                newUser.friend_list.append(user.email())#they are their own friend
                newUser.friend_list.append("golight.app@gmail.com")
                newUser.availability= "success"
                newUser.put()
                #after putting the new user, page must be refreshed to show their info
            
            friends=[]
            addFriend= user_info()
            for friend in newUser.friend_list:
                allFriends = user_info.query(user_info.email == friend).fetch(1)
                if len(allFriends)>0:
                    addFriend = allFriends[0]
                if addFriend:
                    friends.append(addFriend)
                    
                
            self.response.out.write(template.render("templates/friends.html",{
                "friends": friends,
                "logout_link": users.create_logout_url('/'),
               # "worked": worked,
               # "allUsers": allUsers,
               # "addFriend": addFriend
            }))

