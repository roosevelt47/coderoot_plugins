import discord
from discord.ext import commands

class social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def socials(self, ctx):
        embed = discord.Embed(
            title="**R&D Server**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
            description="**Discord:**\n• to be removed",
            color=0xee3463,
            timestamp=ctx.message.created_at
        )
        embed.set_footer(text="Management Team", icon_url="https://cdn.discordapp.com/icons/768497538839871519/a_48fd1abc638cf92fad8a8fb09c1ee04f.gif?size=1024")
        await ctx.send(embed=embed)
        await ctx.send("discord.gg/FvmgmyDDRn")
        
        
def setup(bot):
    bot.add_cog(social(bot))
