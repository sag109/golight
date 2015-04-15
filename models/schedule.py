import webapp2
import logging
from datetime import datetime as dt

from google.appengine.api import users
from google.appengine.ext import ndb

class Schedule(ndb.Model):
    schedule = ndb.JsonProperty()
    last_hour = ndb.IntegerProperty()
    last_day = ndb.IntegerProperty()
    status = ndb.IntegerProperty()
    blurb = ndb.StringProperty()

    def update_status(self, status, blurb):
        if not -1 <= status <= 1:
            raise Exception('Invalid status.')
        if not len(blurb) <= 50:
            raise Exception('Blurb too long')
        self.status = status
        self.blurb = blurb
        now = dt.now()
        self.last_day = now.isoweekday() % 7
        self.last_hour = now.hour
        self.put()

    def schedule_status(self, day, hour, status, blurb):
        if not 0 <= day < 7:
            raise Exception('Invalid day.')
        if not 0 <= hour < 24:
            raise Exception('Invalid hour.')
        if not -1 <= status <= 1:
            raise Exception('Invalid status.')
        if not len(blurb) <= 50:
            raise Exception('Blurb too long')
        self.schedule[day][hour] = {
            'status': status,
            'blurb': blurb
        }
        self.put()

    def unschedule(self, day, hour):
        if not 0 <= day < 7:
            raise Exception('Invalid day.')
        if not 0 <= hour < 24:
            raise Exception('Invalid hour.')
        self.schedule[day][hour] = {
            'status': -2,
            'blurb': ''
        }
        self.put()

    def clear_schedule(self):
        self.schedule = [[-2 for _ in range(24)] for _ in range(7)]
        self.put()

    def get_current_status(self):
        self.update_info()
        return {
            'status': self.status,
            'blurb': self.blurb
        }

    def update_info(self):
        now = dt.now()
        day = now.isoweekday() % 7
        hour = now.hour
        info = self.get_status_at(day, hour)
        self.status = info['status']
        self.blurb = info['blurb']
        self.last_day = day
        self.last_hour = hour
        self.put()

    def get_status_at(self, day, hour):
        now = dt.now()
        if day == self.last_day and hour == self.last_hour:
            return {
                'status': self.status,
                'blurb': self.blurb
            }
        cur_day = day
        cur_hour = hour
        while cur_day != self.last_day and cur_hour != self.last_hour:
            if self.schedule[cur_day][cur_hour]['status'] != -2:
                return {
                    'status': self.schedule[cur_day][cur_hour]['status'],
                    'blurb': self.schedule[cur_day][cur_hour]['blurb']
                }
            cur_hour -= 1
            if cur_hour < 0:
                cur_hour %= 24
                cur_day = (cur_day - 1) % 7
        return {
            'status': self.status,
            'blurb': self.blurb
        }

    @classmethod
    def make_new(cls):
        sched = Schedule()
        sched.schedule = [[{'status':-2, 'blurb':''} for _ in range(24)] for _ in range(7)]
        sched.update_status(0, "I'm new here!")
        sched.put()
        return sched