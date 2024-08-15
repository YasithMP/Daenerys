import discord
from discord import app_commands
from discord.ext import commands


class snipe(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client

        self.client.sniped_messages = {}

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        self.client.sniped_messages[message.guild.id] = (message.content, message.author, message.channel.name, message.created_at)

    @app_commands.command(name="snipe", description="Recovers a deleted message")
    async def snipe(self, interaction: discord.Interaction):

        try:
            contents, author, channel_name, time = self.client.sniped_messages[interaction.guild.id]

            if (interaction.channel.name == channel_name):

                embed = discord.Embed(description=contents, color=discord.Color.random(), timestamp=time)
                embed.set_author(name=f"Message sent by {author.name}", icon_url=author.avatar.url)
                embed.set_footer(text=f"Deleted in : #{channel_name}")
                await interaction.response.send_message(embed=embed)

            else:
                await interaction.response.send_message("Can't find anything.")
        except Exception:
            await interaction.response.send_message("Can't find anything.")



async def setup(client: commands.Bot) -> None:
    await client.add_cog(snipe(client))