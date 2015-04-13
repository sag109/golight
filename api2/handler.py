import json
import logging

def json_reply(function):
    try:
        response = json.dumps(function())
    except Exception as e:
        response = json.dumps({
            'error': e.message
        })
        logging.error(e.message)
    return response

success = {
    'success': True
}