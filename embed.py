import discord
import asyncio
import time
import yaml
import traceback
from discord.ext import commands

#head and owner Commands
class EmbedFacade(dict):
    def to_dict(self):
        return self

    async def __local_check(self, ctx):
        guild = ctx.guild
        role = discord.utils.get(guild.roles, id=439194953823027200)
        if role in ctx.author.roles:
            return True
        return False

    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CheckFailure):
            author = ctx.author
            return print(f"HeadAndOwnerCommand used in {ctx.channel.name} by {author.name}")

    @commands.command()
    async def embed(self, ctx, *, content):
        try:
            data = yaml.load(content)
            their_embed = EmbedFacade(data)
            await ctx.send(embed=their_embed)
        except Exception:
            await ctx.send(traceback.format_exc())

def setup(bot):
    bot.add_cog(EmbedFacade())
