import discord, requests, random
from discord.ext import commands
from math import floor

class Misc(commands.Cog):
	def __init__(self, client) -> None:
		self.client: commands.Bot  = client
		return
	
	@discord.slash_command(name= "ping", description="Get bot latency to discord")
	async def ping(self, interaction: discord.Interaction) -> None:
		await interaction.response.send_message(f'Pong! {floor(self.client.latency * 1000)}ms')
		return

def setup(client: commands.Bot) -> None:
	client.add_cog(Misc(client))
	return