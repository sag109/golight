import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info
import logging

class RenderEdit(webapp2.RequestHandler):
    def get(self):
        user= users.get_current_user()
        if user:
            self.response.out.write(template.render("templates/edit.html",{'logout_link': users.create_logout_url('/')}))

    def post(self):
        user= users.get_current_user()
        if user:
            new_friend= self.request.get('new_friend')
            old_friend= self.request.get('old_friend')
            if new_friend:
                self.friend_add()
            else:
                self.friend_remove()
                
                
    def friend_add(self):
        user= users.get_current_user()
        new_friend= self.request.get('new_friend')
        
        curr_user= user_info()
        users_list= user_info.query(user_info.email == user.email()).fetch(1)
        if len(users_list)>0:
            curr_user= users_list[0]


        friend_exist = False
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }

        friend_query=  user_info.query(user_info.email == new_friend).fetch(1)
        logging.info(friend_query)
        if len(friend_query)>0:
            friend_exist = True
            are_friends = False
            for person in curr_user.friend_list:
                if person == new_friend:
                    are_friends = True

            if are_friends:
                reply_info['status'] = "You are already friends with this user"
            else:
                curr_user.friend_list.append(new_friend)
                curr_user.put()
                reply_info['status'] = "You've successfully added a friend"
            
        else:
            logging.info("hit this")
            reply_info['status'] = "This friend does not have an account"
            
        self.response.out.write(template.render("templates/edit.html", reply_info))


    def friend_remove(self):
        user= users.get_current_user()
        old_friend= self.request.get('old_friend')
        
        curr_user= user_info()
        users_list= user_info.query(user_info.email == user.email()).fetch(1)
        if len(users_list)>0:
            curr_user= users_list[0]

        friend_exist = False
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        
        friend_query=  user_info.query(user_info.email == old_friend).fetch(1)
        if len(friend_query)>0:
            friend_exist = True

        if friend_exist:
            are_friends = False
            for person in curr_user.friend_list:
                if person == old_friend:
                    are_friends = True
            
            if are_friends:
                curr_user.friend_list.remove(old_friend)
                curr_user.put()
                reply_info['status'] = "You've successfully removed a friend"
               
            else:
                reply_info['status'] = "You are not friends with this user"


        else:
            reply_info['status'] = "This friend does not have an account"
            


        self.response.out.write(template.render("templates/edit.html", reply_info))

