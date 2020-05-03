import asyncio
import random

import discord
from discord.ext import tasks

from . import config

PREFIXES = [
    "¿",
    "‽",
    "[prefix goes here]",
    "*notices bot*",
    "*slaps roof of hitomi*",
    "👁",
    "431495393520386068!",
    "8!",
    "according to all known laws of discord, there is no way a bot should be able to ",
    "askjasdljhsdfjkhasdlasdjkajs"
    "erisa!",
    "heh... ",
    "hey bot ",
    "hi!!!!!!!!!",
    "hi!",
    "hi?",
    "hi1",
    "hitomi please",
    "hitomi, do a ",
    "hitomi!",
    "ñ!",
    "undefined",
    "wach!",
]


class SelfClient(discord.AutoShardedClient):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, fetch_offline_members=False, max_messages=None)

        self.pray_task.start()

    async def on_ready(self):
        print(f'Ready to be {self.user}!')

    @tasks.loop(hours=12)
    async def pray_task(self):
        channel = self.get_channel(config.CHANNEL_ID)
        prefix = random.choice(PREFIXES)
        message = f'{prefix}pray'
        print(f'Sending {message} to {channel}...')
        await channel.send(message)

    @pray_task.before_loop
    async def before_loop(self):
        print('Waiting for client to be ready...')
        await self.wait_until_ready()


def main():
    client = SelfClient()
    client.run(config.TOKEN, bot=False)


if __name__ == "__main__":
    main()
