import discord
from discord.ext import commands
import os
from dotenv import load_dotenv


load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DEV_GUILD_ID = os.getenv('DEV_GUILD_ID')


class Dany(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='.',
            intents=discord.Intents.all(),
            help_command=None
            )
    
    async def setup_hook(self) -> None: 
        for file in os.listdir('./cogs'):
            if file.endswith('.py'):
                await self.load_extension(f'cogs.{file[:-3]}')
        try:
            synced = await self.tree.sync(guild=discord.Object(id=DEV_GUILD_ID))
            if len(synced) > 0:
                print(f"Synced {len(synced)} command(s) to the development guild.")
        except Exception as e:
            print(e)

    async def on_ready(self):
        print(f"{self.user} has connected to Discord")


client = Dany()
client.run(DISCORD_TOKEN)