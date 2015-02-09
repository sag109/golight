import webapp2
import os

from google.appengine.ext.webapp import template

class RenderLogin(webapp2.RequestHandler):
    def get(self):
        controller = "login.py"
        self.response.out.write(template.render("templates/test.html",{"controller": controller}))