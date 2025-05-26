import discord
from discord import app_commands
from discord.ext import commands
import datetime
import os
from dotenv import load_dotenv

load_dotenv()
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')

class Help(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.displayText = (f"""**Daenerys's Help Page** 

Daenerys Targaryen is a dragon-backed queen who talks justice, breaks chains, and occasionally burns down cities when things don’t go her way.

** :dividers: Channel Owner Commands**
`.hide` - hide your channel.
`.unhide` - make your channel public.
`.add @user` - add a user to your channel. User will be able to see your channel even when its locked.
`.remove @user` - remove a user. User will not be able to see your channel even when its unlocked.
`.reset @user` - reset permission of a user.

** :books: General Commands**
`.flip` - flip a coin. (Heads, Tails or *maybe* Side).
`.av` - get user avatar.

** :wrench: Moderation Commands** (REQUIRE: MANAGE PERMISSIONS)
`.purge` - delete messages in bulk, mention the number of messages you want to delete.""")

    # @app_commands.guilds(discord.Object(id=DEV_GUILD_ID))
    @app_commands.command(name="help", description="shows all available commands.")
    async def slash_ping(self, interation : discord.Interaction):
        
        embed = discord.Embed(description=self.displayText, color=discord.Color.random(), timestamp=datetime.datetime.now())
        
        await interation.response.send_message(embed=embed)

    @commands.command(name="help")
    async def prefix_help(self, ctx):

        embed = discord.Embed(description=self.displayText, color=discord.Color.random(), timestamp=datetime.datetime.now())

        await ctx.send(embed=embed)


async def setup(client: commands.Bot) -> None:
    await client.add_cog(Help(client))