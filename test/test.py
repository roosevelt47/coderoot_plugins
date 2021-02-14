import discord
from discord.ext import commands


class social(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def socials(self, ctx):
        embed = discord.Embed(
            title="**R&D Server**\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬",
            description="**Discord: **\n• We are following the ranking system of our affiliated server, which is R & D Giveaways. Just chat in R & D Giveaways server to LEVEL UP.
            If you are level 3 or 10 on that server, please send a DM to @ DM to ask for help!

            Ranks with Benefits
            @ 𝕷𝖊𝖛𝖊𝖑 3: Users can gain access to platforms such as Grammarly Business, QuillBot and Canva Pro
            @ 𝕷𝖊𝖛𝖊𝖑 10: Users can gain access to Spotify Premium
            @ 𝕷𝖊𝖛𝖊𝖑 30: Users can gain access to Netflix and Disney +

            Future roles and platforms will be distributed. Stay tuned to know more about upcoming updates!",
            color=0xee3463,
        )
        embed.set_footer(text="Management Team",
                         icon_url="https://cdn.discordapp.com/icons/768497538839871519/a_48fd1abc638cf92fad8a8fb09c1ee04f.gif?size=1024")
        await ctx.send(embed=embed)
        await ctx.send("discord.gg/FvmgmyDDRn")


def setup(bot):
    bot.add_cog(social(bot))
