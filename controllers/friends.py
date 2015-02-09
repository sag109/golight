import webapp2
import os

from google.appengine.ext.webapp import template

class RenderFriends(webapp2.RequestHandler):
    def get(self):
        controller = "friends.py"
        self.response.out.write(template.render("templates/test.html",{"controller": controller}))