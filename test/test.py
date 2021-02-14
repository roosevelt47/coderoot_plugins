import discord
from discord.ext import commands

class Test1(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def send_s(self, ctx):
        embed = discord.Embed(
            title="***R&D'S SOCIALS***\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
            description="<:instagram:724501733317017682> **Instagram:**\n• <https://www.instagram.com/paprika_bms/>\n\n<:youtube:663247076167122945> **YouTube:**\n• <https://www.youtube.com/channel/>\n\n<:twitter:724501698248441877> **Twitter:**\n• <https://twitter.com/>\n\n<:twitch:740634096446734366> **Twitch:**\n• <https://www.twitch.tv/>",
            color=0xee3463,
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Management Team", icon_url="https://cdn.discordapp.com/icons/768497538839871519/a_48fd1abc638cf92fad8a8fb09c1ee04f.gif?size=1024")
        await ctx.send(embed=embed)
        
        
def setup(bot):
    bot.add_cog(Test1(bot))
