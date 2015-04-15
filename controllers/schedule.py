import webapp2
import os
import json

from google.appengine.ext.webapp import template
from google.appengine.api import users
from google.appengine.ext import ndb
from models.account import user_info
from models.group import Group
from models.group_members import GroupMembers

class WholeSchedule(webapp2.RequestHandler):
    def get(self):
        user = user_info.get_user_account()
        schedule = user.schedule.get()
        self.response.out.write(json.dumps(schedule.schedule))

class GroupSchedule(webapp2.RequestHandler):
    def get(self):
        try:
            day = int(self.request.get('day'))
            hour = int(self.request.get('hour'))
            group_name = str(self.request.get('group'))
            user = user_info.get_user_account()
            group = Group.get_by_name(group_name)
            group_member = group.get_member(user.email)
            schedule = group_member.schedule.get()
            self.response.out.write(json.dumps(schedule.get_status_at(day, hour)))
        except Exception as e:
            self.response.our.write(json.dumps(error_obj(e.message)))

    def delete(self):
        try:
            '''
            day = int(self.request.get('day'))
            hour = int(self.request.get('hour'))
            '''
            group_name = str(self.request.get('group'))
            user = user_info.get_user_account()
            group = Group.get_by_name(group_name)
            group_member = group.get_member(user.email)
            schedule = group_member.schedule.get()
            schedule.clear_schedule()
            self.response.out.write(json.dumps(success_obj()))
        except Exception as e:
            self.response.our.write(json.dumps(error_obj(e.message)))


    def put(self):
        try:
            day = int(self.request.get('day'))
            hour = int(self.request.get('hour'))
            group_name = str(self.request.get('group'))
            status = int(self.request.get('status'))
            blurb = int(self.request.get('blurb'))
            user = user_info.get_user_account()
            group = Group.get_by_name(group_name)
            group_member = group.get_member(user.email)
            schedule = group_member.schedule.get()
            schedule.schedule_status(day, hour, status, blurb)
            self.response.out.write(success_obj())
        except Exception as e:
            self.response.our.write(json.dumps(error_obj(e.message)))

class Schedule(webapp2.RequestHandler):

    def get(self):
        try:
            day = int(self.request.get('day'))
            hour = int(self.request.get('hour'))
            user = user_info.get_user_account()
            schedule = user.schedule.get()
            self.response.out.write(json.dumps(schedule.get_status_at(day, hour)))
        except Exception as e:
            self.response.out.write(json.dumps(error_obj(e.message)))

    def delete(self):
        try:
            day = int(self.request.get('day'))
            hour = int(self.request.get('hour'))
            user = user_info.get_user_account()
            schedule = user.schedule.get()
            schedule.clear_schedule()
            self.response.out.write(json.dumps(success_obj()))
        except Exception as e:
            self.response.our.write(json.dumps(error_obj(e.message)))


    def put(self):
        try:
            day = int(self.request.get('day'))
            hour = int(self.request.get('hour'))
            status = int(self.request.get('status'))
            blurb = str(self.request.get('blurb'))
            user = user_info.get_user_account()
            schedule = user.schedule.get()
            schedule.schedule_status(day, hour, status, blurb)
            self.response.out.write(json.dumps(success_obj()))
        except Exception as e:
            self.response.our.write(json.dumps(error_obj(e.message)))

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