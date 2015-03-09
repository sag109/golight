import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class Group(webapp2.RequestHandler):
    def post(self):
        #creates a new group
        #groupName: name of the group
        #blurb: blurb for the group- max 50 char

    def delete(self):
        #deletes a group
        #groupName:name of the group to delete

    def put(self):
        #changes the group settings
        #grouName: The name of the group to change
        #blurb: The string to set the group's blurb to- max 50 char
        