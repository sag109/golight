import webapp2
import os
import json
import logging

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import ndb
from models.account import user_info

class User(webapp2.RequestHandler):
    def get(self):
        """Get your status and blurb."""
        user = users.get_current_user()
        if user:
            user_account = user_info.get_user_account()
            self.response.out.write(json.dumps(account_info(user_account)))
        else:
            self.response.out.write(json.dumps(error_obj('User not logged in.')))

    def put(self):
        """Set your status and blurb."""
        user = users.get_current_user()
        if not user:
            self.response.out.write(json.dumps(error_obj('User not logged in.')))
            return
        user_account = user_info.get_user_account()
        new_status = self.request.get('status')
        new_blurb = self.request.get('blurb')
        
        name = self.request.get('name') #and here is where we'd check if username is already taken!
        if name:
            user_account.name = name
            user_account.put()
            self.response.out.write(json.dumps(success_obj()))
            return

        if not new_status or not new_blurb:
            self.response.out.write(json.dumps(error_obj('Request must include status and blurb.')))
            return
        if len(new_blurb) > 50:
            self.response.out.write(json.dumps(error_obj('Blurb cannot be more than 50 characters.')))
        schedule = user_account.schedule.get()
        schedule.update_status(int(new_status), new_blurb)
        self.response.out.write(json.dumps(success_obj()))
    
def account_info(account):
    """Make a dict of the status information for an account."""
    schedule = account.schedule.get()
    now = schedule.get_current_status()
    return {
        'status': now['status'],
        'availability': now['status'],
        'blurb': now['blurb'],
        'email': account.email,
        'name': account.name,
        'success': True
    }
    
def success_obj():
    """Dict for a success message"""
    return {
        'success': True
    }
    
    
def error_obj(message):
    """Make a dict that contains the error message"""
    return {
        'error': message,
        'success': False
    }