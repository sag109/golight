import webapp2
import os
import json

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class Friend(webapp2.RequestHandler):
    def get(self):
        """Get json for the user's list of friends"""
        user = users.get_current_user()
        if user:
            friend = self.request.get('email')
            user_account = user_info.retrieve_account(user.email)
            if not friend in user_account.friend_list:
                self.response.out.write(error_json('User not in friends list'))
                return
            friend_account = user_info.retrieve_account(friend)
            if friend_account:
                self.response.out.write(json.dumps(account_info(friend_account)))
            else:
                self.response.out.write(error_json('Friend not found'))
        else:
            self.response.out.write(error_json('User not logged in'))

    def post(self):
        """Add the friend"""
        user = users.get_current_user()
        if user:
            friend = self.request.get('email')
            user_account = user_info.retrieve_account(user.email)
            friend_account = user_info.retrieve_account(friend)
            if friend_account:
                user_account.friend_list.append(friend_account.email)
                user_account.put()
            else:
                self.response.out.write(error_json('Friend not found'))
        else:
            self.response.out.write(error_json('User not logged in'))

    def delete(self):
        """Remove the friend"""
        user = users.get_current_user()
        if user:
            friend = self.request.get('email')
            user_account = user_info.retrieve_account(user.email)
            if not friend in user_account.friend_list:
                self.response.out.write(error_json('User not in friends list'))
                return
            user_account.remove(friend.email)
            user_account.put()
        else:
            self.response.out.write(error_json('User not logged in'))

        
def account_info(account):
    data = {
        'name': account.name,
        'email': account.email,
        'status': account.status,
        'availability': account.availability
    }
    return data

def error_json(problem):
    """Create an error response"""
    response = {
        'error': problem
    }
    return json.dumps(response)
