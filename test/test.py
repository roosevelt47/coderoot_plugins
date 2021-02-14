import discord
from discord.ext import commands


class social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def socials(self, ctx):
        embed = discord.Embed(
            title="**R&D Server**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
            description="""**Ranking System: **\n
            • We are following the ranking system of our affiliated server, which is R&D Giveaways. Just chat in R&D Giveaways server to LEVEL UP.
            **If you are level 3 or 10 on that server, please send a DM to <@795958277652480033>!**

            **Ranks with Benefits**
            <@&799207404046123038>: Users can gain access to platforms such as ***Private Grammarly Business***, ***QuillBot*** and ***Canva Pro***
            <@&799230600039890954>: Users can gain access to ***Spotify Premium***
            <@&799245176328552448>: Users can gain access to ***Netflix***, ***HBO MAX***, ***Disney +***

            ***Future roles and platforms will be distributed. Stay tuned to know more about upcoming updates!***
            ```IF YOU HAVE ANY QUESTIONS OR CONCERNS, JUST SEND A MESSAGE (DM) TO THIS BOT.```
            
            
            """,
            color=0xee3463
        )
        embed.set_footer(text="Management Team",
                         icon_url="https://cdn.discordapp.com/icons/768497538839871519/a_48fd1abc638cf92fad8a8fb09c1ee04f.gif?size=1024")
        await ctx.send(embed=embed)
        await ctx.send("Invite link: discord.gg/FvmgmyDDRn")


def setup(bot):
    bot.add_cog(social(bot))

