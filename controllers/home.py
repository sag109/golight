import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users

class RenderHome(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        if user:
            self.response.out.write('logged in!')
        else:
            self.response.out.write('not logged in')

