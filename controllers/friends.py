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
            user_exists = False
            worked = "worked"
            new_user = user_info()
            
            all_users= user_info.query(user_info.email == user.email()).fetch(1)
            if len(all_users)>0:
                new_user= all_users[0]
            
            if not all_users:
                
                worked = "broken"
                new_user.name= user.nickname()
                new_user.email= user.email()
                new_user.friend_list.append(user.email())#they are their own friend
                new_user.friend_list.append("golight.app@gmail.com")
                new_user.availability= "1"
                new_user.put()
                #after putting the new user, page must be refreshed to show their info
            
            friends=[]
            add_friend= user_info()
            for friend in new_user.friend_list:
                all_friends = user_info.query(user_info.email == friend).fetch(1)
                if len(all_friends)>0:
                    add_friend = all_friends[0]
                if add_friend:
                    friends.append(add_friend)
                    
                
            self.response.out.write(template.render("templates/friends.html",{
                "friends": friends,
                "logout_link": users.create_logout_url('/'),
            }))

