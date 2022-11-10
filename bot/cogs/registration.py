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
        print(f'{email}: {first_name}: {last_name}')
        # Insert sql code

async def setup(client):
    await client.add_cog(Register(client))
