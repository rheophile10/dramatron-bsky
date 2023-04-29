
from typing import List
import random
import functools

def make_scene(party:List[str])->str:
    thief= party[random.randint(1,len(party))]
    discoverer = party[random.randint(1,len(party))]
    return f"""The party is in a kitchen in a single room cabin on an island far from shore. 
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

    Last night, somebody stole the cookies and that person is {thief}. This morning {discoverer} found the 
    cookie jar empty and screamed in horror. Everyone has come to find out about it.
    """

def combinations(n:int, r:int)->int:
    n_ = functools.reduce(lambda a, b: a*b, range(1, n+1))
    r_ = functools.reduce(lambda a, b: a*b, range(1, r+1))
    n_r = functools.reduce(lambda a, b: a*b, range(1, (n-r)+1))
    return n_/r_*n_r

def sexual_frustrations(party:List[str]) -> List[str]:
    n = random.randint(1,len(party)) 
    n_relationships = random.randint(1, combinations(n, 2))
    relationship_texts = []
    for _ in range(n_relationships):
        sample = random.sample(range(len(party)),2)
        openly = "openly" if random.getrandbits(1) == 1 else "in secret"
        relationship_texts.append(f"""{sample[0]} and {sample[1]} have been sleeping together {openly}""")
    return relationship_texts

    