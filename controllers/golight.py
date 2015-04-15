import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info
import logging

class Golight(webapp2.RequestHandler):
    def get(self):
        logout = users.create_logout_url('/')
        self.response.out.write(template.render('templates/golight.html', {'logout': logout}))
