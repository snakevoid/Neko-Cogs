import discord
from discord.ext import commands
from random import choice as randchoice

class Fuck:
    """Display fuck you statements"""

    def __init__(self, bot):
        self.bot = bot
        self.fuck = ["Fuck you, {}. ~{}", "Fucking fuck off, {}. ~{}","Fuck off, {}. ~{}","Fuck This, {}. ~{}", "Fuck that, {}. ~{}","You are a fucking faggot, {}. ~{}","{}, Thou clay-brained guts, thou knotty-pated fool, thou whoreson obscene greasy tallow-catch! ~{}","Oh fuck off, just really fuck off you total dickface. Christ {}, you are fucking thick. ~{}","{}, why don't you go outside and play hide-and-go-fuck-yourself? ~{} ","Hey {}, what a fascinating story, in what chapter do you shut the fuck up?\n\nSincerly,\n{}","What you've just said is one of the most insanely idiotic things I have ever heard, {}. At no point in your rambling, incoherent response were you even close to anything that could be considered a rational thought. Everyone in this room is now dumber for having listened to it. I award you no points :name, and may God have mercy on your soul. ~{}"]

    @commands.command(pass_context=True)
    async def fuk(self, ctx, name):
        """Get fuck you statements"""
        user = ctx.message.author
        await self.bot.say("**" + randchoice(self.fuck).format(name, user) + "**")

def setup(bot):
    bot.add_cog(Fuck(bot))
