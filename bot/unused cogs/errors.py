import discord
from discord.ext import commands

class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            await ctx.send("Error: Invalid Command")
            print('Error: Invalid Command')

        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'Error: Missing Argument')
            print('Error: Missing Argument')

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f'Error: Insufficient Permissions')
            print('Error: Insufficient Permissions')

        else:
            raise error

def setup(client):
    client.add_cog(Errors(client))
