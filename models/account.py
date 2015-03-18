import webapp2

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
