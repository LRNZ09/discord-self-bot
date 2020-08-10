import asyncio
import random
from datetime import datetime

import discord
from discord.ext import tasks

from . import config


class SelfClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs, fetch_offline_members=False,
                         guild_subscriptions=False, max_messages=None)

        self.bot_task.start()

    async def on_ready(self):
        print(f'Ready to be {self.user}!')

    async def send_command(self, command):
        channel = self.get_channel(347528226970664971)
        message = f'!{command}'

        print(f'Sending {message} to {channel}...')

        await channel.send(message)

    @tasks.loop(minutes=60 * 6 + 1)
    async def bot_task(self):
        await self.send_command('payday')

        # bet = random.randint(10, 50)
        # choice = random.choice(['heads', 'tails'])
        # await self.send_command(f'coin {bet} {choice}')

    @bot_task.before_loop
    async def bot_task_before_loop(self):
        print('Waiting for client to be ready...')
        await self.wait_until_ready()


def main():
    client = SelfClient()
    client.run(config.TOKEN, bot=False)


if __name__ == "__main__":
    main()
