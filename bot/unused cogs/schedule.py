import sqlite3
import discord
import asyncio
from discord.ext import commands

bot = 841503876762435584

class Schedule(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def createschedule(self, ctx):
        return

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == bot:
            return

        if message.content.startswith('>>createschedule'):
            await message.channel.send('Please answer the questions using your day 1 timetable and spen')
            await message.channel.send('What is your first class? (8:30AM - 9:50AM)')
            def is_correct(m):
                return m.author == message.author
            try:
                class1 = await self.client.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send("Looks like you took too long :(")
            await message.channel.send('What is your second class? (9:33AM - 11:08AM)')
            try:
                class2 = await self.client.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send("Looks like you took too long :(")
            await message.channel.send('What is your third class? (12:03PM - 1:18PM)')
            try:
                class3 = await self.client.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send("Looks like you took too long :(")
            await message.channel.send('What is your fourth class? (1:21PM - 2:36PM)')
            try:
                class4 = await self.client.wait_for('message', check=is_correct, timeout=5.0)
            except asyncio.TimeoutError:
                return await message.channel.send("Looks like you took too long :(")
            conn = sqlite3.connect('schedules.db')
            c = conn.cursor()
            c.execute("SELECT * FROM day_1 WHERE user_id=?", (message.author.id,))
            result = c.fetchone()
            if result != None:
                c.execute(f"DELETE FROM day_1 WHERE user_id={int(message.author.id)}")
                c.execute(f"DELETE FROM day_2 WHERE user_id={int(message.author.id)}")
            c.execute(("INSERT INTO day_1(user_id, class1, class2, class3, class4) VALUES(?,?,?,?,?)"), (message.author.id, class1.content, class2.content, class3.content, class4.content))
            c.execute(("INSERT INTO day_2(user_id, class1, class2, class3, class4) VALUES(?,?,?,?,?)"), (message.author.id, class2.content, class1.content, class4.content, class3.content))
            conn.commit()
            c.close()
            conn.close()
            await message.channel.send("Schedule Created! Use >>schedule to get your schedule for the day")

    @commands.command()
    async def schedule(self, ctx, method=None):
        day = int(open("day.txt", "r").read())
        conn = sqlite3.connect('schedules.db')
        c = conn.cursor()
        c.execute("SELECT * FROM day_1 WHERE user_id=?", (ctx.author.id,))
        result = c.fetchone()
        if result == None:
            await ctx.send(f"{ctx.author.mention} You don't have a schedule! Use >>createschedule to create one!")
            c.close()
            conn.close()
        else:
            if day == 1:
                c.execute("SELECT * FROM day_1 WHERE user_id=?", (ctx.author.id,))
                result = c.fetchone()
                embed = discord.Embed(title=f"{ctx.author}'s Schedule", description=f'Your schedule for day {day}', colour=discord.Color.blue(), url= 'https://www.github.com/megachickn101')
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

                embed.add_field(name='8:30 - 9:50:', value=result[1], inline=False)
                embed.add_field(name='9:53 - 11:08:', value=result[2], inline=False)
                embed.add_field(name='11:08 - 12:03:', value=result[3], inline=False)
                embed.add_field(name='1:21 - 2:36:', value=result[4], inline=False)
            else:
                c.execute("SELECT * FROM day_2 WHERE user_id=?", (ctx.author.id,))
                result = c.fetchone()
                embed = discord.Embed(title=f"{ctx.author}'s Schedule", description=f'Get your schedule for day {day}', colour=discord.Color.blue(), url= 'https://www.github.com/megachickn101')
                embed.set_author(name=self.client.user.name, icon_url=self.client.user.avatar_url)
                embed.set_footer(text=ctx.author.name, icon_url=ctx.author.avatar_url)

                embed.add_field(name='8:30 - 9:50:', value=result[1], inline=False)
                embed.add_field(name='9:53 - 11:08:', value=result[2], inline=False)
                embed.add_field(name='11:08 - 12:03:', value=result[3], inline=False)
                embed.add_field(name='1:21 - 2:36:', value=result[4], inline=False)
            c.close()
            conn.close()
            if method == "DM":
                await ctx.send("Check your DMs!")
                await ctx.author.send(embed=embed)
            else:
                await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Schedule(client))
