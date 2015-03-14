import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.group import group

class Group(webapp2.RequestHandler):
    def get(self):
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        self.response.out.write(template.render("templates/group.html", reply_info))


    def post(self):
        submit_type = self.request.get('submit_type')
        #reply_info = {
        #    'logout_link': users.create_logout_url('/')
        #    }
        #reply_info['status'] = "wish i was a baller"
        #reply_info['what'] = submit_type
        #self.response.out.write(template.render("templates/group.html", reply_info))
        if submit_type == "Update":
            self.put()
        elif submit_type == "Delete": 
            self.delete()
        else: 
            self.post_action()


    def post_action(self):
        #creates a new group
        #groupName: name of the group
        #blurb: blurb for the group- max 50 char
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        submit_type = self.request.get('sumbit_type')
        reply_info['what'] = submit_type
        group_name = self.request.get('group_name')
        blurb = self.request.get('blurb')
        group_query = group.query(group.name == group_name).fetch()
        if len(group_query)>0:
            #group already exists, so return that...?
            reply_info['status'] = "This group already exists"

        else:
            #group is created!
            new_group = group()
            new_group.name = group_name
            new_group.blurb = blurb
            new_group.put()
            reply_info['status'] = "Group Created"


        self.response.out.write(template.render("templates/group.html", reply_info))


    def delete(self):
        #deletes a group
        #groupName:name of the group to delete
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        group_name = self.request.get('group_name')
        group_query - group.query(group.name == group_name).fetch(1)
        if len(group_query)>0:
            #assume that there is only one....
            ndb.Key('group', group_name).delete()
            reply_info['status'] = "Group deleted"
        else:
            reply_info['status'] = "Group does not exist"




        self.response.out.write(template.render("templates/group.html", reply_info))


    def put(self):
        #changes the group settings
        #grouName: The name of the group to change
        #blurb: The string to set the group's blurb to- max 50 char
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        group_name = self.request.get('group_name')
        blurb = self.request.get('blurb')
        group_query = group.query(group.name == group_name).fetch(1)
        wat = group_query
        reply_info['what'] = wat 
        if len(group_query)>0:
            #group already exists, so return that...?
            update_group = group_query[0]
            update_group.name = group_name
            update_group.blurb = blurb
            update_group.put()
            reply_info['status'] = "This group was updated"

        else:
            #group is created!
            new_group = group()
            new_group.name = group_name
            new_group.blurb = blurb
            new_group.put()
            reply_info['status'] = "New Group Created"




        self.response.out.write(template.render("templates/group.html", reply_info))
        