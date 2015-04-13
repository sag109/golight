import json
import logging

def json_reply(function):
    return json.dumps(function())
    # try:
    #     response = json.dumps(function())
    # except Exception as e:
    #     response = json.dumps({
    #         'error': e.message + '\n'
    #     })
    #     raise e
    # return response

success = {
    'success': True
}