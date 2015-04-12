import webapp2

from google.appengine.api import users
from google.appengine.ext import ndb
from models.group_members import GroupMembers
from models.account import user_info

class Group(ndb.Model):
    #the name of the group
    name = ndb.StringProperty()

    #the list of the members of the group, as group_member keys
    members = ndb.KeyProperty(repeated=True)

    #the group's description
    blurb = ndb.StringProperty()

    #the group's admins, their user_info keys
    admins = ndb.KeyProperty(repeated=True)

    #whether the group is public
    public = ndb.BooleanProperty()

    def new(self, name, desc, public=True):
        assert isinstance(name, str)
        assert isinstance(desc, str)
        assert isinstance(public, bool)
        if not (1 <= len(name) <= 20):
            raise Exception('Name length must be between 0 and 20 characters.')
        if not (0 <= len(desc) <= 50):
            raise Exception('Blurb must be between 0 and 50 characters.')
        current_user = user_info.get_user_account()
        new_group = Group(name=name,
                          blurb=desc,
                          admins=[user_info.key],
                          public=public)
        new_member = GroupMembers(new_group, current_user, True)
        new_member.put()
        new_group.members = [new_member]
        new_group.put()

    def clean_delete(self):
        cur_user = user_info.get_user_account()
        if not cur_user.key in self.admins:
            raise Exception('User does not have admin privileges for this group.')
        for member_key in self.members:
            cur_member = member_key.get()
            cur_member.clean_delete()
        self.key.delete()

    def join(self):
        cur_user = user_info.get_user_account()
        for member_key in self.members:
            if member_key in cur_user.group_member_keys:
                raise Exception('User already in this group.')
        if not self.public:
            if self.key in cur_user.group_invites:
                del cur_user.group_invites[self.key]
            else:
                raise Exception('This is a private group. An admin must invite you.')
        new_member = GroupMembers.new(self, cur_user, False)
        new_member.put()
        self.key.put()

    def update_name(self, name):
        assert isinstance(name, str)
        cur_user = user_info.get_user_account()
        if not cur_user.key in self.admins:
            raise Exception('User does not have admin privileges for this group.')
        if not 0 < len(name) <= 20:
            raise Exception('Invalid name length.')
        self.name = name
        self.key.put()

    def update_blurb(self, blurb):
        assert isinstance(blurb, str)
        cur_user = user_info.get_user_account()
        if not cur_user.key in self.admins:
            raise Exception('User does not have admin privileges for this group.')
        if not 0 <= len(blurb) <= 50:
            raise Exception('Blurb length must be between 0 and 50 chars.')
        self.blurb = blurb
        self.key.put()

    def add_admin(self, user_key):
        assert isinstance(user_key, ndb.Key)
        cur_user = user_info.get_user_account()
        if not cur_user.key in self.admins:
            raise Exception('User does not have admin privileges for this group.')
        new_admin = user_key.get()
        self.admins.append(user_key)
        #this is done in this way to minimize datastore reads
        for member_key in self.members:
            if member_key in new_admin.group_member_keys:
                member = member_key.get()
                member.set_admin()
                member.put()
                self.key.put()
                return
        raise Exception('This person is not an admin for this group.')

    def delete_admin(self, user_key):
        assert isinstance(user_key, ndb.Key)
        cur_user = user_info.get_user_account()
        if not cur_user.key in self.admins:
            raise Exception('User does not have admin privileges for this group.')
        if not user_key in self.admins:
            raise Exception('This person is not an admin for this group.')
        if len(self.admins) < 2:
            raise Exception('This is the last admin for the group. We can\'t delete them. Don\'t be ridiculous.')
        del_user = user_key.get()
        for member_key in self.members:
            if member_key in del_user.group_member_keys:
                member = member_key.get()
                member.admin = False
                member.put()
                self.admins.remove(user_key)
                self.key.put()
                return
        raise Exception('Internal data inconsistency in group.delete_admin!')

    def invite(self, user_key):
        assert isinstance(user_key, ndb.Key)
        if self.public:
            raise Exception('This is not a private group.')
        cur_user = user_info.get_user_account()
        if not cur_user.key in self.admins:
            raise Exception('User does not have admin privileges for this group.')
        invited_user = user_key.get()
        if self.key in invited_user.group_invites:
            raise Exception('Invitation already sent.')
        for member_key in self.members:
            if member_key in invited_user.group_member_keys:
                raise Exception('User already in group.')
        invited_user.group_invites[self.key] = self.blurb
        invited_user.put()