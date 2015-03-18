import webapp2
import os
import json
import logging

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import ndb
from models.account import user_info
from models.group import Group

class Groups(webapp2.RequestHandler):
    def get(self):
        """Get a global friend's availability and blurb."""
        user = users.get_current_user()
        if not user:
            self.response.out.write(json.dumps(error_obj('User not logged in.')))
            return
        user_account = user_info.get_by_email(user.email())
        groups = []
        for g in user_account.group_keys:
            group = g.get()
            groups.append({
                'name': group.name,
                'admin': group.admin_email == user.email()
            })
        self.response.out.write(json.dumps(groups))

def error_obj(message):
    """Make a dict that contains the error message"""
    return {
        'error': message,
        'success': False
    }