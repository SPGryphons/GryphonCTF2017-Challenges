import discord
from discord.ext import commands
import aiohttp
import asyncio
import base64

class Seasons:
    """Seasons Commands"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def autumn(self, ctx):
        """Print autumn definition"""
        await self.bot.send_message(ctx.message.author, "Autumn is the year's last, loveliest smile. Find out more at autumniqa7dc3j4p.onion! Visit either with a Tor browser, or perhaps even onion.casa!")

async def greet_member(self, member):
    await t.bot.send_message(member.server, "Welcome " + member.name + " to GryphonCTF 2017.")

def setup(bot):
    global t
    bot.add_listener(greet_member, "on_member_join")
    t = Seasons(bot)
    bot.add_cog(t)
