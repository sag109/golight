import webapp2
import os
import json

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info
from models.group import Group
from models.group_members import GroupMembers

class Member(webapp2.RequestHandler):

    def post(self):
        # Add somebody to a group
        handle_as_user(self, post_member, ['groupName', 'email'])

    def delete(self):
        # Remove somebody from a group
        handle_as_user(self, delete_user, ['groupName', 'email'])

def post_member(parameters):
    user = users.get_current_user()
    user_account = user_info.get_user_account()
    group = Group.get_by_name(parameters['groupName'])
    if not group:
        return json.dumps(error_obj('No group with this name exists.'))
    if not group.admin_email == user_account.email:
        return json.dumps(error_obj('User not the admin of this group.'))
    new_user = user_info.get_by_email(parameters['email'])
    if not new_user:
        return json.dumps(error_obj('This email not associated with a user.'))
    
    # Making the new member
    member = GroupMembers.make_new(new_user)
    
    # Updating the group
    group.members.append(member.key)
    group.put()
    
    # Updating the account
    new_user.group_keys.append(group.key)
    new_user.put()
    return json.dumps(success_obj())
    
def delete_user(parameters):
    user = users.get_current_user()
    user_account = user_info.get_user_account()
    group = Group.get_by_name(parameters['groupName'])
    if not group:
        return json.dumps(error_obj('No group with this name exists.'))
    if not group.admin_email == user_account.email:
        return json.dumps(error_obj('User not the admin of this group.'))
    del_user = group.get_member(parameters['email'])
    if not del_user:
        return json.dumps(error_obj('This email not associated with a user in the group.'))
    del_account = user_info.get_by_email(parameters['email'])
    if not del_account:
        return json.dumps(error_obj('Database error.'))
    del_account.group_keys.remove(group.key)
    del_account.put()
    group.members.remove(del_user.key)
    group.put()
    del_user.remove_self()
    return json.dumps(success_obj())

def handle_as_user(handler, function, required_parameters):
    """For the handler, run and write out the function if the user
    is logged in and the required params exist"""
    user = users.get_current_user()
    if not user:
        handler.response.out.write(json.dumps(error_obj('User not logged in')))
        return
    # Making a dict of the required parameters
    parameters = {}
    for param in required_parameters:
        current = handler.request.get(param)
        if not current:
            handler.response.out.write(json.dumps(error_obj('Missing parameter: ' + param)))
            return
        parameters[param] = current
    handler.response.out.write(function(parameters))
        
def success_obj():
    """Dict for a success message"""
    return {
        'success': True
    }
    
    
def error_obj(message):
    """Make a dict that contains the error message"""
    return {
        'error': message,
        'success': False
    }