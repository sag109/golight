import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import db
from Account import user_info

class User(webapp2.RequestHandler):
    def post(self):
        #add yourself to a group
        #groupName: name of the group to join

    def delete(self):
        #remove yourself from a group
        #groupName:name of the group to leave

    def put(self):
        #sets your status within group
        #grouName: The name of the group to change your status in
        #the integer to change the status to. 

    def get(self):
        #gets your status within a group. 
        #groupName: the name of the group to get your status within. 
        