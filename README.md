Opbeat to Slack hook
--------------

Receive notifications from Opbeat in your Slack channels.
(Uses the new Opbeat API hooks.)

## Setup

1. Create a <a href="https://slack.com/services/new/incoming-webhook" target="_blank">new Slack integration</a> for a channel and copy the unique URL.

    ![SS](http://cl.ly/image/3O1O3r11261e/slack-hookurl.png)

1. Press this button to create a new Heroku app:

    <a href="https://heroku.com/deploy" target="_blank">
        <img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy">
    </a>

1. **(Optional)** Choose a name and region for your application.
1. Paste the unique URL into the `SLACK_URL` field and deploy the app:

    ![SS](http://cl.ly/image/0X1o031P1F3c/slack-deployapp.png)

1. After deployment click "View it" to open the new app:

    ![SS](http://cl.ly/image/2M1Y1w0S2O3q/slack-viewapp.png)

1. Copy the hook url.

1. Go to `https://opbeat.com/<yourorg>/settings/` and enter the hook url:

    ![SS](http://cl.ly/image/3k3j2q263K3M/slack-configurehook.png)

Hooks are now configured. Post a comment on Opbeat to test it out!

