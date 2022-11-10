import discord
from discord.ext import commands
from discord import app_commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    async def ping(self, interaction: discord.Interaction):
        """Shows the latency of the bot (doesn't really matter tbh)"""
        await interaction.response.send_message(f'Ping: {round(self.client.latency * 1000)}ms')

async def setup(client):
    await client.add_cog(Ping(client))
