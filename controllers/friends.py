import webapp2
import os
import json

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class Friends(webapp2.RequestHandler):
    def get(self):
        """Get json for the user's list of friends"""
        user = users.get_current_user()
        if user:
            account = user_info.retrieve_account(user.email)
            friends = []
            for person in account.friend_list:
                friends.append(user_info.retrieve_account(person))
            reply_data = map(lambda x: account_info(x), friends)
            self.response.out.write(json.dumps(reply_data))
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
