import nextcord
import logging

logging.basicConfig(level=logging.INFO)

from nextcord.ext import commands

TESTING_GUILD_ID = 884122820047667211  # Replace with your guild ID

bot = commands.Bot()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.slash_command(description="My first slash command", guild_ids=[TESTING_GUILD_ID])
async def hi(interaction: nextcord.Interaction):
    await interaction.send("hi dadwy uwu")

bot.run('OTc2ODgyMDY0ODE1MTczNjQy.GF79B0.bHqhDVCJ3HyTOLyaUxqBNpT3kBBspBhcGvPIAA')