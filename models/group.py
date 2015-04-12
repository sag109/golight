import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb
from models.group_members import GroupMembers
from models.account import user_info

class Group(ndb.Model):
    #the name of the group
    name = ndb.StringProperty()

    #the list of the members of the group
    members = ndb.KeyProperty(repeated=True)

    #the group's description
    blurb = ndb.StringProperty()

    #the group's admins
    admins = ndb.KeyProperty()
    
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
            member.key.delete()
        self.key.delete()
        
    def get_member(self, email):
        for member_key in self.members:
            member = member_key.get()
            if member.email == email:
                return member
        return None