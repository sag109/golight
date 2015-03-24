import webapp2
import os
import json
import logging

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info
from models.group import Group
from models.group_members import GroupMembers

class User(webapp2.RequestHandler):
    def get(self):
        # Get your status within a group
        logging.info("Gettinggggggggggggggg")
        handle_as_user(self, get_user, ['groupName'])

    def post(self):
        # Add yourself to a group
        handle_as_user(self, post_user, ['groupName', 'status', 'blurb'])

    def delete(self):
        # Remove yourself from a group
        handle_as_user(self, delete_user, ['groupName'])

    def put(self):
        # Change your status within a group
        handle_as_user(self, put_user, ['groupName', 'status', 'blurb'])
        
def post_user(parameters):
    user = users.get_current_user()
    user_account = user_info.get_user_account()
    to_join = Group.get_by_name(parameters['groupName'])
    if not to_join:
        return json.dumps(error_obj('No group with this name exists.'))
    if to_join.key in user_account.group_keys:
        return json.dumps(error_obj('User already in this group.'))
    user_account.group_keys.append(to_join.key)
    user_account.put()
    
    # Making the new group member
    user_member = GroupMembers(email=user_account.email, status=0)
    user_member.blurb = parameters['blurb']
    user_member.group_key = to_join.key
    user_member.put()
    
    # Updating the group
    to_join.members.append(user_member.key)
    to_join.put()
    return json.dumps(success_obj())
    
def delete_user(parameters):
    """Leave a group"""
    user = users.get_current_user()
    to_leave = Group.get_by_name(parameters['groupName'])
    if not to_leave:
        return json.dumps(error_obj('No group with this name exists.'))
    user_account = user_info.get_user_account()
    if not to_leave.key in user_account.group_keys:
        return json.dumps(error_obj('You are not the in this group'))
    if user_account.email == to_leave.admin_email:
        return json.dumps(error_obj('You are the admin of this group.'))
    user_member = GroupMembers.query(ndb.AND(GroupMembers.group_key==to_leave.key,GroupMembers.email==user.email())).get()
    to_leave.members.remove(user_member.key)
    to_leave.put()
    user_account.group_keys.remove(to_leave.key)
    user_account.put()
    user_member.key.delete()
    return json.dumps(success_obj())

def put_user(parameters):
    user = users.get_current_user()
    to_update = Group.get_by_name(parameters['groupName'])
    if not to_update:
        return json.dumps(error_obj('No group with this name exists.'))
    user_account = user_info.get_user_account()
    if not to_update.key in user_account.group_keys:
        return json.dumps(error_obj('You are not in this group'))
    user_member = to_update.get_member(user_account.email)
    if not user_member:
        return json.dumps(error_obj('Server error.'))
    user_member.blurb = parameters['blurb']
    user_member.status = parameters['status']
    return json.dumps(success_obj())

def get_user(parameters):
    logging.info("in getting????????")
    user = users.get_current_user()
    group = Group.get_by_name(parameters['groupName'])
    logging.info("group "+ group)
    if not group:
        return json.dumps(error_obj('No group with this name exists.'))
    user_account = user_info.get_user_account()
    if not group.key in user_account.group_keys:
        return json.dumps(error_obj('The user is not in this group.'))
    member = group.get_member(user_account.email)
    info = {
        'email': member.email,
        'status': member.status,
        'blurb': member.blurb,
        'groupName': group.name
    }
    return json.dumps(info)

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
    logging.info("function is "+ function)
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