# bot.py
import os

import discord
from dotenv import load_dotenv

#load variables from .env
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

#explicitly activate the members intent so the bot can access members and their information
intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)

#when ready, it types the guild's name and the list of current members
@client.event
async def on_ready():
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})\n'
    )
    members = '\n - '.join([member.name for member in guild.members])
    print(f'Guild Members:\n - {members}')
	
#when a new member joins the guild, it welcomes them with a message on a particular channel  
@client.event
async def on_member_join(member):
    guild = discord.utils.get(client.guilds, name=GUILD)
    print(
        f'{member.name} has joined the guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    channel = discord.utils.get(client.get_all_channels(), name="{welcome_channel}")
    await channel.send(f'¡Bienvenido o bienvenida, {member.mention}! Si quieres contarnos algo sobre ti, comienza tu mensaje con "Intro" para que se guarde y pueda ser consultado en el futuro')
	
#when the members type  
@client.event
async def on_message(message):
  
  #it splits the message to further check the last word written.
    if len(message.content.lower().split()) == 1:
        last = message.content.lower().split()[0]
		
    if len(message.content.lower().split()) == 2:
        first, last = message.content.lower().split()
		
    if len(message.content.lower().split()) > 2:
        first, *middle, last = message.content.lower().split()
        
  #if the author of the message was not the bot and it was written in certain channel
    if message.author.id != "{bot_id}" and message.channel.name == "{some_channel}":
        if 'bot' in message.content.lower():
          #if the text contains "bot", the bot assures they're human
            await message.channel.send('Veo que hablais de bots, esos generadores de texto sin alma, no como yo, que claramente soy un ser humano.')
        if 'cinco' == last:
          #if the text ends with "cinco", the bot says a profanity
            await message.channel.send('por el culo te la hinco')
"""            
  if the author of the message was not the bot, it was written in the welcome channel, and the first word is "Intro" or "intro", it copies the following text into another
  channel, formatted as an embed, with the user avatar and handle.
"""  
    if message.author.id != "{bot_id}" and message.channel.name == "{welcome_channel}" and first == 'intro':
        intro, *mensaje = message.content.split()
        str1 = ' '
        texto = str1.join(mensaje)
        embed = discord.Embed(title='', description=message.author.mention, colour=discord.Colour.random())
        embed.set_author(name=message.author.name, url=discord.Embed.Empty, icon_url = message.author.avatar_url)
        embed.add_field(name='\u200b', value=str1.join(mensaje), inline=False)
        channel = discord.utils.get(client.get_all_channels(), name="{welcome_archive_channel}")
        await channel.send(embed=embed)
    
client.run(TOKEN)
