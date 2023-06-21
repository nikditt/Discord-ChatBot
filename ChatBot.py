####################################################################################
#██████╗ ██╗███████╗ ██████╗ ██████╗ ██████╗ ██████╗     ██████╗  ██████╗ ████████╗#
#██╔══██╗██║██╔════╝██╔════╝██╔═══██╗██╔══██╗██╔══██╗    ██╔══██╗██╔═══██╗╚══██╔══╝#
#██║  ██║██║███████╗██║     ██║   ██║██████╔╝██║  ██║    ██████╔╝██║   ██║   ██║   #
#██║  ██║██║╚════██║██║     ██║   ██║██╔══██╗██║  ██║    ██╔══██╗██║   ██║   ██║   #
#██████╔╝██║███████║╚██████╗╚██████╔╝██║  ██║██████╔╝    ██████╔╝╚██████╔╝   ██║   #
#╚═════╝ ╚═╝╚══════╝ ╚═════╝ ╚═════╝ ╚═╝  ╚═╝╚═════╝     ╚═════╝  ╚═════╝    ╚═╝   #                   
####################################################################################

"""
Prerequisites:
-       Python Extenstion in VSCode herunterladen
-       cmd: pip install discord (ggf. noch andere Module)

Hilfelinks:

https://discord.com/developers/applications/
https://discordpy.readthedocs.io/en/stable/index.html
https://www.reddit.com/prefs/apps

"""
###########################################
# Laden der benötigten Module und Befehle #
###########################################

import discord # Discord Modul
from discord.ext import commands # Befehle 
from discord.ext.commands.context import Context # Kontext
import json # Zur Anbindung von anderen APIs und der Nutzung von json-Dateien
import requests # APIs
import os
import random # würfel
#import praw


###########################################

#Reddit API-Zugangsdaten holen (https://www.reddit.com/prefs/apps)
#client_id = os.environ.get(reddit_client_id) 
#client_secret = os.environ.get(reddit_client_secret) 
#username = os.environ.get(reddit_username) 
#password = os.environ.get(reddit_password) 
#Erstellen eines Reddit-Objekts
#reddit = praw.Reddit(
#    client_id=client_id,
#    client_secret=client_secret,
#    username=username,
#    password=password,
#    user_agent='myBot/0.0.1' # Name und Version deines Bots
#)
#Abrufen von Posts aus einem Subreddit
#subreddit = reddit.subreddit('dankmemes') # Name des Subreddits
#for post in subreddit.new(limit=10): # Anzahl der zurückgegebenen Ergebnisse
#    print('Title:', post.title)
#    print('Score:', post.score)
#    print('Author:', post.author)
#    print('\n')


######################################################################################
# Erstellung des Intents-Objekt (Discord API) und Aktivierung der benötigten Intents #
# Intents sind für erweiterte Sicherheit und Berechtigungen notwendig                #
######################################################################################
intents = discord.Intents.default()
intents.members = True # aktiviert das Zugreifen auf Mitgliederlisten (privilegierte Intents)
intents.presences = True # aktiviert das Zugreifen auf die Anwesenheitsinformationen von Benutzern (privilegierte Intents)
intents.messages = True # aktiviert das Zugreifen auf Nachrichten in Textkanälen
intents.dm_messages = True

######################################################################################

# Erstelle einen Bot-Client und übergebe die Intents
bot = discord.Client(intents=intents)


##################################
# Deklaration globaler Variablen #
################################## 
# Globale Variablen müssen in Python nochmal innerhalb der einzelnen Funktionen deklariert werden
# also z.B. innerhalb von @bot.event!

TOKEN = '<Insert your API-Token here>'
##################################


###############################
# Funktionen des Discord-Bots #
###############################

# Lebenszeichen in der Kommandozeile beim Einschalten
 
@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))

# Status des Bots
@bot.event
async def on_ready():
    game = discord.Game("browsing the web")
    await bot.change_presence(status=discord.Status.online, activity=game)


# Nachrichten
#@bot.event
#async def on_message(msg):
# Platzhalterzeile für globale Variablen
#    if msg.author == bot.user:  # Ausnahme für den Bot (Endlosschleife)
#        return                  # bei Return wird die Funktion hier abgebrochen
#    print('[New Message]', msg.content) # in der Konsole/Terminal wird das ausgegeben
#    await msg.channel.send('Für Fortnite')
#    if "fortnite" in msg.content:
#        await msg.channel.send("Did someone say Fortnite?")

@bot.event
async def on_message(msg):
    if msg.author == bot.user:
        return
    print("Message received")
    if "fortnite" in msg.content.lower():
        print("Fortnite mentioned!")
        await msg.channel.send("Did someone say Fortnite?")
    else:
        await msg.channel.send('MessageOutput')



# Ergebnis: TestAberDerNameMussLangSein has connected to Discord!
@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(f'Hi {member.name}, welcome to my Discord server!')






# Münze

#bot = commands.Bot(command_prefix='!')

#@bot.command()
#async def coinflip(ctx):
    # choose a random outcome from a list of heads and tails
#    outcome = random.choice(['Kopf', 'Zahl'])
    # create an embed with the title and field
#    embed = discord.Embed(title='Münzwurf | ' + bot.user.name)
#    embed.add_field(name=ctx.author.name + ', die Münze ist auf ' + outcome + ' gelandet!', value='\u200b')
    # set the thumbnail to a picture of a coin depending on the outcome
#    if outcome == 'Kopf':
#        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/US_One_Cent_Rev.png/220px-US_One_Cent_Rev.png')
#    else:
#        embed.set_thumbnail(url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/US_One_Cent_Obv.png/220px-US_One_Cent_Obv.png')
    # send the embed to the channel
#    await ctx.send(embed=embed)


# Würfel

#client = commands.Bot(command_prefix='!')

#@client.command()
#async def rolldice(ctx, sides: int):
    # check if the number of sides is valid (positive and not too large)
#    if sides > 0 and sides <= 100:
        # choose a random number between 1 and the number of sides
#        result = random.randint(1, sides)
        # send a message with the result
#        await ctx.send(f'{ctx.author.name}, du hast eine {result} gewürfelt!')
#    else:
        # send an error message if the number of sides is invalid
#        await ctx.send('Bitte gib eine gültige Anzahl von Seiten an (zwischen 1 und 100).')






#@bot.event
#async def on_message(msg):
#        if 'meme' in msg.content: #if msg.content.startswith('meme'):   oder das, wenn es nur damit beginnen soll
#            response = requests.get("https://www.reddit.com/r/dankmemes/new.json?sort=new", headers={"User-Agent": "Mozilla/5.0"})
#            data = json.loads(response.text)
#        for post in data['data']['children'][:10]:
#            await msg.channel.send(post['data']['url'])

###############################
bot.run(TOKEN) # Einloggen des Bot-Clients