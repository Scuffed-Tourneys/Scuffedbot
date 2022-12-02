import discord
from logging import info as logging_info
from discord.ext import commands
from NHentai import NHentai

nhentai = NHentai
class nhen(commands.Cog):
	def __init__(self, client):
		self.client: commands.Bot  = client

	@discord.slash_command(name= "nhentai", description= "get random doujin from nhentai")
	async def nhentai(self, interaction: discord.Interaction):
		Doujin = nhentai.get_random()
		id = Doujin.id
		logging_info(id)
		await interaction.response.send_message(f'Your random doujin is https://nhentai.net/g/{id}')

def setup(client: commands.Bot):
	client.add_cog(nhen)