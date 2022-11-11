import discord
from discord.ext import commands
from discord import app_commands
import sqlite3

class Register(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    async def register(self, interaction: discord.Interaction, email: str, first_name: str, last_name: str):
        """Register your name and email with the NPSS Hack Club"""
        registrants = open('registrations.csv', 'a')
        if not email.endswith('@pdsb.net'):
            await interaction.response.send_message('Please use your school email.')
            return
        if len(email) != 15:
            await interaction.response.send_message('Please use a valid school email')
            return
        registrants.write(f"""{email}, {first_name}, {last_name}, {interaction.user.id}
""")
        registrants.close()
        await interaction.response.send_message(f'Thank you for registering!')

async def setup(client):
    await client.add_cog(Register(client))
