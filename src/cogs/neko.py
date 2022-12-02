import discord, io, aiohttp, json, requests
from logging import info as logging_info
from discord.ext import commands

async def image(link):
	logging_info(f"image function ran with {link}")
	async with aiohttp.ClientSession() as session:
		async with session.get(link) as resp:
			json_data = json.loads(await resp.text())
			async with session.get(json_data["url"]) as resp:
				return io.BytesIO(await resp.read())

class neko(commands.Cog):
	def __init__(self, client) -> None:
		self.client: commands.Bot  = client
		return

	@discord.slash_command(name= "waifu", description="Get one NSFW pic.")
	@commands.is_nsfw()
	async def waifu(self, interaction:discord.Interaction) -> None:
		await interaction.response.send_message(file=discord.File(await image("https://api.waifu.pics/nsfw/waifu"), "waifu.png"))

def setup(client: commands.Bot) -> None:
	client.add_cog(neko(client))
	return