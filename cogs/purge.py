from discord.ext import commands

class Purge(commands.Cog):
    def __init__(self, client: commands.Bot):
        self.client = client

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def purge(self, ctx, amount: int):
        if amount == 1:
            deleted = await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"{len(deleted) - 1} message were deleted.", delete_after=5)
        else:
            deleted = await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"{len(deleted) - 1} messages were deleted.", delete_after=5)

    @purge.error
    async def purge_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send("You need the `Manage Channel` permission to use this command.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send("Please enter a valid number.")
        else:
            await ctx.send("An error occurred while trying to purge messages.")

async def setup(client: commands.Bot):
    await client.add_cog(Purge(client))