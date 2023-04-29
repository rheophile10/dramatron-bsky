
from typing import List
import random
import functools

from cookie_mystery.bot import Bot


def combinations(n:int, r:int)->int:
    n_ = functools.reduce(lambda a, b: a*b, range(1, n+1))
    r_ = functools.reduce(lambda a, b: a*b, range(1, r+1))
    n_r = functools.reduce(lambda a, b: a*b, range(1, max((n-r)+1,2)))
    return n_/r_*n_r

def sexual_frustrations(party:List[Bot]) -> None:
    n = random.randint(2,len(party)) 
    n_relationships = min(random.randint(1, combinations(n, 2)),5)
    for _ in range(n_relationships):
        sample = random.sample(range(len(party)),2)
        if random.getrandbits(1) == 1:
            party[sample[0]].relationships.append(f"You have been sleeping with {party[sample[1]].name}")
            party[sample[1]].relationships.append(f"You have been sleeping with {party[sample[0]].name}")
        else:
            party[sample[0]].relationships.append(f"You slept with {party[sample[1]].name} last night and you don't want anyone to know.")
            party[sample[1]].relationships.append(f"You slept with {party[sample[0]].name} last night and you don't want anyone to know.")

def make_scene(party:List[Bot])->List[str]:
    i, j = random.sample(range(len(party)),2)
    thief= party[i]
    discoverer = party[random.randint(0,len(party)-1)]
    patsy = party[j]
    thief.state.append(f"You stole the cookies and you don't want anybody to know. If anybody other than the detective blames you, you will blame {patsy.name}")
    thief.state.append(f"if the detective blames you, you will admit you ate the cookies")
    scene = f"""
    This is an improve comedy and all actors are encouraged to act dramatically and humourously.
    
    A group of people are stranded on an island in a single room cabin with a magically replenishing kitchen. 
    They have access to food, toiletries, and medicine but the only food available is oatmeal and apples. 
    They can fish in the lake and grow vegetables in a garden. There is a jar of cookies that cannot be replaced once empty. 
    They don't know how they got there and are starting to worry about the absence of authority. 
    There is a loaded gun hidden under a floorboard with a skull etched into it.

    Last night, somebody stole the cookies. This morning {discoverer.name} found the cookie jar empty and screamed in horror. 
    Everyone has come into the cabin to find about it. 
    
    Everyone else is very upset and trying to find out who stole the cookes. 

    Scene Begin!
    """
    return [scene]