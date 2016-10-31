import os
import time
from slackclient import SlackClient

# vroomba's ID
BOT_ID = os.environ.get("BOT_ID")

# constants
AT_BOT = "<@" + BOT_ID + ">"
COMMANDS = {
    'URBAN_SALUTATION': ' yo',
    'HELP_COMMAND': ' help',
    'SLASH_LIST': ' slash',
    'HELPFUL_LINKS': ' link'
}

# instantiate Slack client
slack_client = SlackClient(os.environ.get('SLACK_BOT_TOKEN'))

def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they are valid.
        If so, it acts on commands, if not, it asks for clarification.
    """
    response = "Not sure what you mean, human."
    print command + " " + channel

    if command.startswith(COMMANDS['URBAN_SALUTATION']):
        response = "Ayyyyy! :kylo:"
    elif command.startswith(COMMANDS['HELP_COMMAND']):
        response = "The only current commands are: *" + "*, *".join(COMMANDS.values()) + "*."
    elif command.startswith(COMMANDS['SLASH_LIST']):
        response = "Here's a list of official slash commands! https://get.slack.help/hc/en-us/articles/201259356-Slash-commands"
    elif command.startswith(COMMANDS['HELPFUL_LINKS']):
        response = "Here's a list of links associated with the VR Hackathon... tbd"


    slack_client.api_call("chat.postMessage", channel=channel, text=response,
                            as_user=True)

def parse_slack_output(slack_rtm_output):
    """
        This parsing function returns None unless a message is directed at the
        Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace *not* removed
                return output['text'].split(AT_BOT)[1].lower(), \
                output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1sec delay between reading output
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
