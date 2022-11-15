import discord
from discord.ext import commands
from discord import app_commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    async def help(self, interaction: discord.Interaction):
        """Get command list"""
        embed = discord.Embed(title='Click Here For Command List', color=discord.Color.blue(), url='https://megachickn101.github.io/nphcdb-site/')
        await interaction.response.send_message(embed=embed)

    @app_commands.command()
    async def rules(self, interaction: discord.Interaction):
        """Get rules of the server"""
        embed = discord.Embed(title='Rules:', color=discord.Color.red(), url='https://discord.gg/hkZZEuEk4s')
        embed.set_footer(text='NPHC Discord Server')

        embed.add_field(name='#1 Adhere to Discord TOS', value='https://discord.com/terms', inline=False)
        embed.add_field(name='#2 No swearing / explicit content (18+)', value='This a school server. Be smart.', inline=False)
        embed.add_field(name='#3 No hate speech (racism, homophobia, etc)', value='This will not be tolerated. Be kind.', inline=False)
        embed.add_field(name='#4 Keep content relevant to the channel', value='Keeps the server organized.', inline=False)
        embed.add_field(name='#5 No harassment and/or abuse to any member', value='Remember, this is a school server.', inline=False)
        embed.add_field(name='#6 Do not repeatedly ping @everyone, @President, @Mentors, @Execs, etc', value='Try to keep pings spread out in 4 hour periods. We will respond when available.', inline=False)
        embed.add_field(name='#7 Respect everyone', value='Treat people respectfully and you will be treated the same.', inline=False)
        embed.add_field(name='#8 Change your nickname to your first name (/nick)', value='Allows us to know who you are irl and identify you.', inline=False)
        embed.add_field(name='#9 Have fun', value='This is a club, not a class.', inline=False)

        await interaction.response.send_message(embed=embed)

async def setup(client):
    await client.add_cog(Help(client))
