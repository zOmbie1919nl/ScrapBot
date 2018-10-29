import discord
import asyncio
import os
import aiohttp
import time
import random
from discord.ext import commands

#super scrapper and mod
class SuperCommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=344219235527950341) #super scrapper
        role2 = discord.utils.get(guild.roles, id=304833080563204096) #mod
        if ctx.channel.id == 490175018664460298 and role in ctx.author.roles or role2 in ctx.author.roles:
            return True
        return False


    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def ping(self, ctx):
        start = time.monotonic()
        msg = await ctx.send('Pinging....')
        heartbeat = ctx.bot.latency * 1000
        await msg.edit(content=f'Ping: {heartbeat:,.2f}ms')
    

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def memberinfo(self, ctx, member: discord.Member=None):
        colors = [0xc0ffee, 0xff00e4, 0x00ff17, 0xff0000]
        color = random.choice(colors)
        if member is None:
            member = ctx.author
            joindate = f"{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}"
            joined = f'{joindate}, {str(member.joined_at.time())[:-10]}'
            createddate = f"{member.created_at.day}-{member.created_at.month}-{member.created_at.year}"
            created = f"{createddate}, {str(member.created_at.time())[:-10]}"        
            em = discord.Embed(title=f"{member.mention}'s info", colour=color)
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name="Name:", value=f"{member.name}", inline=True) 
            em.add_field(name="Nickname:", value=member.nick, inline=True)
            em.add_field(name="User id", value=member.id, inline=False)
            em.add_field(name="Status:", value=member.status, inline=False)
            em.add_field(name="Created at:", value=created, inline=True)
            em.add_field(name="Joined at:", value=joined, inline=True)
            em.add_field(name="Roles:", value=', '.join(r.name if r.name == '@everyone' else r.mention for r in sorted(member.roles, key=str)), inline=False)
            await ctx.send(embed=em)
        else:
            joindate = f"{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}"
            joined = f'{joindate}, {str(member.joined_at.time())[:-10]}'
            createddate = f"{member.created_at.day}-{member.created_at.month}-{member.created_at.year}"
            created = f"{createddate}, {str(member.created_at.time())[:-10]}"        
            em = discord.Embed(title=f"{member.name}'s info", colour=color)
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name="Name:", value=f"{member.mention}", inline=True)
            em.add_field(name="Nickname:", value=member.nick, inline=True)
            em.add_field(name="User id:", value=member.id, inline=False)
            em.add_field(name="Joined at:", value=joined)
            em.add_field(name="Roles:", value=', '.join(r.name if r.name == '@everyone' else r.mention for r in sorted(member.roles, key=str)), inline=False)
            await ctx.send(embed=em)

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def serverinfo(self, ctx):
        guild = ctx.guild
        serverdate = f"{guild.created_at.day}-{guild.created_at.month}-{guild.created_at.year}"
        servercreated = f"{serverdate}, {str(guild.created_at.time())[:-10]}"
        em = discord.Embed(title=f'{guild.name}', colour=0xFF69B4)
        em.set_thumbnail(url=guild.icon_url)
        em.add_field(name="Server Name:", value=guild.name, inline=True)
        em.add_field(name="server Owner:", value=guild.owner, inline=True)
        em.add_field(name="Server Region:", value=guild.region, inline=True)
        em.add_field(name="Server created:", value=servercreated, inline=True)
        em.add_field(name="Members:", value=guild.member_count, inline=False)
        await ctx.send(embed=em)

    @commands.cooldown(1, 60, commands.BucketType.user)
    @commands.command()
    async def membercount(self, ctx):
        guild = ctx.guild
        await ctx.send(f"The membercount is currently:\n``{guild.member_count}``")

def setup(bot):
    bot.add_cog(SuperCommands(bot))
