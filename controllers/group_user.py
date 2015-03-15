import webapp2
import os
import logging

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info

class User(webapp2.RequestHandler):
    def post(self):
        #add yourself to a group
        #groupName: name of the group
        logging.info("/group/user post")
		
        group_name = self.request.get(groupName)
        group = group.query(group.name == group_name).fetch(1)
        if len(group)>0:
            curr_user= users.get_current_user()
            user = user_info()
            user_query = user_info.query(user_info.email == curr_user.email()).fetch(1)
            if len(user_query)>0:
                user = user_query[0]
            else:
                self.response.out.write("<html><body>User not found.</body></html>")
            
            new_member = group_members()
            new_member.name = user.name
            new_member.status = user.status
            new_member.availability = user.availability
            
            update_group = group_query[0]
            update_group.members.append(new_member)
            update_group.put()
        else:
            self.response.out.write("<html><body>Group not found.</body></html>")
        
    def delete(self):
        #remove yourself from a group
        #groupName:name of the group to delete
        logging.info("/group/user delete")

    def put(self):
        #sets your status within a group
        #groupName: The name of the group to change
        #status: The integer to change the status to.
        logging.info("/group/user put")
        
        status = self.request.get(status)
        group_name = self.request.get(groupName)
        group = group.query(group.name == group_name).fetch(1)
        if(len(group)>0):
            curr_user= users.get_current_user()
            user = user_info()
            user_query = user_info.query(user_info.email == curr_user.email()).fetch(1)
            if len(user_query)>0:
                user=user_query[0]
            else:
                self.response.out.write("<html><body>User not found.</body></html>")
            
            update_group = group_query[0]
            update_members = group_members[]
            update_members = update_group.members
            for member in update_members:
                if(member.name == user.name):
                    member.status = status
        else:
            self.response.out.write("<html><body>Group not found.</body></html>")

    def get(self):
		#gets your status within a group
		#groupName: The name of the group to get your status within.
        logging.info("/group/user get")
        
        group_name= self.request.get("groupName")
		group_query = group.query(group.name == group_name).fetch(1)
        if len(group_query)>0:
		    
        else:
		    #
			
		self.response.out.write(template.render("templates/group_user.html", {
		    "group": group,
			"logout_link": users.create_logout_url('/'),
		}))