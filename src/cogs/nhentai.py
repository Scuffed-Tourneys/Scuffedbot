import discord
from logging import info as logging_info
from discord.ext import commands
from NHentai import NHentai

# BROKEN COG
# Nhentai does not have an api and after they added cloudflare the module broke
# https://github.com/AlexandreSenpai/NHentai-API/pull/43

nh: NHentai = NHentai()
class NHentaiCog(commands.Cog):
	def __init__(self, client) -> None:
		self.client: commands.Bot  = client
		return

	@discord.slash_command(name= "nhentai", description= "get random doujin from nhentai")
	async def nhentai(self, interaction: discord.Interaction) -> None:
		Doujin = nh.get_random()
		id: str = Doujin.id
		logging_info(id)
		await interaction.response.send_message(f'Your random doujin is https://nhentai.net/g/{id}')
		return

def setup(client: commands.Bot) -> None:
	client.add_cog(NHentaiCog(client))
	return