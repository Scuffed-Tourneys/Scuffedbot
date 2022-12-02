import discord, requests, random
from discord.ext import commands
from math import floor

class Cards(commands.Cog):
	def __init__(self, client):
		self.client: commands.Bot  = client

	@discord.slash_command(name= "draw", description="Draw a card")
	async def draw(self, interaction: discord.Interaction):
		r = requests.get('https://scoresaber.com/api/players/count')
		id = random.randint(1, int(r.text))
		await interaction.response.send_message(f"Drawn {id}")

def setup(client: commands.Bot):
	client.add_cog(Cards(client))