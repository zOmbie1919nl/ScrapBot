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

    async def on_message(self, msg: discord.Message):
        if msg.channel.id == 488373296300032001:
            guild = msg.guild
            member = msg.author
            role = discord.utils.get(guild.roles, id=488374525856317470)
            role2 = discord.utils.get(msg.guild.roles, id=304833080563204096)
            if role2 in msg.author.roles:
                return
            else:
                await member.add_roles(role)
                await member.send(f"Because of Speed-Builds, you have been muted for one minute! \nThis means you can suggest a build again in one minute!")
                length = 60
                await asyncio.sleep(length)
                await member.remove_roles(role)

    async def on_message(self, msg: discord.Message):
        channel = msg.channel
        if msg.content == "?ban":
            url = "https://cdn.discordapp.com/attachments/332597002816978944/493491330941452304/zOmbie2.gif"
            em = discord.Embed()
            em.set_image(url=url)
            await channel.send(embed=em)


def setup(bot):
    bot.add_cog(AutoActions(bot))
