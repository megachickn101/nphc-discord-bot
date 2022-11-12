import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    async def help(self, interaction: discord.Interaction):
        """Get command list"""
        embed = discord.Embed(title='Click Here For Command List', color=discord.Color.blue(), url='http://nphcdiscord.ml/')
        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(Help(client))
