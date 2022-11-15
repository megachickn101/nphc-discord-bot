import discord
from discord.ext import commands
from discord import app_commands
import os

intents = discord.Intents.all()

class MyClient(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix='---', intents=intents)
    
    async def startup(self):
        await client.wait_until_ready()
        await client.tree.sync()
        print('Synced application commands')
        print(f'Connected')

    async def setup_hook(self):
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                await client.load_extension(f'cogs.{filename[:-3]}')
                print(f'Loaded {filename[:-3]}')
        self.loop.create_task(self.startup())

intents = discord.Intents.all()
client = MyClient()
client.run(str(open('token.txt', 'r').read()))
