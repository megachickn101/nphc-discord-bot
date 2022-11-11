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
    @app_commands.checks.has_permissions(kick_members=True)
    async def kick(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        """Kicks specified used"""
        await member.kick(reason=reason)
        await interaction.response.send_message(f'Kicked {member.name}')

    @app_commands.command()
    @app_commands.checks.has_permissions(ban_members=True)
    async def ban(self, interaction: discord.Interaction, member: discord.Member, reason: str):
        await member.ban(reason=reason)
        await interaction.response.send_message(f'Banned {member.name}')

async def setup(client):
    await client.add_cog(Moderation(client))
