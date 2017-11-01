# [XtremBot](https://t.me/XtremBot)

This repository contains the source code of [@XtremBot](https://t.me/XtremBot),
a telegram bot that uses the [telegram-bot-framework](https://github.com/alvarogzp/telegram-bot-framework).

Initially, the telegram-bot-framework repository served also as a hosting for XtremBot, as it was the only bot using the framework.

So, this repository has been created to split the bot specific code from the framework.

Currently, this repository only declares the telegram-bot-framework as a dependency and runs it (the [xtrem/manager.py](xtrem/manager.py) is a mere copy of telegram-bot-framework's [bot/manager.py](https://github.com/alvarogzp/telegram-bot-framework/blob/develop/bot/manager.py)).
For this reason, the version number here is the same as the telegram-bot-framework version that it uses.

In the future, new XtremBot features may be added here, and code specifc to XtremBot may be moved from telegram-bot-framework to this repository.

For configuration and other information, see the [telegram-bot-framework README file](https://github.com/alvarogzp/telegram-bot-framework).


## Developed by

- Alvaro Gutierrez Perez
  - alvarogzp@gmail.com
  - https://linkedin.com/in/alvarogzp
