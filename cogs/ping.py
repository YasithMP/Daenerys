import discord
import datetime
from discord import app_commands
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')

class ping(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # @app_commands.guilds(discord.Object(id=DEV_GUILD_ID))
    @app_commands.command(name="ping", description="Shows API Latency")
    async def slash_ping(self, interaction : discord.Interaction):
        displayText = (f"**API Latency: {round(self.client.latency * 1000)}ms**")

        embed = discord.Embed(description=displayText, color=discord.Color.random(), timestamp=datetime.datetime.now())
        embed.set_author(name=f"{interaction.user.display_name}", icon_url=interaction.user.display_avatar)
        
        await interaction.response.send_message(embed=embed)


    @commands.command(name="ping")
    async def prefix_ping(self, ctx):
        await ctx.reply(f"API Latency: `{round(self.client.latency * 1000)}ms`")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(ping(client))

    