#!/usr/bin/env python3

import asyncio
import random
import signal
import discord
from discord.ext import commands

from config import TOKEN, SERV_ID, SERVER_TYPE
from command_handler import CommandHandler

# init
bot = commands.Bot(command_prefix='!')
handler = CommandHandler(SERVER_TYPE)
loop = asyncio.get_event_loop()

# start action
async def setStatusMessage(msg: str):
    await bot.change_presence(activity=discord.Game(name=msg))
async def on_shutdown():
    if SERVER_TYPE != 'RPI':
        await setStatusMessage('server is OFF !')
    raise KeyboardInterrupt
async def on_startup():
    if SERVER_TYPE != 'RPI':
        bot.remove_command("help")
        await setStatusMessage('server is ON ✅ ✅ ✅')
        loop.add_signal_handler(
            signal.SIGTERM,
            lambda: asyncio.ensure_future(on_shutdown())
        )

@bot.event
async def on_ready():
    server = discord.utils.get(bot.guilds, id=SERV_ID)
    if server is None:
        return
    await on_startup()
    print(f'{bot.user} is connected to {server.name}(id: {server.id})')

@bot.event
async def on_error(event, *args, **kwargs):
    # Called when a function raises an exception
    print(f'{event} failed\n{args}\n{kwargs}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    await bot.process_commands(message)

@bot.command(name='minecraft', help='Commands: ping, count, list')
async def minecraft(ctx, command: str):
    await handler.minecraft_command(ctx, command)

@bot.command(name='server', help='Command: ping, boot, poweroff')
async def server(ctx, command: str):
    await handler.server_command(ctx, command)


@minecraft.error
@server.error
async def dm_error(ctx, error):
    if SERVER_TYPE == 'RPI':
        await ctx.send(f':no_entry: This is not okay sir, {error}')

bot.run(TOKEN)
