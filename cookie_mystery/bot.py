import asyncio
import random
import openai
import dotenv
import os
from string import punctuation
from rich import print
from typing import List

dotenv.load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.organization = os.getenv("OPENAI_ORGANIZATION")

def get_char_color():
    colours= ['black', 'red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white', 'bright_black', 'bright_red', 'bright_green', 'bright_yellow', 'bright_blue', 'bright_magenta', 'bright_cyan', 'bright_white']
    return colours[random.randint(0, len(colours))]
    


def format_response(response):
    for i, char in enumerate(reversed(response)):
        if char in punctuation:
            response = response[:len(response) - i]
            break
    response += "\n"
    return response


class Bot:
    def __init__(self, name:str, char_prompt:List[str]=[], model="gpt-3.5-turbo", temperature=0.7, max_tokens=150, delay=2):
        self.name = name
        self.char_prompt = char_prompt
        self.model = model
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.delay = delay

        self.color = get_char_color()
        self.colored_name = f"[{self.color}]{self.name}[/{self.color}]"
        print(self.colored_name)

    async def respond(self, history: list):
        # history is a list of strings
        # here we convert to  a dictionary with a role and content
        messages = [{"role": "system", "content": i} for i in self.char_prompt]
        for message in history:
            if message.startswith(self.name):
                messages.append({"role": "assistant", "content": message})
            else:
                messages.append({"role": "user", "content": message})
        messages.append({"role": "assistant", "content": self.name + ": "})
        completion = openai.ChatCompletion.create(
            model=self.model,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            stop=["\n", "Human:", "AI:", self.name + ":"]
        )

        response = completion.choices[0].message.content
        response = self.colored_name + ": " + format_response(response)
        return response

    async def run(self, channel):

        while not channel.closed:
            if random.randint(1, 20) > 10:
                history = channel.get_history()
                response = await self.respond(history)
                channel.add_message(response)
            await asyncio.sleep(self.delay + random.randint(0, 1))