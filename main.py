import discord
import random
from discord.ext import commands
import time
from discord.utils import get
from discord.ext.commands import Bot
import asyncio
import typing
from discord.ext.commands import has_permissions, CheckFailure
from discord.utils import get
import logging
import inspect
from PIL import Image
import json
import sys
import string
from translate import Translator
import requests
from discord import Webhook, RequestsWebhookAdapter, File
import urllib.request
from datetime import datetime
import ast
import aiohttp






#-----CONFIGURATION-----

custom_status = "ExiaRP" # Activity suffix
prefix = "/" # What symbol(s) will trigger a command
token = "" # Bot login authentication

#-----CONFIG ENDS HERE!-----

login = time.time()

intents = discord.Intents.default()

intents.members = True
client = commands.Bot(command_prefix = prefix, intents=intents)
client.remove_command("help")

@client.event
async def on_ready():
  await client.change_presence(status=discord.Status.online, activity=discord.Activity(name=custom_status, type=discord.ActivityType.playing))
  print("Bot is now online.")




@client.command(aliases=["commands","cmds"])
async def help(ctx):
  with open("commands.json","r") as f:
    commands = json.load(f)

  embed=discord.Embed(description="__**ExiaRP Commands**__\nCommands marked with `*` require you to `@mention` the user!\nBot made by **ExiaRP Development Team**.", color=0x004cff, timestamp=ctx.message.created_at)
  for key,value in commands.items():
    embed.add_field(name=f"{prefix}{key}", value=value, inline=False)
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/OymW-1cs4AGIKFjlLTx97h-bN6o24yyz20q2xcReuXM/%3Fsize%3D512/https/cdn.discordapp.com/icons/527702646585425921/5bd1257b95aa2788137c271c53eb4d7a.webp")
  await ctx.author.send(embed=embed)
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description="**I have messaged you a list of my commands!**", color=0x004cff))


@client.command()
async def info(ctx):
  embed=discord.Embed(title="ExiaRP Info", description="**ExiaRP-BOT** is an upgrade to your roleplay experience!\n\nI offer multiple commands to ensure roleplay stays simple and easy, all while doing so through realism.\nThis bot was created by the **ExiaRP Development Team**.\n\nRun `/help` to get a list of commands for the server!", color=0x004cff, timestamp=ctx.message.created_at)
  embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/OymW-1cs4AGIKFjlLTx97h-bN6o24yyz20q2xcReuXM/%3Fsize%3D512/https/cdn.discordapp.com/icons/527702646585425921/5bd1257b95aa2788137c271c53eb4d7a.webp")
  await ctx.author.send(embed=embed)
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description="**I have messaged you some bot info!**", color=0x004cff))


@client.command()
async def addcommand(ctx, cmd, *, desc):
  if ctx.author.id == 374289476492722187 or ctx.author.id == 318203855365996544:
    with open("commands.json","r") as f:
      commands = json.load(f)

    try:
      commands[str(cmd)] = desc
      await ctx.send(embed=discord.Embed(description="**Success!**", color=0x00FF00))
    except Exception as e:
      await ctx.send(embed=discord.Embed(description="**Failed!**", color=0xff0000))
      print(e)

    with open("commands.json","w") as f:
      json.dump(commands, f, indent = 4)

@client.command()
async def removecommand(ctx, cmd):
  if ctx.author.id == 374289476492722187 or ctx.author.id == 318203855365996544:
    with open("commands.json","r") as f:
      commands = json.load(f)

    try:
      commands.pop(str(cmd))
      await ctx.send(embed=discord.Embed(description="**Success!**", color=0x00FF00))
    except Exception as e:
      await ctx.send(embed=discord.Embed(description="**Failed!**", color=0xff0000))
      print(e)

    with open("commands.json","w") as f:
      json.dump(commands, f, indent = 4)

