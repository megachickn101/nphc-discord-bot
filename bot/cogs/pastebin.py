import discord
from discord.ext import commands

class Pastebin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.startswith("```") and message.content.endswith("```"):
            print("Code detected")
        else:
            print("No code detected")

async def setup(client):
    await client.add_cog(Pastebin(client))
