import discord
import datetime
from discord import app_commands
from discord.ext import commands

class ping(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client


    @app_commands.command(name="ping", description="Shows API Latency")
    async def ping(self, interaction : discord.Interaction):
        displayText = (f"**API Latency: {round(self.client.latency * 1000)}ms**")

        embed = discord.Embed(description=displayText, color=discord.Color.random(), timestamp=datetime.datetime.now())
        embed.set_author(name=f"{interaction.user.display_name}", icon_url=interaction.user.display_avatar)
        

        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(ping(client))

    