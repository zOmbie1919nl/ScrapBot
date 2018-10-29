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

    @commands.cooldown(1, 60, commands.BucketType.user)      
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
