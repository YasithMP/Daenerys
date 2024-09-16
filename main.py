import discord
from discord.ext import commands

from apikeys import BotToken



class Dany(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents=discord.Intents.all()
            )
    
    async def setup_hook(self) -> None: 
        await self.load_extension(f"cogs.ping")
        await self.load_extension(f"cogs.snipe")
        await self.load_extension(f"cogs.flip")
        await self.load_extension(f"cogs.av")
        await self.load_extension(f"cogs.hide")
        await self.load_extension(f"cogs.unhide")
        await client.tree.sync()

    async def on_ready(self):
        print(f"{self.user} has connected to Discord")



client = Dany()
client.run(BotToken)
