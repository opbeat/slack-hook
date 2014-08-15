Opbeat to Slack hook
--------------

Uses the new Opbeat API hooks.

## Setup

Deploy to Heroku:

[![Deploy](https://www.herokucdn.com/deploy/button.png)](https://heroku.com/deploy)

Approximate instructions:

1. Create a Slack integration: https://slack.com/services/new/incoming-webhook.
1. Copy the unique URL.
1. Create a new heroku app (or press the big purple button above)
1. Set SLACK_URL environment variable: `heroku config:set SLACK_URL:<url>`
1. Set up a http hook for your organization on Opbeat.

