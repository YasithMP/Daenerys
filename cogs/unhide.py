import discord
from discord.ext import commands

class Unhide(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unhide(self, ctx):
        
        channel = ctx.channel
        
        everyone_role = ctx.guild.default_role 

        overwrite = discord.PermissionOverwrite(view_channel=None)
        
        await channel.set_permissions(everyone_role, overwrite=overwrite)

        await ctx.send(f'Channel is now visible.')

    @unhide.error
    async def permissions_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the `Manage Channels` permission to run this command.")

async def setup(client: commands.Bot):
    await client.add_cog(Unhide(client))