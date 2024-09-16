import discord
from discord.ext import commands

class Channel(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def hide(self, ctx):
        
        channel = ctx.channel
        
        everyone_role = ctx.guild.default_role
        
        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False
        
        await channel.set_permissions(everyone_role, overwrite=overwrite)

        await ctx.send(f'Channel is now hidden.')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def unhide(self, ctx):
        
        channel = ctx.channel
        
        everyone_role = ctx.guild.default_role 

        overwrite = discord.PermissionOverwrite(view_channel=None)
        
        await channel.set_permissions(everyone_role, overwrite=overwrite)

        await ctx.send(f'Channel is now visible.')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def add(self, ctx, member: discord.Member):
        channel = ctx.channel

        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = True 

        await channel.set_permissions(member, overwrite=overwrite)

        await ctx.send(f'{member.mention} has been added to this channel.')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def remove(self, ctx, member: discord.Member):
        channel = ctx.channel

        overwrite = discord.PermissionOverwrite()
        overwrite.view_channel = False 

        await channel.set_permissions(member, overwrite=overwrite)

        await ctx.send(f'{member.mention} has been removed from this channel.')

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def reset(self, ctx, member: discord.Member):
        channel = ctx.channel

        await channel.set_permissions(member, overwrite=None)

        await ctx.send(f'Permissions for {member.mention} have been reset to default.')


    @hide.error
    @unhide.error
    @add.error
    @remove.error
    @reset.error
    async def permissions_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You don't have the `Manage Channels` permission to run this command.")

async def setup(client: commands.Bot):
    await client.add_cog(Channel(client))