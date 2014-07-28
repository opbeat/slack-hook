Opbeat SLACK
--------------

Uses the new Opbeat api hooks.

## Setup

Approximate instructions:

1. Create a Slack integration: https://slack.com/services/new/incoming-webhook. Take a note of the unique url.
1. Create a new heroku app. Set SLACK_URL environment variable: `heroku config:set SLACK_URL:<url>`
1. `git push heroku master`
1. Set up a http hook for your organization on Opbeat.

