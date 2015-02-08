import webapp2
import os

from google.appengine.ext.webapp import template

class RenderHome(webapp2.RequestHandler):
    def get(self):
        self.response.out.write("templates/index.html")