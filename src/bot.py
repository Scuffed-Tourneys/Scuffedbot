import discord, os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = commands.Bot(command_prefix="<", intents=intents)

@client.event
async def on_ready():
	print(f"Logged on as {client.user}")

cogs = ['cards', 'misc']

for cog in cogs:
	client.load_extension(f'cogs.{cog}')
client.load_extension('jishaku')

client.run(os.getenv("TOKEN"))