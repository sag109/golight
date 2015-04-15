import webapp2
from models.schedule import Schedule

from google.appengine.api import users
from google.appengine.ext import ndb
from google.appengine.api import mail

class user_info(ndb.Model):
    name = ndb.StringProperty()
    email = ndb.StringProperty()
    friend_list = ndb.StringProperty(repeated=True)
    status = ndb.IntegerProperty()
    availability = ndb.StringProperty()
    message = ndb.StringProperty()
    group_keys = ndb.KeyProperty(repeated=True)
    schedule = ndb.KeyProperty()

    def set_name(self, name):
        if not 0 < len(name) <= 20:
            raise Exception('Invalid name length.')
        for key in self.group_keys:
            group = key.get()
            member = group.get_member(self.email)
            member.name = name
            member.put()
        self.name = name
        self.put()

    @staticmethod
    def get_by_email(email):
        account_query = user_info.query(user_info.email == email)
        # Get executes the query and returns the first result, or None
        # if no results were generated.
        return account_query.get()

    @staticmethod
    def get_user_account():
        user = users.get_current_user()
        account = user_info.get_by_email(user.email())
        if not account:
            account = user_info(email=user.email(), name=user.nickname(), status=0, availability='0')
            account.friend_list = [user.email()]
            account.message = "I'm new here!"
<<<<<<< HEAD
            schedule = Schedule.make_new()
            schedule.update_status(0, "I'm new here!")
            account.schedule = schedule.key
            mail.send_mail("golightapp@gmail.com", account.email, 'Welcome to Golight', r"""
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
=======
            mail.send_mail("golightapp@gmail.com", account.email, 'Welcome to Golight', """

		Welcome to GoLight!

		www.golight-app.appspot.com

		Our site is dedicated to providing spontaneous availibilities to
		make it easier to coordinate activities and plans with your friends,
		coworkers, and family.

		We endevour to create a friendly and intuitive service that people
		will enjoy using. Please feel free to contact us with any questions,
		concerns, or feedback.

		Thanks for using GoLight!

		Kindest regards,
			The GoLight development team.

>>>>>>> 29495962b420cae1cbd450c84ac64718b6393288
            """)
            account.put()
        return account
