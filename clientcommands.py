import discord
import random
import asyncio

client = discord.Client

#wrap send_message
async def say(client, channel, msg):
    await client.send_message(channel, msg)

async def react(client, channel):
    msg = await client.send_message(channel, 'react to me')
    res = await client.wait_for_reaction(message=msg)
    await client.send_message(channel, res.reaction.emoji)
    print(res.reaction.emoji)

async def repeat(client, channel, msgs):
    for i in msgs:
        await say(client, channel, i.content)
