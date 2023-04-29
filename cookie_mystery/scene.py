
from typing import List
import random
import functools

from cookie_mystery.bot import Bot


def combinations(n:int, r:int)->int:
    n_ = functools.reduce(lambda a, b: a*b, range(1, n+1))
    r_ = functools.reduce(lambda a, b: a*b, range(1, r+1))
    n_r = functools.reduce(lambda a, b: a*b, range(1, max((n-r)+1,2)))
    return n_/r_*n_r

def sexual_frustrations(party:List[Bot]) -> List[Bot]:
    n = random.randint(2,len(party)) 
    n_relationships = random.randint(1, combinations(n, 2))
    for _ in range(n_relationships):
        sample = random.sample(range(len(party)),2)
        if random.getrandbits(1) == 1:
            party[sample[0]].relationships.append(f"You have been sleeping with {party[sample[1]].name}")
            party[sample[1]].relationships.append(f"You have been sleeping with {party[sample[0]].name}")
        else:
            party[sample[0]].relationships.append(f"You slept with {party[sample[1]].name} last night and you don't want anyone to know.")
            party[sample[1]].relationships.append(f"You slept with {party[sample[0]].name} last night and you don't want anyone to know.")
    return party

def make_scene(party:List[Bot])->List[str]:
    i, j = random.sample(range(len(party)),2)
    thief= party[i]
    discoverer = party[random.randint(0,len(party)-1)]
    patsy = party[j]
    scene = f"""The party is in a kitchen in a single room cabin on an island in the middle of a limitless ocean. 
    None of them remember how they got there and they've been living together there for several weeks now. 
    Every time they open the kitchen cabinets, food appears magically. They never want for food or toiletries 
    or medecine or first aid supplies. The food available to them however only consists of oatmeal and apples. 
    There are fish in the lake and a garden is full of vegetables. They are able to fish with tackle they 
    found in a shed. Essentially the party has all it needs but in the cabin there is a single jar of cookies and 
    when a cookie is removed from the jar it is not restored as the other items are. It is impossible to make
    or acquire new cookies. 

    The Party does not know why they are here or how they got here. They are still very civil with one another
    but they are beginning to be nervous about how long they can maintain this civility in the absence of 
    any authority to enforce laws or standards of decency among them. They have not found it but there is a 
    Browning Hi Power in good condition with a fully loaded magazine under one of the floorboards in the cabin. 
    That floorboard has a skull etched into its surface. 

    Last night, somebody stole the cookies and that person is {thief.name}. This morning {discoverer.name} found the 
    cookie jar empty and screamed in horror. Everyone has come into the cabin to find about it. {thief.name} does not
    believe they stole the cookies (they were sleepwalking). While {thief.name} was sleeping, they dreamed that 
    {patsy.name} ate the cookies and this morning they really suspect {patsy.name} ate them.  
    
    Everyone else is very upset and trying to find out who stole the cookes. 

    Scene Begin!
    """
    return [scene]