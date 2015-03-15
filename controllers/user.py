import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class User(webapp2.RequestHandler):
    def get(self):
        """Get your status and blurb."""
        user = users.get_current_user()
        if user:
            account = retrieve_account(user.email)
            if account:
                data = account_data(account)
                data_json = json.dumps(data)
                self.response.out.write(data_json)
            else:
                self.response.out.write(error_json('No account found'))
        else:
            self.response.out.write(error_json('User not logged in'))
    
    def put(self):
        """Set your status and blurb."""
        user = users.get_current_user()
        if user:
            account = retrieve_account(user.email)
            if account:
                blurb = self.request.get('blurb')
                status = self.request.get('status')
                set_account_data(account, status, blurb)
                account.put()
            else:
                self.response.out.write(error_json('No account found.'))
        else:
            self.response.out.write(error_json('User not logged in'))

def retrieve_account(email):
    """Get an account by the user's email"""
    accounts = user_info.query(user_info.email == email)
    if accounts:
        return accounts[0]
    else:
        return None    

def account_data(account):
    """Get the data for an account"""
    data = {
        'status': account.status,
        'availability': account.availability,
        'blurb': account.message
    }

def error_json(problem):
    """Create an error response"""
    response = {
        'error': problem
    }
    return json.dumps(response)
    
def set_account_data(account, status, blub):
    """Set the account data with the given information"""
    if status:
        account.status = status
    if blurb:
        account.message = blurb
