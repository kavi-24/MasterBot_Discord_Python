from constants import TOKEN
import random
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')


@bot.command(name='roll', help='Simulates rolling dice.\nUsage: !roll <number of sides=6>')
async def roll(ctx, number_of_sides: int = 6):  # Type annonation is important
    dice = str(random.choice(range(1, number_of_sides+1)))
    await ctx.send(' '.join(dice))



@bot.command(name="create_channel", help="Creates a channel (admin rights required)\nUsage: !create_channel <channel_name>")
@commands.has_role("Mod")
async def create_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f"Creating channel: {channel_name}")
        await guild.create_text_channel(channel_name)
    else:
        await ctx.send(f"Channel '{existing_channel}' already exists")

@bot.command(name="delete_channel", help="Deletes a channel (admin rights required)\nUsage: !delete_channel <channel_name>")
@commands.has_role("Mod")
async def delete_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel:
        print(f"Deleting channel: {channel_name}")
        await existing_channel.delete()
    else:
        await ctx.send(f"Channel '{channel_name}' does not exist")

@bot.command(name="create_voice_channel", help="Creates a voice channel (admin rights required)\nUsage: !create_voice_channel <channel_name>")
@commands.has_role("Mod")
async def create_voice_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if not existing_channel:
        print(f"Creating voice channel: {channel_name}")
        await guild.create_voice_channel(channel_name)
    else:
        await ctx.send(f"Voice channel '{existing_channel}' already exists")

@bot.command(name="delete_voice_channel", help="Deletes a voice channel (admin rights required)\nUsage: !delete_voice_channel <channel_name>")
@commands.has_role("Mod")
async def delete_voice_channel(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel:
        print(f"Deleting voice channel: {channel_name}")
        await existing_channel.delete()
    else:
        await ctx.send(f"Voice channel '{channel_name}' does not exist")

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.CheckFailure):
        await ctx.send('You do not have the role for this command.')

bot.run(TOKEN)
