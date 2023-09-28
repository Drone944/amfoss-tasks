import discord
import csv
import os
from datetime import date
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import scraper

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'We have logged in as {client.user}')
s1,a3,a4,b2,d = scraper.onStart()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!livescore'):
        await message.channel.send(s1)
        await message.channel.send(a3[0])
        await message.channel.send(a4)
        await message.channel.send(b2)
        await message.channel.send(d)
    if message.content.startswith('!csv'):
    	await message.channel.send("livescore", file=discord.File('livescore.csv'))
    if message.content.startswith('!help'):
    	await message.channel.send("!csv - get the csv file the livescores are stored in")
    	await message.channel.send("!livescore - get the live scores")

client.run(os.getenv('TOKEN'))