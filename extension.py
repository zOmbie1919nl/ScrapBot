import discord
import asyncio
import async_timeout
from discord.ext import commands

class AutoActions:
    def __init__(self, bot):
        self.bot = bot
        self.raid_modes = dict()

    @commands.command()
    async def raidmode(self, ctx):
        current_mode = self.raid_modes.get(ctx.guild.id, False)
        decoder = {
            "True": "ON",
            "False": "OFF"
        }
        self.raid_modes[ctx.guild.id] = not current_mode
        await ctx.send(f"Turned raid mode {decoder[str(not current_mode)]}")

    async def on_member_join(self, member: discord.Member):
        current_mode = self.raid_modes.get(member.guild.id, False)
        if current_mode:
            await member.send(f"We've enabled raid mode for our server, this makes it so you cannot join the server. \nPlease try again later.")
            await member.kick(reason="Raidmode active")

def setup(bot):
    bot.add_cog(AutoActions(bot))
