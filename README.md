Opbeat to Slack hook
--------------

Receive notifications from Opbeat in your Slack channels.
(Uses the new Opbeat API hooks.)

## Setup

Quick instructions:

1. Create a <a href="https://slack.com/services/new/incoming-webhook" target="_blank">new Slack integration</a>.
1. Copy the unique URL.
1. Press this button: 

    [![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

1. (Optional) Choose a name and region for your application
1. Paste the unique URL into the `SLACK_URL` field and click "Deploy"

1. Copy the URL of your new Heroku app

1. Go to `https://opbeat.com/<yourorg>/settings/` and enter the hook:

Hooks are now configured. Post a comment on Opbeat to test it out!

