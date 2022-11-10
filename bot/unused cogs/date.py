import time
import discord
from discord.ext import commands, tasks


class SchoolDay(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        self.daycheck.start()
        await self.client.change_presence(activity=discord.Game(f'Today is day {open("day.txt", "r").read()}'))
        print('Day Check Is Online')

    @tasks.loop(hours=1)
    async def daycheck(self):
        current_time = time.localtime()
        if current_time[3] == 0:
            day = int(open("day.txt", "r").read())
            if day == 1:
                day = open("day.txt", "w")
                day.write("2")
                day.close()
            else:
                day = open("day.txt", "w")
                day.write("1")
                day.close()
        await self.client.change_presence(activity=discord.Game(f'Today is day {open("day.txt", "r").read()}'))

    @commands.command()
    async def whatschoolday(self, ctx):
        await ctx.send(f'Today is day {open("day.txt", "r").read()}')

    @commands.command()
    async def whatday(self, ctx):
        current_time = time.localtime()
        weekdays = {
        '0': 'Monday',
        '1': 'Tuesday',
        '2': 'Wednesday',
        '3': 'Thursday',
        '4': 'Friday',
        '5': 'Saturday',
        '6': 'Sunday'
        }
        await ctx.send(f'Today is {weekdays[str(current_time[6])]}')

def setup(client):
    client.add_cog(SchoolDay(client))
