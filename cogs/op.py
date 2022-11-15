import discord
from discord.ext import commands
from discord import app_commands

def is_it_me(interaction: discord.Interaction) -> bool:
    return interaction.user.id == int(open("user_id.txt", "r").read())

class OP(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    @app_commands.check(is_it_me)
    async def shutdown(self, interaction: discord.Interaction):
        await interaction.response.send_message('Shutting down')
        await self.client.close()

    @app_commands.command()
    @app_commands.check(is_it_me)
    async def load(self, interaction: discord.Interaction, extension: str):
        try:
            await self.client.load_extension(f'cogs.{extension}')
            await interaction.response.send_message(f'Loaded {extension}')
            print(f'Loaded {extension}')
        except:
            await interaction.response.send_message(f'Failed to load {extension}')

    @app_commands.command()
    @app_commands.check(is_it_me)
    async def unload(self, interaction: discord.Interaction, extension: str):
        try:
            await self.client.unload_extension(f'cogs.{extension}')
            await interaction.response.send_message(f'Unloaded {extension}')
            print(f'Unloaded {extension}')            
        except:
            await interaction.response.send_message(f'Failed to unload {extension}')

    @app_commands.command()
    @app_commands.check(is_it_me)
    async def reload(self, interaction: discord.Interaction, extension: str):
        try:
            await self.client.unload_extension(f'cogs.{extension}')
            await self.client.load_extension(f'cogs.{extension}')
            await interaction.response.send_message(f'Reloaded {extension}')
            print(f'Reloaded {extension}')            
        except:
            await interaction.response.send_message(f'Failed to reload {extension}')

async def setup(client):
    await client.add_cog(OP(client))
