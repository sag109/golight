import webapp2
import os

from google.appengine.ext.webapp import template

class RenderMain(webapp2.RequestHandler):
    def get(self):
        controller = "main.py"
        self.response.out.write(template.render("templates/test.html",{"controller": controller}))