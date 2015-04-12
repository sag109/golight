import webapp2
import datetime

from google.appengine.api import users
from google.appengine.ext import ndb

class GroupMembers(ndb.Model):
    blurb = ndb.StringProperty()
    status = ndb.IntegerProperty()
    group_key = ndb.KeyProperty() #why do we use this here?
    name = ndb.StringProperty()
    admin = ndb.BooleanProperty()
    user_info_key = ndb.KeyProperty()

    #schedule data
    schedule = ndb.JsonProperty()
    last_update_day = ndb.IntegerProperty()
    last_update_hour = ndb.IntegerProperty()

    def update_blurb(self, blurb):
        assert isinstance(blurb, str)
        if not 0 <= len(blurb) <= 50:
            raise Exception('Blurb length must be between 0 and 50 chars.')
        self.blurb = blurb
        now = datetime.now()
        self.last_update_day = now.isoweekday() % 7
        self.last_update_hour = now.hour
        self.key.put()

    def update_status(self, status):
        assert isinstance(status, int)
        if not -2 <= status < 2:
            raise Exception('Invalid status value.')
        now = datetime.now()
        self.last_update_day = now.isoweekday() % 7
        self.last_update_hour = now.hour
        self.key.put()


    def status_at(self, day, hour):
        assert isinstance(day, int)
        assert isinstance(hour, int)
        if not 0 <= day < 7:
            raise Exception('Invalid day.')
        if not 0 <= hour < 24:
            raise Exception('Invalid hour.')
        if self.last_update_hour == hour and self.last_update_day == day:
            return self.status
        cur_day = day
        cur_hr = hour - 1
        while not (self.last_update_hour == cur_hr and self.last_update_day == cur_day):
            if self.schedule[cur_day][cur_hr] != -2:
                return self.schedule[cur_day][cur_hr]
            cur_hr -= 1
            if cur_hr < 0:
                cur_day = (cur_day - 1) % 7
                cur_hr %= 23
        return self.status

    def clear_schedule(self):
        self.schedule = [[-2 for _ in range(24)] for _ in range(7)]
        self.key.put()

    def clear_schedule_at(self, day, hour):
        assert isinstance(day, int)
        assert isinstance(hour, int)
        if not 0 <= day < 7:
            raise Exception('Invalid day.')
        if not 0 <= hour < 24:
            raise Exception('Invalid hour.')
        self.schedule[day][hour] = -2
        self.key.put()

    def schedule_status(self, status, day, hour):
        assert isinstance(status, int)
        assert isinstance(day, int)
        assert isinstance(hour, int)
        if not -2 < status < 2:
            raise Exception('Invalid status value.')
        if not 0 <= day <= 6:
            raise Exception('Invalid day value.')
        if not 0 <= hour <= 23:
            raise Exception('Invalid hour value.')
        self.schedule[day][hour] = status

    def clean_delete(self):
        user = self.user_info_key.get()
        user.group_member_keys.remove(self.key)
        self.key.delete()

    @staticmethod
    def new(group, user, admin):
        assert isinstance(group, ndb.Key)
        assert isinstance(user, ndb.Key)
        assert isinstance(admin, bool)
        new_member = GroupMembers(blurb="I'm new here!",
                                  status=0,
                                  name=user.name,
                                  admin=admin,
                                  group_key=group.key,
                                  user_info_key=user.key)
        new_member.schedule = [[-2 for _ in range(24)] for _ in range(7)]
        now = datetime.now()
        new_member.last_update_day = now.isoweekday() % 7
        new_member.last_update_day = now.hour
        new_member.put()
        user.group_member_keys.append(new_member.key)
        user.key.put()
