import webapp2
import json
from api2 import handler
from google.appengine.api import users
from models.account import user_info

class NameSettings(webapp2.RequestHandler):
    def put(self):
        response = handler.json_reply(self.put_name())
        self.response.out.write(response)

    def put_name(self):
        user = user_info.get_user_account()
        data = json.loads(self.request.body)
        user.update_name(data['name'])
        return handler.success
