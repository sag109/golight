import webapp2
import os
import json
import logging

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import ndb
from models.account import user_info

class Friend(webapp2.RequestHandler):
    def get(self):
        """Get a global friend's availability and blurb."""
        user = users.get_current_user()
        if not user:
            self.response.out.write(json.dumps(error_obj('User not logged in.')))
            return
        friend = self.request.get('email')
        if not friend:
            self.response.out.write(json.dumps(error_obj('Must provide email of friend to add.')))
            return
        account = user_info.get_user_account()
        if not friend in account.friend_list:
            self.response.out.write(json.dumps(error_obj('This email is not in your friends list.')))
            return
        friend_account = user_info.get_by_email(friend)
        self.response.out.write(json.dumps(account_info(friend_account)))

    def post(self):
        """Add a friend"""
        user = users.get_current_user()
        if not user:
            self.response.out.write(json.dumps(error_obj('User not logged in.')))
            return
            
            
        friend = self.request.get('email')
        if not friend:
            self.response.out.write(json.dumps(error_obj('Must provide email of friend to add.')))
            return
            
        #added in for fun
        account = user_info.get_user_account()
        if friend in account.friend_list:
            self.response.out.write(json.dumps(error_obj('You are already friends with this user.')))
            return
        #/added in for fun  
            
        friend_account = user_info.get_by_email(friend)
        if not friend_account:
            self.response.out.write(json.dumps(error_obj('There is no account for this email.')))
            return
        account.friend_list.append(friend)
        account.put()
        self.response.out.write(json.dumps(success_obj()))
    
    def delete(self):
        """Remove a friend."""
        user = users.get_current_user()
        if not user:
            self.response.out.write(json.dumps(error_obj('User not logged in.')))
            return
        friend = self.request.get('email')
        if not friend:
            self.response.out.write(json.dumps(error_obj('Must provide email of friend to add.')))
            return
        account = user_info.get_user_account()
        if not friend in account.friend_list:
            self.response.out.write(json.dumps(error_obj('This email is not in your friends list.')))
            return
        account.friend_list.remove(friend)
        account.put()
        self.response.out.write(json.dumps(success_obj()))

def account_info(account):
    """Make a dict of the status information for an account."""
    schedule = account.schedule.get()
    current = schedule.get_current_status()
    return {
        'status': current['status'],
        'availability': current['status'],
        'blurb': current['blurb'],
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