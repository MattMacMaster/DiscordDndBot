# DiscordDndBot
A personal Project dreamt up from transistioning from hosting DnD in person to online
over discord to help with the difficulties of online.This project uses two major api's to assist in the development of this project.You can add the bot [here](https://discord.com/api/oauth2/authorize?client_id=769265469306830898&permissions=0&scope=bot).

# Discordpy
I use this library as this projects goal is a bot that is available for use on discord and is publicly available for use to anyone with the ability to add it to their respective servers

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


# Local Setup
Ensure that Python is enabled on your machine

There is a env file utilized in the bot, which can be made in the root directory.
The discord token credential can be found [here](https://discord.com/developers/docs/intro) on appplications and General information.

```
# .env
DISCORD_TOKEN= {Discord Token}
DISCORD_GUILD= {Server Name}
```
Then simply run in your respective command line
```
python DnDBot.py
```