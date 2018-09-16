import discord
import asyncio
import os
import aiohttp
import time
import json
import traceback
from discord.ext import commands

class Modcommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=304833080563204096)
        if role in ctx.auhtor.roles:
            return True
        return False

    @commands.command()
    async def clear(self, ctx, amount: int=None):
        if amount is None:
            await ctx.send('Please put in a value for me to clear!')
        else:
            clear = amount +1
            await ctx.channel.purge(limit=clear)
            await ctx.send(f'``{amount}`` message(s) has been cleared', delete_after = 5)

    @commands.command()
    async def userinfo(self, ctx, member: discord.Member=None):
        if member is None:
            member = ctx.author
            display = member.name
            discrim = member.discriminator
            name = f'{display}#{discrim}'
            joindate = f'{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}'
            joined = f'{joindate}, {str(member.joined_at.time())[:-10]}'
            createddate = f'{member.created_at.day}-{member.created_at.month}-{member.created_at.year}'
            created = f'{createddate}, {str(member.created_at.time())[:-10]}'
            em = discord.Embed(title='userinfo', colour=0xFF0000)
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Name:', value=name, inline=False)
            em.add_field(name='Nickname:', value=member.nick, inline=False)
            em.add_field(name='User id', value=member.id, inline=False)
            em.add_field(name='Status:', value=member.status, inline=False)
            em.add_field(name='Created at:', value=created, inline=False)
            em.add_field(name='Joined at:', value=joined, inline=False)
            em.add_field(name='Roles:', value='\n '.join(r.name if r.name == '@everyone' else r.mention for r in sorted(member.roles, key=str)), inline=False)
            return await ctx.send(embed=em)
        else:
            display = member.name
            discrim = member.discriminator
            name = f'{display}#{discrim}'
            joindate = f'{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}'
            joined = f'{joindate}, {str(member.joined_at.time())[:-10]}'
            createddate = f'{member.created_at.day}-{member.created_at.month}-{member.created_at.year}'
            created = f'{createddate}, {str(member.created_at.time())[:-10]}'
            em = discord.Embed(title='userinfo', colour=0xFF0000)
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name='Name:', value=name, inline=False)
            em.add_field(name='Nickname:', value=member.nick, inline=False)
            em.add_field(name='User id', value=member.id, inline=False)
            em.add_field(name='Status:', value=member.status, inline=False)
            em.add_field(name='Created at:', value=created, inline=False)
            em.add_field(name='Joined at:', value=joined, inline=False)
            em.add_field(name='Roles:', value='\n '.join(r.name if r.name == '@everyone' else r.mention for r in sorted(member.roles, key=str)), inline=False)
            return await ctx.send(embed=em)


def setup(bot):
    bot.add_cog(Modcommands(bot))
