import webapp2
import json
from api2 import handler
from google.appengine.api import users
from models.account import user_info
from google.appengine.ext import ndb

class Friends(webapp2.RequestHandler):
    def delete(self, friend_key):
        self.friend_key = friend_key
        response = handler.json_reply(self.delete_friend)
        self.response.out.write(response)

    def delete_friend(self):
        friend_key = ndb.Key(urlsafe=self.friend_key)
        user = user_info.get_user_account()
        user.delete_friend(friend_key)
        return handler.success

class FriendsList(webapp2.RequestHandler):
    def get(self):
        response = handler.json_reply(self.get_friends)
        self.response.out.write(response)

    def get_friends(self):
        user = user_info.get_user_account()
        def friend_info(friend_key):
            friend = friend_key.get()
            return {
                'key': friend.key.urlsafe(),
                'name': friend.name,
                'status': friend.status,
                'message': friend.message
            }
        return map(friend_info, user.friend_list)

class FriendRequests(webapp2.RequestHandler):
    def get(self):
        response = handler.json_reply(self.get_requests)
        self.response.out.write(response)

    def post(self, friend_key):
        self.friend_key = friend_key
        response = handler.json_reply(self.post_request)
        self.response.out.write(response)

    def delete(self, friend_key):
        self.friend_key = friend_key
        response = handler.json_reply(self.delete_request)
        self.response.out.write(response)

    def get_requests(self):
        user = user_info.get_user_account()
        response = {}
        for key, value in user.friend_requests:
            cur_user = key.get()
            response[key.urlsafe()] = {
                'message': value,
                'name': cur_user.name
            }
        return user.friend_requests()

    def post_request(self):
        data = json.loads(self.request.body)
        user = user_info.get_user_account
        friend_key = ndb.Key(urlsafe=self.friend_key.get())
        friend = friend_key.get()
        friend.friend_process(user.key, data['message'])
        return handler.success

    def delete_request(self):
        user = user_info.get_user_account()
        friend_key = ndb.Key(urlsafe=self.friend_key.get())
        user.remove_friend_request(friend_key)
        return handler.success
