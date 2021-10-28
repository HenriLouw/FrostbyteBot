import discord 
import requests
import json
from discord.ext import commands, tasks
from itertools import cycle
from battlemetrics import *

bot = commands.Bot(command_prefix = '!') 
status = cycle([server_player + '/' + server_max_players, 'Created by MrT1TAN#3244'])

@bot.event 
async def on_ready():
  change_status.start()
  print('Frostbyte Bot now online')

@tasks.loop(seconds=15)
async def change_status():
  await bot.change_presence(activity=discord.Game(next(status)))

@bot.command()
@commands.has_role('Server Dev')
async def testing(ctx):
  channel = bot.get_channel(730113369075613748)
  await channel.send('Testing permisions')

@bot.command(aliases=["serverinfo"])
async def server(ctx):
    await ctx.send("Getting Commands!", delete_after=3.0)
    embed = discord.Embed(
        title="2x FrostbyteNetwork Server Info",
        description="All available info about the server.",
        colour=discord.Colour.teal(),
    )

    embed.set_footer(
        text="Website: https://www.frostbyte.network/ | Twitter: @FrostByteZA "
    )
    embed.set_thumbnail(url="https://imgur.com/KDFmLbU.png")
    embed.add_field(
        name="**__Server Name:__**",
        value="2x FrostbyteNetwork",
        inline=False,
    )
    embed.add_field(
        name="**__Server IP:__**",
        value='connect ' + server_ip,
        inline=False,
    )
    embed.add_field(
        name="**__Players Online:__**",
        value=server_player + '/' + server_max_players,
        inline=False,
    )
    embed.add_field(
        name="**__Average Server FPS:__**",
        value=server_fps,
        inline=False,
    )

    await ctx.send(embed=embed)

@bot.command(aliases=["commands"])
async def c(ctx):
    await ctx.send("Getting Commands!", delete_after=3.0)
    embed = discord.Embed(
        title="Commands",
        description="All Available Commands.",
        colour=discord.Colour.teal(),
    )

    embed.set_footer(
        text="Website: https://www.frostbyte.network/ | Twitter: @FrostByteZA "
    )
    embed.set_thumbnail(url="https://imgur.com/KDFmLbU.png")
    embed.add_field(
        name="**__!server / serverinfo__**",
        value="Shows All available info about the server",
        inline=False,
    )

    await ctx.send(embed=embed)

bot.run('ODc5MDM5MTk0MDQ2MDIxNjMy.YSJ7Cw.BXtasLvvT-zS3ppGmMDlZFaTY00')



