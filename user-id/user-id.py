import discord
from core import checks
from core.models import PermissionLevel
from discord.ext import commands


class userID(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.has_permissions(PermissionLevel.SUPPORTER)
    async def userid(self, ctx):
        thread = ctx.thread
        if thread == None:
            member = ctx.author
        else:
            member = thread.recipient
        await ctx.send(f"{member.mention}'s ID is {member.id}")


def setup(bot):
    bot.add_cog(userID(bot))
