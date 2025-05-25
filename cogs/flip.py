import discord
from discord import app_commands
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')

class flip(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

    # @app_commands.guilds(discord.Object(id=DEV_GUILD_ID))
    @app_commands.command(name="flip",  description="Flips a coin")
    async def slash_flip(self, interaction : discord.Interaction):
        result = random.randint(1, 2)
        if result == 1:
            coin_flip = "Heads"
        else:
            coin_flip = "Tails"

        await interaction.response.send_message(coin_flip)

    @commands.command(name="flip")
    async def prefix_flip(self, ctx):
        result = random.randint(1, 2)
        if result == 1:
            coin_flip = "Heads"
        else:
            coin_flip = "Tails"

        await ctx.reply(coin_flip)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(flip(client))
            