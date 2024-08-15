import discord
from discord import app_commands
from discord.ext import commands
import random


class flip(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client


    @app_commands.command(name="flip",  description="Flips a coin")
    async def flip(self, interaction : discord.Interaction):
        result = random.randint(1, 2)
        if result == 1:
            coin_flip = "Heads"
        else:
            coin_flip = "Tails"

        await interaction.response.send_message(coin_flip)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(flip(client))
            