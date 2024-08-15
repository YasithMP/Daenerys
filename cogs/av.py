import discord
from discord import app_commands
from discord.ext import commands

class av(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        

    @app_commands.command(name="av", description="Displays your avatar.")
    async def avatar(self, interaction: discord.Interaction):

        embed = discord.Embed(title="Server Avatar", color=discord.Color.random())
        embed.set_image(url=interaction.user.display_avatar)
        embed.set_author(name=f"{interaction.user.display_name}", icon_url=interaction.user.display_avatar.url)

        await interaction.response.send_message(embed=embed)

async def setup(client: commands.Bot) -> None:
    await client.add_cog(av(client))
        