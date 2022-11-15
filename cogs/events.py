import discord
from discord.ext import commands

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Bot Is Online')

    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f'Welcome {member.mention} to {guild.name}!'
            await guild.system_channel.send(message)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        guild = member.guild
        if guild.system_channel is not None:
            message = f'{member} left {guild.name}. Sad to see you go'
            await guild.system_channel.send(message)

async def setup(client):
    await client.add_cog(Events(client))
