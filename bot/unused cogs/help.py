import discord
from discord.ext import commands

class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        embed = discord.Embed(title='Help', description="The bot is lowkey basic, I'm working on features ok? :'( I'm trying my best here. | Prefix >>", colour=discord.Color.blue(), url='https://www.megachickn101.github.io/')
        embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
        embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url)

        embed.add_field(name='createschedule', value='Follow prompts and create a school schedule!', inline=False)
        embed.add_field(name='schedule <methodofdelivery:Optional>', value='Sends your created schedule to you. If you want it sent to your dms, add a space and "DM" after the command', inline=False)
        embed.add_field(name='whatschoolday', value='Tells you what school day it is today.', inline=False)
        embed.add_field(name='whatday', value="Tells you the today's day", inline=False)
        embed.add_field(name='arbiter', value="He's a bit of a sussy wussy baka", inline=False)
        embed.add_field(name='invite', value="Invite me!", inline=False)
        embed.add_field(name='ping', value='Ping me!', inline=False)
        embed.add_field(name='github', value='Get my discord repo', inline=False)
        embed.add_field(name='clear', value='For Mods Only!', inline=False)
        embed.add_field(name='kick', value='For Mods Only!', inline=False)
        embed.add_field(name='ban', value='For Mods Only!', inline=False)
        embed.add_field(name='unban', value='For Admins Only!', inline=False)
        embed.add_field(name='help', value='This command...', inline=False)
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Help(client))
