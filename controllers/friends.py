import webapp2
import os
import json

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import ndb
from models.account import user_info

class Friends(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            info = user_info.get_user_account()
            self.response.out.write(json.dumps(friend_list(info)))
        else:
            self.response.out.write(json.dumps(error_obj('User not logged in.')))

def friend_list(account):
    """Return a list of friend info for the account"""
    friend_infos = []
    for person in account.friend_list:
        cur_account = user_info.get_by_email(person)
        if cur_account:
            schedule = cur_account.schedule.get()
            now = schedule.get_current_status()
            friend_infos.append({
                'name': cur_account.name,
                'email': cur_account.email,
                'message': now['blurb'],
                'status': now['status'],
                'availability': now['status']
            })
    return friend_infos
    
def error_obj(message):
    """Make a dict that contains the error message"""
    return {
        'error': message
    }