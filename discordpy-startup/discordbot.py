from discord.ext import commands
import os
import traceback
import random

bot = commands.Bot('$')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def split(ctx, num: int, *args):
    words = list(*args)
    namelist = random.sample(words, len(words))
    result = [namelist[i::num] for i in range(num)]
    await ctx.send(result)

bot.run(token)
