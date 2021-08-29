import discord
from discord.ext import commands
from utils import *
from funtions import *
import youtube_dl
import os

intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
Bot = commands.Bot("..", intents=intents)
game = Game()


@Bot.event
async def on_ready():
    print("Selamun aleyküm")


@Bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='genel')
    await channel.send(f"{member} aramıza katıldı. Heş geldin!")
    print(f"{member} aramıza katıldı. Heş geldin!")


@Bot.event
async def on_member_remove(member):
    channel = discord.utils.get(member.guild.text_channels, name='genel')
    await channel.send(f"{member} aramızdan ayrıldı :(")
    print(f"{member} aramızdan ayrıldı :(")


@Bot.command()
async def selam(ctx):
    await ctx.send('Aleykümselam {}'.format(ctx.author.name))


@Bot.command()
async def clear(ctx, amount=3):
    await ctx.channel.purge(limit=amount)


@Bot.command()
async def kaccm(ctx, *args):
    print(args[0])
    await ctx.send(game.kaccm(args[0]))

@Bot.command()
async def kufret(ctx):
    await ctx.send(game.kufret())

 
Bot.run(token)
