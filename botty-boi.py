import discord
from discord.ext import commands

#token del bot
bot_token = 'NjY0ODIzOTEyMDIxODg0OTQ4.Xhcr6A.6pq18K6iAbCjdXlVGFCsdLlkkpc'

bot = commands.Bot(command_prefix='!')


@bot.command()
async def bot_help(ctx):
    await ctx.send("usa !figurine <numero figurina> per ottenere l' immagine della figurina corrispondente")

@bot.command()
async def figurine(ctx, arg):
    if len(arg) == 0:
        channel = bot.get_channel(664778731654479882)
        await channel.send("fuck you")
    else:
        image = arg + ".jpg"
        channel = bot.get_channel(664778731654479882)
        await channel.send(file=discord.File(image))

@bot.event
async def on_ready():
    print('Ready!')

bot.run(bot_token)