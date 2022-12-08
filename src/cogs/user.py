import discord, requests, bson, json
from discord.ext import commands
from pymongo.collection import Collection
from db import database
import re
	
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
		
		# get user ID
		if mention == "*":
			mention = str(interaction.user.id)
		else:
			mention = re.search('/([0-9])\w+/g', mention).group(1)
		
		# Get userdata from database
		users: Collection = database.client["users"]
		user = users.find_one({"user_id" : bson.Int64(mention)})
		if not user:
			await interaction.response.send_message(f"Could not find user with ID: `{interaction.user.id}`")
			return
		
		# Get data from
		r: requests.Response = requests.get(f"https://new.scoresaber.com/api/player/{user['scoresaber']}/full")
		if not r.ok:
			await interaction.response.send_message(f"Could not get scoresaber userdata from user with ID: `{interaction.user.id}`")
			return
		scoresaberdata = json.loads(r.text)
		
		# Create embed
		embed: discord.Embed = discord.Embed(title=f"{user['username']}'s scoresaber stats", type="rich", color=int('0x' + user['color'], base=16))
		embed.add_field(name="Global Rank 🌐", value=scoresaberdata['playerInfo']['rank'], inline=True)
		embed.add_field(name="Country Rank 🇳🇱", value=scoresaberdata['playerInfo']['countryRank'], inline=True)
		embed.add_field(name="PP <a:PogLick:792002791828357131>", value=scoresaberdata['playerInfo']['pp'], inline=True)
		embed.add_field(name="Ranked Acc <:PeepoAcc:792385194351001610>", value=f"{round(scoresaberdata['scoreStats']['averageRankedAccuracy'], 2)}%", inline=True)
		embed.add_field(name="Total Play Count <a:ppJedi:754632378206388315>", value=scoresaberdata['scoreStats']['totalPlayCount'], inline=True)
		embed.add_field(name="Ranked Play Count 🧑‍🌾", value=scoresaberdata['scoreStats']['rankedPlayCount'], inline=True)
		embed.set_footer(text="Bot made by ThiJNmEnS#6669", icon_url="https://cdn.discordapp.com/avatars/490534335884165121/c9ac651c2c61a774820f10a611627678.png")
		
		# Send
		await interaction.response.send_message(embed=embed)
		return

def setup(client: commands.Bot) -> None:
	client.add_cog(User(client))
	return