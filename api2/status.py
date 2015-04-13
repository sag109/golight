import webapp2
import json
from api2 import handler
from google.appengine.api import users
from models.account import user_info

class Status(webapp2.RequestHandler):
    def get(self):
        response = handler.json_reply(self.get_status)
        self.response.out.write(response)

    def put(self):
        response = handler.json_reply(self.put_status)
        self.response.out.write(response)

    def get_status(self):
        user = user_info.get_user_account()
        if self.request.get('day') and self.request.get('hour'):
            return {
                'name': user.name,
                'blurb': user.message,
                'status': user.status_at(int(self.request.get('day')), int(self.request.get('hour')))
            }
        else:
            return {
                'name': user.name,
                'status': user.status,
                'blurb': user.message
            }

    def put_status(self):
        data = json.loads(self.request.body)
        user = user_info.get_user_account()
        if 'time' in data:
            user.schedule_status(data['status'], data['time']['day'], data['time']['hour'])
        else:
            user.update_blurb(str(data['blurb']))
            user.update_status(data['status'])
        return handler.success
