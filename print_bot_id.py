import os
from slackclient import SlackClient

# globals for use throughout script
BOT_NAME = 'vroomba'
# this should be pulled from an environment variable, check readme for deets
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find the bot
        users = api_call.get('members')
        for user in users:
            if user.get('name') == BOT_NAME:
                print("Bot ID for " + user['name'] + " is " + user.get('id'))
            else:
                print("not " + BOT_NAME + ", hiding ID...")
