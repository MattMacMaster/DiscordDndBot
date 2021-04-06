![GitHub last commit](https://img.shields.io/github/last-commit/MattMacMaster/DiscordDndBot)

# DiscordDndBot
A personal Project dreamt up from transitioning from hosting DnD in person to online
over discord to help with the difficulties of online.This project uses two major api's to assist in the development of this project.You can add the bot [here](https://discord.com/api/oauth2/authorize?client_id=769265469306830898&permissions=0&scope=bot) to a discord server of your own.

# Discordpy
This library allows the bot to work with discords toolkits and allow the bot proper permissions when being added to anyones servers.

# D&D 5e API
I utilized this public [API](http://www.dnd5eapi.co/) for the minimum core game data that the bot could use.

# Technology Summary
Windows 10, VSCode, Python - Version(3.8.2), [Discordpy](https://discordpy.readthedocs.io/en/latest/api.html), and the [5e API](http://www.dnd5eapi.co/)

# Future Additions
- Add a did you mean clause on failed requests
- Further Error Handling
- Add Command Cooldowns
- Make codebase less monolithic and more reuseable
- Add Homebrew manager/handler with local database?
- Unit Testing
- Hardcore Code thinning and optimizing
- Running on its own  personal server for 24/7 uptime


# Known Issues
Due to inconsistencies from the data source some entries break the bot - Noting known ones below


# Local Setup
Ensure that Python is enabled on your machine, and the needed python dependencies which should be built into python 3
except for the discord library which can be installed so.
```
python3 -m pip install -U discord.py
```


There is a env file utilized in the bot, which can be made in the root directory.
The discord token credential can be found [here](https://discord.com/developers/docs/intro) on applications and General information.

```
# .env
DISCORD_TOKEN= {Discord Token}
DISCORD_GUILD= {Server Name}
```
Then simply run in your respective command line
```
python DnDBot.py
```
