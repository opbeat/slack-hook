import os
import requests
from bottle import post, run, request
from bottle import jinja2_template as template

activity_template = """
<b>{{app['name']}}:</b> <{{html_url}}|{{title}}> - {{summary}}
"""

SLACK_URL = os.environ.get('SLACK_URL')
if not SLACK_URL:
    print("Missing environment variable SLACK_URL")


def send(self, data):
    rendered_activity = template(self.activity_template, **data)

    requests.post(SLACK_URL, {
        "payload": {"text": rendered_activity}
    })

@post('/new-activity')
def new_activity():
    data = request.json
    send(data)
    return "ok"


run(host='localhost', port=8080)
