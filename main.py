import discord
from functools import reduce
import tokens
import operator

client = discord.Client()

emoji_message_prefix = '!emoji'


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith(emoji_message_prefix):
        message_text = message.content[len(emoji_message_prefix):].strip()
        if not len(message_text):
            await client.send_message(message.channel, 'Empty string :drooling_face:')
            return

        emojis = list(
            map(lambda letter: ':regional_indicator_' + letter + ':' if letter.isalpha() else letter, message_text))
        emoji_string = reduce(operator.add, emojis)
        await client.send_message(message.channel, emoji_string)


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


client.run(tokens.EMOJI_BOT_TOKEN)
