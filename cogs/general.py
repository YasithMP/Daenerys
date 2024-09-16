from discord.ext import commands

class General(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='sync', hidden = True)
    @commands.is_owner()
    async def sync(self, ctx):
        synced = await self.client.tree.sync()
        await ctx.send(f'`{len(synced)}` commands synced successfully.')


    @commands.command(name='reload', hidden = True)
    @commands.is_owner()
    async def reload(self, ctx, extension):
        await self.client.reload_extension(f'cogs.{extension}')
        await ctx.send(f'Cog: `{extension}` reloaded successfully.')

async def setup(client: commands.Bot) -> None:
    await client.add_cog(General(client))
