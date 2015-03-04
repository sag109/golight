import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class RenderEdit(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
        if user:
            self.response.out.write(template.render("templates/edit.html",{}))

    def post(self):
        user= users.get_current_user()
        if user:
            newFriend= self.request.get('newFriend')
            oldFriend= self.request.get('oldFriend')
            if newFriend:
                self.friend_add()
            else:
                self.friend_remove()
                
                
    def friend_add(self):
        user= users.get_current_user()
        newFriend= self.request.get('newFriend')
        
        currUser= user_info()
        usersList= user_info.query(user_info.email == user.email()).fetch(1)
        if len(usersList)>0:
            currUser= usersList[0]


        friendExist = False
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }

        friend_query=  user_info.query(user_info.email == newFriend).fetch(1)
        if len(friend_query)>0:
            friendExist = True
        

        if friendExist:
            areFriends = False
            for person in currUser.friend_list:
                if person == newFriend:
                    areFriends = True

            if areFriends:
                reply_info['status'] = "You are already friends with this user"
            else:
                currUser.friend_list.append(newFriend)
                currUser.put()
                reply_info['status'] = "You've successfully added a friend"
            
        else:
            reply_info['status'] = "This friend does not have an account"
            
        self.response.out.write(template.render("templates/edit.html", reply_info))


    def friend_remove(self):
        user= users.get_current_user()
        oldFriend= self.request.get('oldFriend')
        
        currUser= user_info()
        usersList= user_info.query(user_info.email == user.email()).fetch(1)
        if len(usersList)>0:
            currUser= usersList[0]

        friendExist = False
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        
        friend_query=  user_info.query(user_info.email == oldFriend).fetch(1)
        if len(friend_query)>0:
            friendExist = True

        if friendExist:
            areFriends = False
            for person in currUser.friend_list:
                if person == oldFriend:
                    areFriends = True
            
            if areFriends:
                currUser.friend_list.remove(oldFriend)
                currUser.put()
                reply_info['status'] = "You've successfully removed a friend"
               
            else:
                reply_info['status'] = "You are not friends with this user"


        else:
            reply_info['status'] = "This friend does not have an account"
            


        self.response.out.write(template.render("templates/edit.html", reply_info))

