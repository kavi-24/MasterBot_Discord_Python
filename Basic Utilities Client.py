# App
# Application ID : 922503627740938240
# Public key : cfa6a44c6fc7cae351c053d6fff0b9fba624be8960e600e041e7c0379a7ecfd0

import discord
from constants import TOKEN, GUILD
from random import choice
import time

'''
class CustomClient(discord.Client):
    async def on_ready(self):
        print(f"{self.user} has connected to Discord")

client = CustomClient()
client.run(TOKEN)
'''

# ALL EVENT HANDLERS IN THIS FILE MUST BE
# COROUTINES (async functions)

intents = discord.Intents.default()
intents.members = True
client = discord.Client(intents=intents)
'''
@client.event
async def on_ready():
    print(f"{client.user} has connected to Discord!")
'''

'''
@client.event
async def on_ready():
    guild = discord.utils.find(lambda g : g.name == GUILD, client.guilds)
    
    print(f"{client.user} is connected to the guild {guild.name} (ID:{guild.id})")
'''


@client.event
async def on_ready():

    guild = discord.utils.get(client.guilds, name=GUILD)

    print(guild)
    print(f"{client.user} is connected to the guild {guild.name} (ID:{guild.id})")

    members = "\n - ".join([member.name for member in guild.members])
    print(f"Guild members:\n - {members}")

    for channel in guild.channels:
        print(f"{channel.name}(id: {channel.id})")

    for role in guild.roles:
        print(f"{role.name}(id: {role.id})")

    # Members
    # for member in guild.members:
    #     print(f"{member}")
    #     print(f"{member.name}")
    #     print(f"{member.nick}")
    #     print(f"{member.id}")
    #     print(f"{member.status}")
    #     print(f"{member.activities}")
    #     print(f"{member.joined_at}")
    #     print(f"{member.roles}")
    #     print(f"{member.top_role}")
    #     print(f"{member.color}")
    #     print(f"{member.avatar_url}")
    #     print(f"{member.guild_permissions}")
    #     print(f"{member.voice}")
    #     print(f"{member.voice.channel}")
    #     print(f"{member.voice.channel.id}")
    #     print(f"{member.voice.channel.name}")
    #     print(f"{member.voice.channel.position}")
    #     print(f"{member.voice.channel.bitrate}")
    #     print(f"{member.voice.channel.user_limit}")
    #     print(f"{member.voice.channel.permissions_for(member)}")
    #     print(f"{member.voice.channel.permissions_for(member).connect}")
    #     print(f"{member.voice.channel.permissions_for(member).speak}")
    #     print(f"{member.voice.channel.permissions_for(member).mute_members}")
    #     print(f"{member.voice.channel.permissions_for(member).deafen_members}")
    #     print(f"{member.voice.channel.permissions_for(member).move_members}")
    #     print(f"{member.voice.channel.permissions_for(member).use_voice_activation}")
    #     print(f"{member.voice.channel.permissions_for(member).priority_speaker}")
    #     print(f"{member.voice.channel.permissions_for(member).view_channel}")


@client.event
async def on_member_join(member):

    # Welcome message in all channels
    # Some other alternate way please
    for channel in member.guild.channels:
        # Check for text channels
        if str(channel.type) == "text":
            await channel.send("Welcome to the server, " + member.mention + "!")
    '''
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )
    '''


