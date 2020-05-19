import asyncio
import random
from datetime import datetime

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

        self.bot_task.start()

    async def on_ready(self):
        print(f'Ready to be {self.user}!')

    @tasks.loop(hours=1)
    async def bot_task(self):
        channel = self.get_channel(347528226970664971)
        prefix = random.choice(PREFIXES)

        bet = random.randint(5, 25)
        gamble_message = f'{prefix}gamble {bet}'
        print(f'Sending {gamble_message} to {channel}...')
        await channel.send(gamble_message)

        if (datetime.utcnow().hour == 4):
            pray_message = f'{prefix}pray'
            print(f'Sending {pray_message} to {channel}...')
            await channel.send(pray_message)

    @bot_task.before_loop
    async def bot_task_before_loop(self):
        print('Waiting for client to be ready...')
        await self.wait_until_ready()


def main():
    client = SelfClient()
    client.run(config.TOKEN, bot=False)


if __name__ == "__main__":
    main()
