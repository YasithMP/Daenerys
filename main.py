import discord
from discord.ext import commands
import os

from dotenv import load_dotenv


class Dany(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents=discord.Intents.all()
            )
    
    async def setup_hook(self) -> None: 
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')


    async def on_ready(self):
        print(f"{self.user} has connected to Discord")


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')


client = Dany()
client.run(DISCORD_TOKEN)