import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info
import logging

class Create(webapp2.RequestHandler):
    def get(self):
        logout = users.create_logout_url('/')
        self.response.out.write(template.render('templates/add_create.html', {'logout': logout}))

    def post(self):
        logout = users.create_logout_url('/')
        self.response.out.write(template.render('templates/add_create.html', {'logout': logout}))
        '''
        group_name = self.request.get("group_name");
        if not group_name:
            return json.dumps(error_obj('No group name provided.'))
        group = Group.get_by_name(group_name)
        if not group:
            return json.dumps(success_obj())
        else:
            user_account = user_info.get_user_account()
            if to_leave.key in user_account.group_keys:
                return json.dumps(error_obj('You are already in this group.'))
            return json.dumps(success_obj())
        '''
         
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