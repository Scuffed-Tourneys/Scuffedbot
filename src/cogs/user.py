import discord
from discord.ext import commands
from logging import info as logging_info
from math import floor
import bson
from pymongo.collection import Collection
from db import database
	
class User(commands.Cog):
	def __init__(self, client) -> None:
		self.client: commands.Bot  = client
		return
	
	user_group: discord.SlashCommandGroup = discord.SlashCommandGroup("user", "User info")


	@user_group.command()
	async def add(self, interaction: discord.Interaction, profile_url: str) -> None:
		await interaction.response.send_message(profile_url)
		return
	
	@user_group.command()
	async def info(self, interaction: discord.Interaction, mention: str = "*") -> None:
		users: Collection = database.client["users"]
		if mention == "*":
			mention = str(interaction.user.id)
		user = users.find_one({"user_id" : bson.Int64(mention.split(':')[-1])})
		if not user:
			await interaction.response.send_message(f"Could not find user with ID: `{interaction.user.id}`, `{mention.split(':')[-1]}`")
			return
		embed: discord.Embed = discord.Embed(title=f"{user['username']}'s scoresaber stats", type="rich", color=int('0x' + user['color'], base=16))
		embed.add_field(name="Global Rank 🌐", value="4608", inline=True)
		embed.add_field(name="Country Rank 🇳🇱", value="121", inline=True)
		embed.add_field(name="PP <a:PogLick:792002791828357131>", value="6542.69", inline=True)
		embed.add_field(name="Ranked Acc <:PeepoAcc:792385194351001610>", value="85.09%", inline=True)
		embed.add_field(name="Total Play Count <a:ppJedi:754632378206388315>", value="937", inline=True)
		embed.add_field(name="Ranked Play Count 🧑‍🌾", value="317", inline=True)
		embed.set_footer(text="Bot made by ThiJNmEnS#6669", icon_url="https://cdn.discordapp.com/avatars/490534335884165121/c9ac651c2c61a774820f10a611627678.png")
		await interaction.response.send_message(embed=embed)
		return
	
	"""
	@user_group_add.command()
	async def user_add(self, interaction: discord.Interaction) -> None:
		await interaction.response.send_message(f'User_add')
		return
	"""

def setup(client: commands.Bot) -> None:
	client.add_cog(User(client))
	return