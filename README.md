# definitely_not_a_discord_bot
Bot for discord written in Python

*To run locally, the files needed are bot.py and .env. 

- Set the environment variables to the particular ones of your discord server (token, guild name, bot id), set the channels you want to monitor/write on, and the text you want it to write. 
- Execute with 'python bot.py'

*To run constantly on the net without hiring a hosting service (need Repl.it and uptimerobot.com accounts), the files needed are bot.py and keep_alive.py

- Upload bot.py and keep_alive.py on a Repl.it (the code on bot.py loading the environment variables would have to be deleted, since Repl.it has its own environment variables management system).
- Start the bot.
- A new window with a url would appear. Copy the url.
- Create a monitor on uptimerobot, and paste the copied url. Set the time to an interval lower than 30 minutes (the bot would go to sleep after 30 minutes of inactivity).
- Start the monitor

*For more information: 
- https://realpython.com/how-to-make-a-discord-bot-python/#connecting-a-bot
- https://www.freecodecamp.org/news/create-a-discord-bot-with-python/
