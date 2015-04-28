Opbeat to Slack hook
--------------

Receive notifications from Opbeat in your Slack channels.
(Uses the new Opbeat API hooks.)

**Note**: Opbeat now has [native Slack integration](https://opbeat.com/docs/articles/how-to-set-up-slack-integration/). The method explained below will continue to work.

## Setup

It is really simple to set up with a few clicks. Follow these steps:

1. Create a <a href="https://slack.com/services/new/incoming-webhook" target="_blank">new Slack integration</a> for a channel and copy the unique URL.
    
    <small>Screenshot:</small>
    <img src="http://cl.ly/image/3O1O3r11261e/slack-hookurl.png" title="Screenshot">

1. Press this button to create a new Heroku app:

    <a href="https://heroku.com/deploy" target="_blank">
        <img src="https://www.herokucdn.com/deploy/button.png" alt="Deploy">
    </a>

1. Paste the unique URL into the `SLACK_URL` field and deploy the app:
    
    <small>Screenshot:</small><br>
    <img src="http://cl.ly/image/0X1o031P1F3c/slack-deployapp.png" title="Screenshot">

1. After deployment, click **"View it"** to open the new app and copy the hook url.
    
    <small>Screenshot:</small><br>
    <img src="http://cl.ly/image/2M1Y1w0S2O3q/slack-viewapp.png" title="Screenshot">

1. Go to `https://opbeat.com/<yourorg>/settings/` and enter the hook url:
    
    <small>Screenshot:</small><br>
    <img src="http://cl.ly/image/3k3j2q263K3M/slack-configurehook.png" title="Screenshot">

    **Note:** The hook URL should like this:
    
    `https://random-app-name.herokuapp.com/new-activity`
    
    The `/new-activity` part is required for the hook to work.
    

Hooks are now configured. Post a comment on Opbeat to test it out!

