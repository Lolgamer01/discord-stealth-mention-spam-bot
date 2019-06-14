import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import os

Client = discord.Client()
bot = commands.Bot(command_prefix="%")


@bot.event
async def on_ready():
    print("discord-stealth-mention-bot is ready")
    print("Client: " + bot.user.name)
    print("ID: " + str(bot.user.id))



@bot.event
async def on_message(message):

    if message.content == ".":
        print("started spamming on: " + message.server.name)
        await bot.delete_message(message)
        while True:
            sent = await bot.send_message(message.channel, "@everyone")
            await bot.delete_message(sent)
            # await asyncio.sleep(0.1)


    # if message.author.id == bot.user.id:
    #     await bot.delete_message(message)





# token_file = open('token.txt', 'r')
# token = token_file.readline().replace('\n', '')
# token_file.close()
# bot.run(token)

bot.run(os.environ.get('DISCORDKEY'))
