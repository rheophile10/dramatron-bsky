
from typing import List
import random

from cookie_mystery.bot import Bot

def make_scene(party:List[Bot])->List[str]:
    i, j = random.sample(range(len(party)),2)
    thief= party[i]
    discoverer = party[random.randint(0,len(party)-1)]
    patsy = party[j]
    thief.char_prompt.append(f"You stole the cookies and you don't want anybody to know. If anybody other than the detective blames you, you will blame {patsy.name}")
    thief.char_prompt.append(f"if the detective blames you, you will admit you ate the cookies")
    scene = f"""
    This is an improve comedy and all actors are encouraged to act dramatically and humourously.
    
    A group of people are stranded on an island in a single room cabin with a magically replenishing kitchen. 
    They have access to food, toiletries, and medicine but the only food available is oatmeal and apples. 
    They can fish in the lake and grow vegetables in a garden. There is a jar of cookies that cannot be replaced once empty. 
    They don't know how they got there and are starting to worry about the absence of authority. 

    Last night, somebody stole the cookies. This morning {discoverer.name} found the cookie jar empty and called everybody together. 
    Everyone has come into the cabin to find about it. 
    
    Everyone else is very upset and trying to find out who stole the cookes. 

    Scene Begin!
    """
    return [scene]