import webapp2
import json
from api2 import handler
from google.appengine.api import users
from models.account import user_info
from models.group import Group
from google.appengine.ext import ndb

class Users(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(handler.json_reply(self.search_users))

    def search_users(self):
        user = user_info.get_user_account()
        query = user_info.query()
        for key in user.friend_list:
            query.filter(user_info.key != key)
        users = query.fetch()
        users.sort()
        return map(lambda x: {
            'name': x.name,
            'key': x.key.urlsafe()
        }, users)

class Groups(webapp2.RequestHandler):
    def get(self):
        self.response.out.write(handler.json_reply(self.search_groups))

    def search_groups(self):
        user = user_info.get_user_account()
        query = Group.query()
        groups = query.fetch()
        return map(lambda x: {
            'name': x.name,
            'key': x.key.urlsafe()
        }, groups)