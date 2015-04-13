import webapp2
import json
from api2 import handler
from google.appengine.api import users
from models.account import user_info
from models.group import Group
from google.appengine.ext import ndb

class GroupsList(webapp2.RequestHandler):
    def get(self):
        response = handler.json_reply(self.get_groups)
        self.response.out.write(response)

    def post(self):
        response = handler.json_reply(self.post_group)
        self.response.out.write(response)

    def post_group(self):
        data = json.loads(self.request.body)
        Group.new(data['name'], data['blurb'], public=data['public'])
        return handler.success

    def get_groups(self):
        user = user_info.get_user_account()
        def group_info(member_key):
            member = member_key.get()
            group = member.group_key.get()
            return {
                'name': group.name,
                'blurb': group.blurb,
                'key': group.key.urlsafe()
            }
        response = map(group_info, user.group_member_keys)
        return handler.success

class MemberList(webapp2.RequestHandler):
    def get(self, group_key):
        self.group_key = group_key
        response = handler.json_reply(self.get_group)
        self.response.out.write(response)

    def get_group(self):
        group_key = ndb.Key(urlsafe=self.group_key)
        group = group_key.get()
        info = []
        for member_key in group.members:
            member = member_key.get()
            info.append({
                'name': member.name,
                'status': member.status,
                'key': member.key.urlsafe(),
                'blurb': member.blurb
            })
        return info

class GroupDescription(webapp2.RequestHandler):
    def put(self, group_key):
        self.group_key = group_key
        response = handler.json_reply(self.put_desc)
        self.response.out.write(response)

    def put_desc(self):
        data = json.loads(self.request.body)
        group_key = ndb.Key(urlsafe=self.group_key)
        group = group_key.get()
        group.update_blurb(data['blurb'])
        return handler.success

class Admins(webapp2.RequestHandler):
    def post(self, group_key, user_key):
        self.user_key = user_key
        self.group_key = group_key
        response = handler.json_reply(self.post_admin)
        self.response.out.write(response)

    def delete(self, group_key, user_key):
        self.group_key = group_key
        self.user_key = user_key
        response = handler.json_reply(self.del_admin)
        self.response.out.write(response)

    def del_admin(self):
        group_key = ndb.Key(urlsafe=self.group_key)
        user_key = ndb.Key(urlsafe=self.group_key)
        group = group_key.get()
        group.delete_admin(user_key)
        return handler.success

    def post_admin(self):
        user_key = ndb.Key(urlsafe=self.user_key)
        group_key = ndb.Key(urlsafe=self.group_key)
        group = group_key.get()
        group.add_admin(user_key)
        return handler.success

class AdminList(webapp2.RequestHandler):
    def get(self, group_key):
        self.group_key = group_key
        response = handler.json_reply(self.get_admins)
        self.response.out.write(response)

    def get_admins(self):
        group_key = ndb.Key(urlsafe=self.group_key)
        group = group_key.get()
        def admin_info(admin_key):
            admin_user = admin_key.get()
            for key in admin_user.group_member_keys():
                if key in group.members:
                    member_key = key
            member = member_key.get()
            return {
                'name': member.name,
                'key': member_key,
            }
        return map(admin_info, group.admins)

class GroupStatus(webapp2.RequestHandler):
    def put(self, group_key):
        self.group_key = group_key
        response = handler.json_reply(self.put_status)
        self.response.out.write(response)

    def put_status(self):
        group_key = ndb.Key(urlsafe=self.group_key)
        data = json.loads(self.request.body)
        user = user_info.get_user_account()
        group = group_key.get()
        for member_key in group.members:
            if member_key in user.group_member_keys:
                user_member_key = member_key
                break
        if not user_member_key:
            raise Exception('Data inconsistency in groups.GroupStatus')
        user_member = user_member_key.get()
        user_member.update_blurb(data['blurb'])
        user_member.update_status(data['status'])
        return handler.success
