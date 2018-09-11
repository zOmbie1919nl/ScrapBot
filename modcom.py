import discord
import asyncio
import os
import aiohttp
import time
from discord.ext import commands

class Modcommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        return ctx.author.guild_permissions.view_audit_log

    @commands.command()
    async def poll(self, ctx, *, words):
        msg = await ctx.send(words)
        await ctx.message.delete()
        await msg.add_reaction(u"\U0001F44E")
        await msg.add_reaction(u"\U0001F44D")

    @commands.command()
    async def ping(self, ctx):
        start = time.monotonic()
        msg = await ctx.send('Pinging....')
        heartbeat = ctx.bot.latency * 1000
        await msg.edit(content=f'Ping: {heartbeat:,.2f}ms')

    @commands.command()
    async def clear(self, ctx, amount: int=None):
        if amount is None:
            await ctx.send('Please put in a value for me to clear!')
        else:
            clear = amount +1
            await ctx.channel.purge(limit=clear)
            await ctx.send(f'``{amount}`` message(s) has been cleared', delete_after = 5)

    @commands.command()
    async def info(self, ctx):
        guild = ctx.guild
        em = discord.Embed(title="ScrapMan's social Media", colour=0xFF0000)
        em.set_author(name="ScrapMan's discord")
        em.set_thumbnail(url=guild.icon_url)
        em.add_field(name="Twitter:", value="Get updates about videos and random day to day thoughts from ScrapMan and his peers! \nhttps://twitter.com/ScrapManYT", inline=False)
        em.add_field(name="Sponser:", value="Become a Sponsor on Youtube for special perks and rewards within the Youtube app by clicking the Sponsor button next to the Sub button on his channel!", inline=False)
        em.add_field(name="Patreon:", value="Directly support ScrapMan for his efforts in exchange for exclusive access to various rewards \nhttps://www.patreon.com/scrapman", inline=False)
        em.add_field(name="Merch:", value="Show off your support for ScrapMan to your friends with a shirt branding the official ScrapMan logo \nhttps://teespring.com/stores/scrapman", inline=False)
        await ctx.send(embed=em)

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

    @commands.command()
    async def altsuspect(self, ctx, member: discord.Member=None, *, reason=None):
        await ctx.message.delete()
        if member is None:
            return await ctx.send("Please give me a member to check if they're an alt account.")

        guild = ctx.guild
        author = ctx.author
        id = 488763748128129035
        channel = guild.get_channel(id)
        joindate = f"{member.joined_at.day}-{member.joined_at.month}-{member.joined_at.year}"
        joined = f'{joindate}, {str(member.joined_at.time())[:-10]}'
        joinedday = member.joined_at.day + member.joined_at.month + member.joined_at.year
        joinedday2 = member.joined_at.day + 2
        createddate = f"{member.created_at.day}-{member.created_at.month}-{member.created_at.year}"
        created = f"{createddate}, {str(member.created_at.time())[:-10]}"
        createdday =  member.created_at.day + member.created_at.month + member.created_at.year

        if reason is None:
            return await ctx.send("I'd need a reason why you suspect this member of being or having an alt account.")

        elif createdday == joinedday or createdday == joinedday2:
            em = discord.Embed(title="Alt account suspected", colour=0xff6700)
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name="Bot's Opinion:", value="Seeing they've just joined, there is a slight chance that they're an alt account!", inline=False)
            em.add_field(name="Username:", value=member.mention, inline=False)
            em.add_field(name="User's ID:", value=member.id, inline=False)
            em.add_field(name="Joined at:", value=joined, inline=False)
            em.add_field(name="Registered:", value=created, inline=False)
            em.add_field(name="Suspected by:", value=author.mention, inline=False)
            em.add_field(name="Suspected for:", value=reason, inline=False)
            return await channel.send(embed=em)
        else:
            em = discord.Embed(title="Alt account suspected", colour=0xff6700)
            em.set_thumbnail(url=member.avatar_url)
            em.add_field(name="Bot's Opinion:", value="Nothing really, this person doesn't look suspicious to me.", inline=False)
            em.add_field(name="Username:", value=member.mention, inline=False)
            em.add_field(name="User's ID:", value=member.id, inline=False)
            em.add_field(name="Joined at:", value=joined, inline=False)
            em.add_field(name="Registered:", value=created, inline=False)
            em.add_field(name="Suspected by:", value=author.mention, inline=False)
            em.add_field(name="Suspected for:", value=reason, inline=False)
            return await channel.send(embed=em)





def setup(bot):
    bot.add_cog(Modcommands(bot))
