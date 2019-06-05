# Sample Career Python Bot

Built off of Bot Framework v4 core bot sample.

This bot has been created using [Bot Framework](https://dev.botframework.com), it shows how to:

- Use [LUIS](https://www.luis.ai) to implement core AI capabilities
- Implement a multi-turn conversation using Dialogs
- Handle user interruptions for such things as `Help` or `Cancel`
- Prompt for and validate requests for information from the user

1. Create a LUIS app (you can start by importing the json file under the cognitiveModels folder). 
2. In LUIS, press TRAIN and then PUBLISH. Make a note of the app id, key and hostname (e.g. https://westus.api.cognitive.microsoft.com)
3. Update the config.py with the values from 2
4. Run the bot locally (python main.py)
5. Run the bot emulator and try it out (see below for details)

## Testing the bot using Bot Framework Emulator

[Bot Framework Emulator](https://github.com/microsoft/botframework-emulator) is a desktop application that allows bot developers to test and debug their bots on localhost or running remotely through a tunnel.

- Install the Bot Framework Emulator version 4.3.0 or greater from [here](https://github.com/Microsoft/BotFramework-Emulator/releases)

### Connect to the bot using Bot Framework Emulator

- Launch Bot Framework Emulator
- File -> Open Bot
- Enter a Bot URL of `http://localhost:3978/api/messages`