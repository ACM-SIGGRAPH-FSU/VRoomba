# VRoomba
Cleans stuff up, like a Roomba. Except, virtually and not really in reality...


## Features
* Based on [Slack's RTM API](https://api.slack.com/rtm)
* Uses Python based [slackclient](https://github.com/slackhq/python-slackclient)
* No actual, current features
* Some sort of onboarding
* Some sort of guidance for new users outside of prelimenary info

## Installation
The only dependencies are the slackclient library which can be installed via the following command:
```
pip install slackclient
```
You'll also need to create environment variables for the Bot's API Token:
```
export SLACK_BOT_TOKEN='get this token from the maintainer'
```
Once you've installed the slackclient library and setup your environment variable, we can now get the Bot ID for VRoomba and be on our way!
```
python print_bot_id.py
```
Now we'll set an environment variable for the Bot's ID:
```
export BOT_ID='id returned by script'
```
And after running:
```
python vroomba.py
```
we should be able to listen for and respond to commands!

## Usage and Config
Using the bot is as easy as getting in it's @mentions with the first word after `@vroomba` being a command it understands... Configuring it will take a bit of coding.

Thankfully, we've made it pretty painless. Add a string to the `COMMANDS` dict (if you don't add your commands to the `COMMANDS` dict, the `help` command won't auto-magically list them). Then, within the `handle_command` function, add another case for the command starting with your new string. Change the response string or call a function (that should return a string value for the response).

Current commands look a bit like this:
```python
# constants
COMMANDS = {
    'SALUTATION': ' hey',
    'HELP_COMMAND': ' help'
}
...
def handle_command(command, channel):
...
    response = "Default reponse"
    if command.startswith(COMMANDS['SALUTATION']):
      response = "Hello! :smile:"
...
    slack_client.api_call("chat.postMessage", channel=channel, text=response,
                          as_user=True)
```
