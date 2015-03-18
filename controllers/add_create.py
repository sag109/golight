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