@client.event
async def on_message(message):

    print(message.content)
    lower = message.content.lower()
    print(lower)

    if message.content == "$hello":
        await message.channel.send("Hello!")
    elif message.content == "$goodbye":
        await message.channel.send("Goodbye!")
    elif message.content == "$help":
        await message.channel.send("$hello - Say hello\n$goodbye - Say goodbye")
    elif message.content == 'raise-exception':
        await message.channel.send('This will raise an exception')
    elif message.content == "$clear":
        await message.channel.purge(limit=10)
    
    # Copilot Suggestions :)

    # Add bot to vc
    elif "$add-bot" in message.content:
        await message.channel.send("Adding bot to VC")
        await message.author.voice.channel.connect()
        await message.channel.send("Bot added to VC")
        
    elif "$type-random" in message.content:
        await message.channel.send("qwertyuiop[]\\asdfghjkl;'zxcvbnm,./")
     
    elif "$h-me" in message.content:
        await message.channel.send(choice(["STFU", "Didn't ask", "So ?", "No one asked"]))
    
    # elif "fuck" or "shit" or "bitch" in message.content:
        # await message.channel.purge(limit=1)
        # await message.channel.send("Don't be rude, you dumb person.")

    elif "$kick" in message.content :
        await message.channel.send("Kicked user " + message.mentions[0].mention)
        await message.mentions[0].kick()
    elif "$ban" in message.content:
        await message.channel.send("Banned user " + message.mentions[0].mention)
        await message.mentions[0].ban()
    elif "$unban" in message.content:
        await message.channel.send("Unbanned user " + message.mentions[0].mention)
        await message.guild.unban(message.mentions[0])
    elif "$mute" in message.content:
        await message.channel.send("Muted user " + message.mentions[0].mention)
        await message.mentions[0].edit(mute=True)
    elif "$unmute" in message.content:
        await message.channel.send("Unmuted user " + message.mentions[0].mention)
        await message.mentions[0].edit(mute=False)
    elif "$nick" in message.content:
        await message.channel.send("Nickname changed to " + message.mentions[0].nick)
        await message.mentions[0].edit(nick="Nickname")
    elif "$create-role" in message.content:
        await message.channel.send("Created role " + message.mentions[0].mention)
        await message.guild.create_role(message.mentions[0])
    elif "$delete-role" in message.content:
        await message.channel.send("Deleted role " + message.mentions[0].mention)
        await message.mentions[0].delete()
    elif "$role" in message.content:
        await message.channel.send("Added role " + message.mentions[0].mention)
        await message.mentions[0].add_roles(message.mentions[1])
    elif "$unrole" in message.content:
        await message.channel.send("Removed role " + message.mentions[0].mention)
        await message.mentions[0].remove_roles(message.mentions[1])
    elif "$move-user" in message.content:
        await message.channel.send("Moved user " + message.mentions[0].mention)
        await message.mentions[0].move_to(message.mentions[1])
    elif "$create-ch" in message.content:
        await message.channel.send("Created channel " + message.content.split("$create-ch ")[1])
        await message.guild.create_text_channel(message.content.split("$create-ch ")[1])
    elif "$delete-ch" in message.content:
        await message.channel.send("Deleted channel " + message.content.split("$delete-ch ")[1])
        await message.guild.delete_text_channel(message.content.split("$delete-ch ")[1])
    elif "$create-vc" in message.content:
        await message.channel.send("Created voice channel " + message.content.split("$create-vc ")[1])
        await message.guild.create_voice_channel(message.content.split("$create-vc ")[1])
    elif "$delete-vc" in message.content:
        await message.channel.send("Deleted voice channel " + message.content.split("$delete-vc ")[1])
        await message.guild.delete_voice_channel(message.content.split("$delete-vc ")[1])
    elif "$create-em" in message.content:
        await message.channel.send("Created emoji " + message.mentions[0].mention)
        await message.guild.create_emoji(message.mentions[0])
    elif "$delete-em" in message.content:
        await message.channel.send("Deleted emoji " + message.mentions[0].mention)
        await message.mentions[0].delete()
    elif "$create-cat" in message.content:
        await message.channel.send("Created category " + message.mentions[0].mention)
        await message.guild.create_category(message.mentions[0])
    elif "$delete-cat" in message.content:
        await message.channel.send("Deleted category " + message.mentions[0].mention)
        await message.mentions[0].delete()
    elif "$create-msg" in message.content:
        await message.channel.send("Created message " + message.mentions[0].mention)
        await message.guild.create_text_channel(message.mentions[0])
    elif "$delete-msg" in message.content:
        await message.channel.send("Deleted message " + message.mentions[0].mention)
        await message.mentions[0].delete()
    elif "$create-vc-msg" in message.content:
        await message.channel.send("Created voice channel " + message.mentions[0].mention)
        await message.guild.create_voice_channel(message.mentions[0])
    elif "$delete-vc-msg" in message.content:
        await message.channel.send("Deleted voice channel " + message.mentions[0].mention)
        await message.mentions[0].delete()
    elif "$create-role-msg" in message.content:
        await message.channel.send("Created role " + message.mentions[0].mention)
        await message.guild.create_role(message.mentions[0])
    elif "$delete-role-msg" in message.content:
        await message.channel.send("Deleted role " + message.mentions[0].mention)
        await message.mentions[0].delete()

# print("Bruh") # This runs first since the above function is an async

client.run(TOKEN)
