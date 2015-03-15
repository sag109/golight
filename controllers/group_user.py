import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class User(webapp2.RequestHandler):
    def post(self):
        #add yourself to a group
        #groupName: name of the group

    def delete(self):
        #remove yourself from a group
        #groupName:name of the group to delete

    def put(self):
        #sets your status within a group
        #groupName: The name of the group to change
		#status: The integer to change the status to.
		
	def get(self):
		#gets the status within a group
		#groupName: The name of the group to get your status within.