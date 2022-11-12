import discord
from discord.ext import commands
from discord import app_commands
import sqlite3

class Register(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    async def register(self, interaction: discord.Interaction, email: str, first_name: str, last_name: str):
        """Register your name and email with the NPSS Hack Club & gain access to the server."""
        role_id = 956341649120829460
        for i in range(len(interaction.guild.get_member(interaction.user.id).roles)):
            if interaction.guild.get_member(interaction.user.id).roles[i].id == role_id:
                await interaction.response.send_message(f'You have already registered.')
                return
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
        await interaction.guild.get_member(interaction.user.id).add_roles(interaction.guild.get_role(role_id))

async def setup(client):
    await client.add_cog(Register(client))
