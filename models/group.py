import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb
from models.group_members import GroupMembers
from models.account import user_info

class Group(ndb.Model):
    name = ndb.StringProperty()
    members = ndb.KeyProperty(repeated=True)
    blurb = ndb.StringProperty()
    admin_email = ndb.StringProperty()

    @staticmethod
    def make_new(name, blurb):
        user = user_info.get_user_account()
        group = Group(
            name = name,
            blurb = blurb,
            admin_email = user.email
        )
        admin = GroupMembers.make_new(user)
        group.admin_email = user.email
        group.members.append(admin.key)
        group.put()
        return group

    @staticmethod
    def get_by_name(name):
        name_query = Group.query(Group.name == name)
        return name_query.get()
    
    def clean_delete(self):
        for member_key in self.members:
            member = member_key.get()
            account = user_info.get_by_email(member.email)
            account.group_keys.remove(self.key)
            account.put()
            member.remove_self()
        self.key.delete()
        
    def get_member(self, email):
        for member_key in self.members:
            member = member_key.get()
            if member.email == email:
                return member
        return None