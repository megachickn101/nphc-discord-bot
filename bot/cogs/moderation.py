import discord
from discord.ext import commands
from discord import app_commands

class Moderation(commands.Cog):
    swear_words = str(open('swear_words.txt', 'r').read())
    swear_words = swear_words.split(''',
''')
    swear_words.pop()

    def __init__(self, client):
        self.client = client 

    @commands.Cog.listener()
    async def on_message(self, message):
        for i in range(len(self.swear_words)):
            if self.swear_words[i] in message.content.lower():
                await message.delete()
                print(f'{message.author.name} said {self.swear_words[i]}.')

        await self.client.process_commands(message)

    @app_commands.command()
    async def kick(self, interaction: discord.Interation, member: discord.Member):
        pass

async def setup(client):
    await client.add_cog(Moderation(client))
