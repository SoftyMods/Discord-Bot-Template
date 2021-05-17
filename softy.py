import discord
import json
from discord.ext import commands

with open('config.json') as f:
    config = json.load(f)

token = config.get('token')
prefix = config.get('prefix')

intents = discord.Intents.all()
softy = commands.Bot(command_prefix=prefix)

@softy.event
async def on_command_error(ctx, error):
    pass

@softy.event
async def on_ready():
    print("Loaded")

softy.run(token, bot = True)
