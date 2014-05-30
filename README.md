Opbeat SLACK
--------------

Uses the new unreleased api hooks.

## Setup

Approximate instructions:

1. Create a Slack integration: https://<your-org>.slack.com/services/new/incoming-webhook. Take a note of the unique url.
1. Create a new heroku app. Set SLACK_URL environment variable: `heroku config:set SLACK_URL:<url>`
1. `git push heroku master`
1. Ask someone at Opbeat to set up a http hook for you, send them your heroku app url.

