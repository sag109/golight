import webapp2
import datetime

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import mail

class user_info(ndb.Model):
    # the owner]
    user = ndb.UserProperty()

    # the person's username, between 1 and 20 chars
    name = ndb.StringProperty()

    # the person's email. nabbed from google through oauth
    email = ndb.StringProperty()

    #keys of friends
    friend_list = ndb.KeyProperty(repeated=True)

    #dict mapping the key of the user the request is from to the request message
    friend_requests = ndb.JsonProperty()
    #from the group to the group's description
    group_invites = ndb.JsonProperty()

    # -1, 0, or 1, being unavailable, tentative, or available respectively
    status = ndb.IntegerProperty()

    # the user's status message, between 1 and 50 chars (inclusive)
    message = ndb.StringProperty()

    # a list of the groups the user is in
    group_member_keys = ndb.KeyProperty(repeated=True)

    #a list of lists, with the first int being day of week (0-6) and second being hour (0-23)
    schedule = ndb.JsonProperty()

    #two ints, representing the last time the current status was updated
    last_update_day = ndb.IntegerProperty()
    last_update_hour = ndb.IntegerProperty()

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
        self.key.put()

    def clear_schedule(self):
        self.schedule = [[-2 for _ in range(24)] for _ in range(7)]
        self.key.put()

    def clear_schedule_at(self, day, hour):
        assert isinstance(day, int)
        assert isinstance(hour, int)
        if not 0 <= day <= 6:
            raise Exception('Invalid day value.')
        if not 0 <= hour <= 23:
            raise Exception('Invalid hour value.')
        self.schedule[day][hour] = -2
        self.key.put()

    def status_at(self, day, hour):
        assert isinstance(day, int)
        assert isinstance(hour, int)
        if not 0 <= day <= 6:
            raise Exception('Invalid day value.')
        if not 0 <= hour <= 23:
            raise Exception('Invalid hour value.')
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

    def update_status(self, status):
        assert isinstance(status, int)
        if not -2 < status < 2:
            raise Exception('Invalid status value.')
        self.status = status
        now = datetime.now()
        self.last_update_day = now.isoweekday() % 7
        self.last_update_hour = now.hour
        self.key.put()

    def update_blurb(self, blurb):
        assert isinstance(blurb, str)
        if not 0 <= len(blurb) <= 50:
            raise Exception('Invalid blurb length. Must be between 1 and 50 chars.')
        self.message = blurb
        self.key.put()

    def update_name(self, name):
        assert isinstance(name, str)
        if not name:
            raise Exception('Name not specified.')
        if not 0 < len(name) <= 20:
            raise Exception('Invalid name length. Must be between 1 and 20 chars.')
        self.name = name
        for member_key in self.group_member_keys:
            member = member_key.get()
            member.name = name
            member.put()
        self.key.put()


    def add_friend(self, friend_user):
        assert(isinstance(friend_user, ndb.Key))
        if not friend_user:
            raise Exception('No friend specified to add.')
        if friend_user in self.friend_list:
            raise Exception('User already in friends list.')
        if friend_user in self.friend_requests:
            self.friend_list.append(friend_user)
            self.remove_friend_request(friend_user)
        self.key.put()

    def delete_friend(self, friend_user):
        assert isinstance(friend_user, ndb.Key)
        if not friend_user:
            raise Exception('No friend specified for deletion.')
        if not friend_user in self.friend_list:
            raise Exception('Friend to delete not in friends list.')
        self.friend_list.remove(friend_user)
        friend = friend_user.get()
        friend.friend_list.remove(self.key)
        friend.key.put()
        self.key.put()

    def add_friend_request(self, request_user, message):
        assert isinstance(request_user, ndb.key)
        assert isinstance(message, str)
        if request_user in self.friend_requests:
            raise Exception('Pending request exists.')
        self.friend_requests[request_user] = message
        self.key.put()

    def remove_friend_request(self, request_user):
        assert(isinstance(request_user, ndb.Key))
        if not request_user in self.friend_requests:
            raise Exception('No request from this person to delete.')
        del self.friend_requests[request_user]
        self.key.put()

    @staticmethod
    def get_by_email(email):
        return user_info.query(user_info.email == email).get()

    @staticmethod
    def get_user_account():
        user = users.get_current_user()
        account = user_info.get_by_email(user.email())
        if not account:
            account = user_info(email=user.email(), name=user.nickname())
            account.userid = user.id
            account.update_status(0)
            account.user = user
            account.add_friend(account.key)
            account.schedule = [[-2 for _ in range(24)] for _ in range(7)]
            account.message = "I'm new here!"
            account.friend_requests = {}
            account.group_invites = {}
            mail.send_mail("golightapp@gmail.com", account.email, 'Welcome to Golight', """
                   ____________________
                  |\                   \      l____
                  | \___________________\     |\   \
                  | |                    |    |\l___\___
             [__]_[ |    Welcome to      |[\\]| |__|_\__\
            /\[__]\ |      Golight       |\[\\]\|. | |===\
            \ \[__]\[____________________] \[__]|__|..___]
             \/.-.\_______________________\/.-.\____\/.-.\
              ( @ )                        ( @ )  =  ( @ )
               `-'                          `-'       `-'
            """)
            account.put()
        return account
