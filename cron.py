import webapp2
import models

from google.appengine.api import mail
from google.appengine.api import users
from models.account import user_info

class SendEmails(webapp2.RequestHandler):
  def get(self):
    users = user_info.query().fetch()
    for user in users:
        mail.send.mail("golightapp@gmail.com",user.email(),"Your Weekly GoLight Update","Sup fuckers!")

    
app = webapp2.WSGIApplication([
  ('/cronstuff/email', SendEmails)
])