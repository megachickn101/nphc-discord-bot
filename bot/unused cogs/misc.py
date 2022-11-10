import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def creator(self, ctx):
        embed = discord.Embed(title='Created By megachickn101, a certified uninteresting idiot', colour=discord.Color.blue(), url= 'https://megachickn101.github.io')
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def invite(self, ctx):
        await ctx.send("https://discord.com/api/oauth2/authorize?client_id=955963073494151218&permissions=8&scope=bot")

    @commands.command()
    async def arbiter(self, ctx):
        arbiter = self.client.get_user(654010719079235585)
        try:
            await ctx.send(f"{arbiter.mention} is hella sus")
        except:
            await ctx.send("arbiter is hella sus")

    @commands.command()
    async def github(self, ctx):
        await ctx.send("""That's right! NPBot is fully open source (so I'm not sus and my classmates accuse me of using the bot for malicious purposes. I swear to god guys, I'm not going to destroy the server, pinky promise)
        https://github.com/megachickn101/npbot""")

def setup(client):
    client.add_cog(Misc(client))
