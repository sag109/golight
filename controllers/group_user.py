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
		
        #Pull the group from ndb.
        group_name = self.request.get('groupName')
        group = group.query(group.name == group_name).fetch(1)
        if len(group)>0:
            #Get current user's user_info object.
            curr_user= users.get_current_user()
            user = user_info()
            user_query = user_info.query(user_info.email == curr_user.email()).fetch(1)
            if len(user_query)>0:
                user = user_query[0]
            else:
                self.response.out.write("<html><body>User not found.</body></html>")
                logging.info("ERROR: User not found!")
            
            #Add the current user to group by creating new group_members object.
            new_member = group_members()
            new_member.name = user.name
            new_member.status = user.status
            new_member.availability = user.availability
            #new_member.member_key = ???
            
            #Update the group so results reflect work.
            update_group = group_query[0]
            update_group.members.append(new_member)
            update_group.put()
        else:
            self.response.out.write("<html><body>Group not found.</body></html>")
            logging.info("ERROR: Group not found!")
        
    def delete(self):
        #remove yourself from a group
        #groupName:name of the group to delete
        logging.info("/group/user delete")
        
        #Pull group from ndb.
        group_name = self.request.get('groupName')
        group = group.query(group.name == group_name).fetch(1)
        if(len(group)>0):
            #Get current user's user_info object.
            curr_user= users.get_current_user()
            user = user_info()
            user_query = user_info.query(user_info.email == curr_user.email()).fetch(1)
            if len(user_query)>0:
                user=user_query[0]
            else:
                self.response.out.write("<html><body>User not found.</body></html>")
                logging.info("ERROR: User not found!")
            #Pull members from group
            update_group = group_query[0]
            update_members = group_members[]
            update_members = update_group.members
            
            #Find the users member object.
            curr_member = group_members()
            for member in update_members:
                if(member.name == user.name):
                    curr_member = member
                    break
            #Remove the user from the group.
            if(curr_member):
                update_members.remove(curr_member)
            else:
            self.response.out.write("<html><body>You're not in the group.</body></html>")
            logging.info("ERROR: User wasn't in group to remove!")
            
            #Update the group so results reflect work.
            update_group.members = update_members
            update_group.put()

        else:
            self.response.out.write("<html><body>Group not found.</body></html>")
            logging.info("ERROR: Group not found!")

    def put(self):
        #sets your status within a group
        #groupName: The name of the group to change
        #status: The integer to change the status to.
        logging.info("/group/user put")
        
        #Pull group from ndb.
        new_status = self.request.get('status')
        group_name = self.request.get('groupName')
        group = group.query(group.name == group_name).fetch(1)
        if(len(group)>0):
            #Pull current user's user_object.
            curr_user= users.get_current_user()
            user = user_info()
            user_query = user_info.query(user_info.email == curr_user.email()).fetch(1)
            if len(user_query)>0:
                user=user_query[0]
            else:
                self.response.out.write("<html><body>User not found.</body></html>")
                logging.info("ERROR: User not found!")
            
            #Pull group's members.
            update_group = group_query[0]
            update_members = group_members[]
            update_members = update_group.members
            
            #Find current user's member object in group and update status.
            for member in update_members:
                if(member.name == user.name):
                    member.status = new_status
                    break
            
            #Update the group so results reflect work.
            update_group.members = update_members
            update_group.put()

        else:
            self.response.out.write("<html><body>Group not found.</body></html>")
            logging.info("ERROR: Group not found!")

    def get(self):
        #gets your status within a group
        #groupName: The name of the group to get your status within.
        logging.info("/group/user get")
        
        #Pull current group from NDB.
        curr_status = "NULL"
        group_name = self.request.get('groupName')
        group = group.query(group.name == group_name).fetch(1)
        if(len(group)>0):
            #Pull current user's user_object
            curr_user= users.get_current_user()
            user = user_info()
            user_query = user_info.query(user_info.email == curr_user.email()).fetch(1)
            if len(user_query)>0:
                user=user_query[0]
            else:
                self.response.out.write("<html><body>User not found.</body></html>")
                logging.info("ERROR: User not found!")
            
            #Pull members from group.
            update_group = group_query[0]
            update_members = group_members[]
            update_members = update_group.members
            
            #Find current user's member object in group and get the status.
            for member in update_members:
                if(member.name == user.name):
                    curr_status = member.status
                    break
                    
            #Return the status.
            self.response.out.write("<html><body>" + curr_status + "</body></html>")
            logging.info("Success!")

        else:
            self.response.out.write("<html><body>Group not found.</body></html>")
            logging.info("ERROR: Group not found!")
		