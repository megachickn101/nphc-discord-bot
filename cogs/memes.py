import discord
from discord.ext import commands
from discord import app_commands
import asyncpraw
import random
import xkcd

reddit = asyncpraw.Reddit(client_id='4fqBCl9I0Cc2KQ',
					client_secret='xS0C9f2q3P3hnSeUJZnUlsYHPKg',
					user_agent='A meme scraper For Another Bot (by /u/megachickn)')

class Memes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @app_commands.command()
    async def comic(self, interaction: discord.Interaction):
        """Get a comic from xkcd"""
        comic = xkcd.random_comic()
        embed = discord.Embed(title=comic[1], colour=discord.Color.blue(), url= 'https://www.xkcd.com')
        embed.set_footer(text='XKCD Comic')
        embed.set_image(url=comic[0])
        await interaction.response.send_message(embed=embed)

    @app_commands.command()
    async def memes(self, interaction: discord.Interaction):
        """Get a meme from r/programmingmemes or r/ProgrammerHumor"""
        subreddit = await reddit.subreddit('programmingmemes+ProgrammerHumor')
        meme = random.choice([memes async for memes in subreddit.hot(limit=100)])
        embed = discord.Embed(title=meme.title, colour=discord.Color.blue(), url= 'https://reddit.com')
        embed.set_image(url=meme.url)
        await interaction.response.send_message(embed=embed)
        return

async def setup(client):
    await client.add_cog(Memes(client))
