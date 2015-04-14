import webapp2
import os
import json

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.api import mail
from google.appengine.ext import ndb
from models.account import user_info
from models.group import Group
from models.group_members import GroupMembers
import logging

class LogoutLink(webapp2.RequestHandler):
    def get(self):
    	user = users.get_current_user()
    	logout_link = users.create_logout_url('/')
        self.response.out.write(json.dumps({'url':logout_link}))