import discord
from discord.ext import commands

class ScrapperCommands:
    def __init__(self, bot):
        self.bot = bot

    async def __local_check(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=308288217910870017) #scrapper
        if role in ctx.author.roles:
            return True
        return False


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
        createddate = f"{member.created_at.day}-{member.created_at.month}-{member.created_at.year}"
        created = f"{createddate}, {str(member.created_at.time())[:-10]}"
        createdday =  member.created_at.day + member.created_at.month + member.created_at.year

        if reason is None:
            return await ctx.send("I'd need a reason why you suspect this member of being or having an alt account.")

        else:
            em = discord.Embed(title="Alt account suspected", colour=0xff6700)
            em.set_thumbnail(url=member.avatar_url)

            em.add_field(name="Username:", value=member.mention, inline=False)
            em.add_field(name="User's ID:", value=member.id, inline=False)
            em.add_field(name="Joined at:", value=joined, inline=False)
            em.add_field(name="Registered:", value=created, inline=False)
            em.add_field(name="Suspected by:", value=author.mention, inline=False)
            return await channel.send(embed=em)

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

def setup(bot):
    bot.add_cog(ScrapperCommands(bot))
