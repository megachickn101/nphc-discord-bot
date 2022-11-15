import discord
from discord.ext import commands
import pysourcebin as psb

class Sourcebin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith('```') and message.content.endswith('```'):
            code = message.content[3:][:-3]
            url = psb.create(f'{message.author.name}', code, title='NPHC Code Snippet', description=f'Generated for {message.author.name}')
            await message.delete()
            await message.channel.send(f"{message.author.mention}, You code was automatically uploaded to {url}. Please use a code sharing service when possible. :)")
        await self.client.process_commands(message)

async def setup(client):
    await client.add_cog(Sourcebin(client))
