from discord.ext import commands

class ping_prefix(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client


    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f"API Latency: `{round(self.client.latency * 1000)}ms`")


async def setup(client: commands.Bot) -> None:
    await client.add_cog(ping_prefix(client))
