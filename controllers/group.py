import webapp2
import os
import json

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info
from models.group import Group as GroupModel
from models.group_members import GroupMembers

class Group(webapp2.RequestHandler):
    def get(self):
        # Get a list of group members with their blurbs and 
        # statuses
        handle_as_user(self, get_group, ['groupName'])

    def post(self):
        #creates a new group
        #groupName: name of the group
        #blurb: blurb for the group- max 50 char
        handle_as_user(self, post_group, ['groupName', 'blurb'])

    def delete(self):
        #deletes a group
        #groupName:name of the group to delete
        handle_as_user(self, delete_group, ['groupName'])

    def put(self):
        #changes the group settings
        #grouName: The name of the group to change
        #blurb: The string to set the group's blurb to- max 50 char
        handle_as_user(self, put_group, ['groupName', 'blurb'])
        
def post_group(parameters):
    if len(parameters['blurb']) > 50:
        return json.dumps(error_obj('Blurb cannot be longer than 50 chars'))
    if GroupModel.get_by_name(parameters['groupName']):
        return json.dumps(error_obj('Group with this name already exists.'))
    user = users.get_current_user()
    user_account = user_info.get_user_account()
    new_group = GroupModel(name=parameters['groupName'],blurb=parameters['blurb'])
    new_group.admin_email = user.email()
    
    # Making the creator a member
    creator_member = GroupMembers(status=0,group_key=new_group.key,email=user.email())
    creator_member.blurb = 'Let there be a group.'
    creator_member.put()
    new_group.members.append(creator_member.key)
    new_group.put()
    
    # Putting the group in the member's group list
    user_account.group_keys.append(new_group.key)
    user_account.put()
    return json.dumps(success_obj())
    
def delete_group(parameters):
    user = users.get_current_user()
    to_delete = GroupModel.get_by_name(parameters['groupName'])
    if not to_delete:
        return json.dumps(error_obj('No group with this name exists.'))
    user_account = user_info.get_user_account()
    if not to_delete.admin_email == user_account.email:
        return json.dumps(error_obj('You are not the admin of this group'))
    to_delete.clean_delete()
    return json.dumps(success_obj())

def put_group(parameters):
    user = users.get_current_user()
    to_update = GroupModel.get_by_name(parameters['groupName'])
    if not to_update:
        return json.dumps(error_obj('No group with this name exists.'))
    user_account = user_info.get_user_account()
    if not to_update.admin_email == user_account.email:
        return json.dumps(error_obj('You are not the admin of this group'))
    to_update.blurb = parameters['blurb']
    to_update.put()
    return json.dumps(success_obj())

def get_group(parameters):
    user = users.get_current_user()
    group = GroupModel.get_by_name(parameters['groupName'])
    if not group:
        return json.dumps(error_obj('No group with this name exists.'))
    user_account = user_info.get_user_account()
    if not group.key in user_account.group_keys:
        return json.dumps(error_obj('The user is not in this group.'))
    return json.dumps(group_info(group))

def group_info(group):
    info = []
    for member_key in group.members:
        member = member_key.get()
        info.append({
            'email': member.email,
            'blurb': member.blurb,
            'status': member.status,
        })
    return info

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