import asyncio
import time

from rich import print

from typing import List

from cookie_mystery.bot import Bot
from cookie_mystery.scene import make_scene
from cookie_mystery.party import Party
class Channel:
    def __init__(self, party: Party, time_limit:int = 15):
        self.closed = False
        self.time_limit = time_limit
        self.conversation = make_scene(party.bots)
        self.start = time.time()

    def get_history(self):
        return self.conversation[-5:]
    
    def get_user_input(self):
        print("[blue]Detective[/blue]: ", end="")
        text = input()
        self.start = time.time()
        if len(text) == 0:
            return
        if text in ["quit", "exit", "q", "e"]:
            self.closed = True
            return
        formatted_input = f"Detective: {text}"
        self.conversation.append(formatted_input)

    def add_message(self, message):
        self.conversation.append(message)
        print(message)
        if time.time() - self.start > self.time_limit:
            self.get_user_input()

if __name__ == "__main__":  
    from cookie_mystery.prompts import bots
    party = Party(bots)
    channel = Channel(party)

    # Run all the bots at once
    async def run_bots():
        tasks = [bot.run(channel) for bot in party.bots]
        await asyncio.gather(*tasks)
            
    asyncio.run(run_bots())