@client.command(aliases=["c"])
async def cuff(ctx, user:discord.Member):
  if ctx.message.guild != None:
    msg = await ctx.send(embed=discord.Embed(description=f"Applying cuffs...", color=0x004cff, timestamp=ctx.message.created_at))

    await asyncio.sleep(1)

    await msg.edit(embed=discord.Embed(description=f"**{ctx.author.display_name}** cuffed **{user.display_name}**!", color=0x004cff, timestamp=ctx.message.created_at))

@client.command(aliases=["uc"])
async def uncuff(ctx, user:discord.Member):
  if ctx.message.guild != None:
    msg = await ctx.send(embed=discord.Embed(description=f"Unapplying cuffs...", color=0x004cff, timestamp=ctx.message.created_at))

    await asyncio.sleep(1)

    await msg.edit(embed=discord.Embed(description=f"**{ctx.author.display_name}** uncuffed **{user.display_name}**!", color=0x004cff, timestamp=ctx.message.created_at))

@client.command(aliases=["read-id"])
async def readid(ctx, user:discord.Member):
  if ctx.message.guild != None:
    await ctx.send(user.mention,embed=discord.Embed(description=f"**{user.display_name}'s ID is being read by {ctx.author.display_name}!**\n*please state your name below*", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["g"])
async def grab(ctx, user:discord.Member):
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** has grabbed **{user.display_name}**!", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=[])
async def ping(ctx, user:discord.Member):
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}**'s location has been pinged to **{user.display_name}**!\n`You are now able to locate {ctx.author.display_name} using your pause screen!`", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=[])
async def search(ctx, user:discord.Member):
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** is searching **{user.display_name}**!\n`Please state everything currently on you.`", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=[])
async def tackle(ctx, user:discord.Member):
  if ctx.message.guild != None:
    msg = await ctx.send(embed=discord.Embed(description=f"**Tackling...**", color=0x004cff,timestamp=ctx.message.created_at))

    await asyncio.sleep(0.5)

    await msg.edit(embed=discord.Embed(description=f"**{ctx.author.display_name}** has tackled **{user.display_name}**!", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=[])
async def finish(ctx, user:discord.Member):
  if ctx.message.guild != None:
    msg = await ctx.send(embed=discord.Embed(description=f"Finishing **{user.display_name}** off...", color=0x004cff,timestamp=ctx.message.created_at))

    await asyncio.sleep(2)

    await msg.edit(embed=discord.Embed(description=f"**{ctx.author.display_name}** has finished off **{user.display_name}**! *(dead)*", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["vitals"])
async def check(ctx, user:discord.Member):
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** is checking **{user.display_name}**'s injuries and pulse!\n`State your injuries and pulse below!`", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["l"])
async def lock(ctx):
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** has locked their vehicle!", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["ul"])
async def unlock(ctx):
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** has unlocked their vehicle!", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["pd","pin-down"])
async def pindown(ctx, user:discord.Member):
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** has pinned **{user.display_name}** down!", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["rw","rack-weapon"])
async def rackweapon(ctx):
  if ctx.message.guild != None:
    await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** has racked their weapon.", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=[])
async def reload(ctx):
  if ctx.message.guild != None:
    msg = await ctx.send(embed=discord.Embed(description=f"*Reloading...*", color=0x004cff,timestamp=ctx.message.created_at))

    await asyncio.sleep(3)

    await msg.edit(embed=discord.Embed(description=f"**{ctx.author.display_name}** has reloaded their weapon.", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=[])
async def refuel(ctx):
  if ctx.message.guild != None:
    msg = await ctx.send(embed=discord.Embed(description=f"*Refueling...*", color=0x004cff,timestamp=ctx.message.created_at))

    await asyncio.sleep(5)

    await msg.edit(embed=discord.Embed(description=f"**{ctx.author.display_name}** has refueled.", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["eon","eng-on","engineon","engine-on"])
async def engon(ctx):
  if ctx.message.guild != None:
    msg = await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** is turning their engine on...", color=0x004cff,timestamp=ctx.message.created_at))

    await asyncio.sleep(1)

    await msg.edit(embed=discord.Embed(description=f"**{ctx.author.display_name}** has turned on their engine.", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["eoff","eng-off","engineoff","engine-off"])
async def engoff(ctx):
  if ctx.message.guild != None:
    msg = await ctx.send(embed=discord.Embed(description=f"**{ctx.author.display_name}** is turning their engine off...", color=0x004cff,timestamp=ctx.message.created_at))

    await asyncio.sleep(1)

    await msg.edit(embed=discord.Embed(description=f"**{ctx.author.display_name}** has turned off their engine.", color=0x004cff,timestamp=ctx.message.created_at))

@client.command(aliases=["tweet","twt"])
async def twotter(ctx,*,content):
  if ctx.message.guild != None:

    content = content.replace("anon","")
    content = content.replace("vpn","")

    await ctx.message.delete()

    if "vpn" in ctx.message.content:
      embed=discord.Embed(title="<:twitter:858110570087972884> TWOTTER (VPN)",description=f"{content}", color=0x1DA1F2,timestamp=ctx.message.created_at)
    else:
      embed=discord.Embed(title="<:twitter:858110570087972884> TWOTTER",description=f"{content}", color=0x1DA1F2,timestamp=ctx.message.created_at)


    if "anon" in ctx.message.content:
      embed.set_author(name=f"@<ANON>", icon_url="https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_1280.png")
    else:
      embed.set_author(name=f"@{ctx.author.display_name}", icon_url=ctx.author.avatar_url)
    await ctx.send(embed=embed)

@client.command(aliases=["call","text","txt"])
async def contact(ctx, user:discord.Member):
  if ctx.author == user:
    await ctx.send(embed=discord.Embed(description=f"You can't call yourself!", color=0x004cff,timestamp=ctx.message.created_at))
  if ctx.author != user:
    msg = await ctx.send(f"**<a:telephone:858107193656213534> Calling {user.display_name}...**")
    try:
      acceptCheck = await user.send(f"**<a:phone:858107193656213534> {ctx.author.display_name} is calling you. React with <:accept:858107173799198740> to accept or <:decline:858107161266618369> to decline.**")
      await acceptCheck.add_reaction("<:accept:858107173799198740>")
      await acceptCheck.add_reaction("<:decline:858107161266618369>")

      def acceptCheck(reaction, user2):
        return user2 == user

      acceptDecline, user = await client.wait_for("reaction_add", check=acceptCheck)

      def ctxCheck(message):
        return message.author == ctx.author and message.guild == None

      def uCheck(message):
        return message.author == user and message.guild == None

      if str(acceptDecline) == "<:decline:858107161266618369>": # declined
        await ctx.author.send(f"**`{user.display_name}` declined your call.**")
        await user.send(f"**You declined.**")
        await msg.edit(content=f"**<:<:decline:858107161266618369> {user.display_name} declined.**")
      elif str(acceptDecline) == "<:accept:858107173799198740>": # accepted
        await msg.edit(content=f"**<:accept:858107173799198740> `{user.display_name}` accepted.**")
        await ctx.author.send(f"**You are now on call with {user.display_name}! Say something or `end` at any time to hang up!**")
        await user.send(f"**You are now on call with {ctx.author.display_name}! Say `end` at any time to hang up!**")
        endCall = False
        while endCall == False:
          ctxMsg = await client.wait_for("message",check=ctxCheck)
          if ctxMsg.content.lower() == "end":
            endCall = True
            await user.send(f"**{ctx.author.display_name} ended the call.**")
            await ctx.author.send(f"**You ended the call.**")
          else:
            await user.send(f"**{ctx.author.display_name}:** {ctxMsg.content}")

          uMsg = await client.wait_for("message",check=uCheck)
          if uMsg.content.lower() == "end":
            endCall = True
            await ctx.author.send(f"**{user.display_name} ended the call.**")
            await user.send(f"**You ended the call.**")
          else:
            await ctx.author.send(f"**{user.display_name}:** {uMsg.content}")
    except:
      await msg.edit(content=f"**❌ {user.display_name} was not reachable.**")

client.run(token)
