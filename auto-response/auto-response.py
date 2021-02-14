from discord.ext import commands


class AutoTrigger(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,message):
        if message.author.bot:
            return
        message_str = message.content.lower()
        message_list = message_str.split()
        if "hello" in message_list:
            await message.channel.send("Hey")
        elif "yo" in message_list:
            await message.channel.send("yo")
        elif "gm" in message_list:
            await message.channel.send("Good Morning")
        elif "gn" in message_list:
            await message.channel.send("Good Night")
        elif "good morning" in message_list:
            await message.channel.send("Good Morning !")
        elif "good night" in message_list:
            await message.channel.send("Good Night !")
        elif "hey" in message_list:
            await message.channel.send("Hello !")
        elif "sup" in message_list:
            await message.channel.send("Sup")
        elif "hi" in message_list:
            await message.channel.send("Hello!")


def setup(bot):
    bot.add_cog(AutoTrigger(bot))
