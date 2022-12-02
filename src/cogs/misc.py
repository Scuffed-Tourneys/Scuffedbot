import discord, requests, random
from discord.ext import commands
from logging import info as logging_info
from math import floor

class Misc(commands.Cog):
	def __init__(self, client):
		self.client: commands.Bot  = client
	
	@discord.slash_command(name= "ping", description="Get bot latency to discord")
	async def ping(self, interaction: discord.Interaction):
		await interaction.response.send_message(f'Pong! {floor(self.client.latency * 1000)}ms')
		logging_info('{floor(self.client.latency * 1000)}ms')

def setup(client: commands.Bot):
	client.add_cog(Misc(client))