import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class Test(webapp2.RequestHandler):
    def get(self):
        reply = template.render('templates/test.html', {})
        self.response.out.write(reply)
