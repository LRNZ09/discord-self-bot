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

    async def send_command(self, command):
        channel = self.get_channel(347528226970664971)
        prefix = random.choice(PREFIXES)
        message = f'{prefix}{command}'

        print(f'Sending {message} to {channel}...')

        await channel.send(message)

    @tasks.loop(hours=1)
    async def bot_task(self):
        hour = datetime.utcnow().hour

        if (hour == 0):
            await self.send_command('pray')

        if (hour % 2):
            bet = random.randint(1, 20)
            await self.send_command(f'gamble {bet}')

    @bot_task.before_loop
    async def bot_task_before_loop(self):
        print('Waiting for client to be ready...')
        await self.wait_until_ready()


def main():
    client = SelfClient()
    client.run(config.TOKEN, bot=False)


if __name__ == "__main__":
    main()
