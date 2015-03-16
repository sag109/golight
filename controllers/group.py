import webapp2
import os

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.group import group

import logging

class Group(webapp2.RequestHandler):
    def get(self):
        logging.info("get request")
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        reply_info['status']= self.request.get('group_name')
        self.response.out.write(template.render("templates/group.html", reply_info))

    def post(self):
        logging.info("post request")
        submit_type = self.request.get('submit_type')
        #reply_info = {
        #    'logout_link': users.create_logout_url('/')
        #    }
        #reply_info['status'] = "wish i was a baller"
        #reply_info['what'] = submit_type
        #self.response.out.write(template.render("templates/group.html", reply_info))
        if submit_type == "Update":
            logging.info("Update")
            self.put()
        elif submit_type == "Delete": 
            logging.info("Delete")
            self.delete()
        elif submit_type == "Add": 
            logging.info("Add")
            self.post_action()
        


    def post_action(self):
        #creates a new group
        #groupName: name of the group
        #blurb: blurb for the group- max 50 char
        logging.info("add")
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
            logging.info("group already exists")

        else:
            #group is created!
            new_group = group()
            new_group.name = group_name
            new_group.blurb = blurb
            new_group.put()
            reply_info['status'] = "Group Created"
            logging.info("group created")

        logging.info("end post action")
        self.response.out.write(reply_info['status'])
        #self.response.out.write(template.render("templates/group.html", reply_info))


    def delete(self):
        #this method doesn't currently work...
        #deletes a group
        #groupName:name of the group to delete
        logging.info("Delete method")
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        group_name = self.request.get('group_name')
        group_query = group.query(group.name == group_name).fetch(1)
        if len(group_query)>0:
            #assume that there is only one....
            ndb.Key('group', group_name).delete()
            #IDK how to delete things...
            reply_info['status'] = "Group deleted"
            logging.info("group Delete")
        else:
            reply_info['status'] = "Group does not exist"
            logging.info("group doesn't exist")



        logging.info("end Delete method")
        self.response.out.write(reply_info['status'])
        #self.response.out.write(template.render("templates/group.html", reply_info))


    def put(self):
        #changes the group settings
        #grouName: The name of the group to change
        #blurb: The string to set the group's blurb to- max 50 char
        logging.info("put method")
        reply_info = {
            'logout_link': users.create_logout_url('/')
            }
        group_name = self.request.get('group_name')
        blurb = self.request.get('blurb')
        logging.info("group name is "+group_name)
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
            logging.info("group exists")

        else:
            #group is created!
            new_group = group()
            new_group.name = group_name
            new_group.blurb = blurb
            new_group.put()
            reply_info['status'] = "New Group Created"
            logging.info("create new group?")



        logging.info("end put method")
        self.response.out.write(reply_info['status'])
        #self.response.out.write(template.render("templates/group.html", reply_info))
        