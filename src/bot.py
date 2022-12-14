import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents: discord.Intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client: commands.Bot = commands.Bot(command_prefix="\\", intents=intents)

@client.event
async def on_ready() -> None:
	print(f"Logged on as {client.user}")
	return

cogs: list[str] = ['error_handler', 'misc', 'neko', 'status', 'user']

for cog in cogs:
	client.load_extension(f'cogs.{cog}')
client.load_extension('jishaku')

client.run(os.getenv("TOKEN"))