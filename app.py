import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio

Client = discord.Client()
bot = commands.Bot(command_prefix="%")


@bot.event
async def on_ready():
    print("discord-stealth-mention-bot is ready")
    print("Client: " + bot.user.name)
    print("ID: " + bot.user.id)



@bot.event
async def on_message(message):
    
    async def spam_loop(message):
        while True:
            await bot.send_message(message.channel, "@everyone")
            await asyncio.sleep(3)


    loop = asyncio.get_event_loop()

    if message.content == ".":
        print("started spamming on: " + message.server.name)
        await bot.delete_message(message)
        await loop.run_forever(spam_loop(message))


    if message.content == ",":
        print("stopped spammin on " + message.server.name)
        await bot.delete_message(message)
        loop.stop()


    if message.author.id == bot.user.id:
        await bot.delete_message(message)





token_file = open('token.txt', 'r')
token = token_file.readline().replace('\n', '')
token_file.close()
bot.run(token)
