import discord
import json

from helperfile import filter_list, command_list, add_word, remove_word
from asyncio import sleep
from time import gmtime, strftime
from discord.ext import commands
from datetime import timedelta

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix="$", intents=intents)


@client.event
# Startup Alerter
async def on_ready():
    channel = client.get_channel(1486116302404845608)

    await channel.send(f"Actived at: {strftime("%Y-%m-%d %H:%M:%S", gmtime())}")


@client.event
# Message Filter
async def on_message(message):
    if message.author.id == 1486094436088942792:
        await sleep(10)
        await message.delete()

    await client.process_commands(message)

    content = message.content.lower()

    if message.author.bot:
        return
    for word in filter_list:
        if content.split(" ")[0] in command_list:
            continue
        else:
            if word.lower() in content:
                author = message.author

                await message.reply(
                    f"{author.mention} was just timed out for repeating a blacklisted word."
                )
                await message.delete()

                try:
                    await author.timeout(timedelta(seconds=60))
                except Exception as e:
                    print(f"Failed to timeout: {e}")
                return


@client.command()
@commands.has_permissions(administrator=True)
# Add blacklisted word
async def blacklist_add(ctx, *, word: str):
    if add_word(word):
        await ctx.reply(f"Added `{word}` to blacklist.")
    else:
        await ctx.reply("Already within blacklisted filter.")


@client.command()
@commands.has_permissions(administrator=True)
# Remove blacklisted word
async def blacklist_remove(ctx, *, word: str):
    if remove_word(word):
        await ctx.reply(f"Removed `{word}` from blacklist.")
    else:
        await ctx.reply("Not within blacklisted filter.")


@client.command()
@commands.has_permissions(manage_messages=True)
# Purge Messages
async def purge(ctx, *, amount: int):
    current_chanel = ctx.channel

    async for message in current_chanel.history(limit=amount):
        await sleep(0.05)
        await message.delete()
    await ctx.send(f"Purged {amount} messages.")


@client.event
# Startup Alerter
async def on_disconnect(ctx):
    current_channel = ctx.channel

client.run("no")
