#!/usr/bin/env python3

simpsons = [ ('Moe', "?"), ('Otto', '?'), ('Lisa', 8), ('Bart', 10), ('Maggie', 2), ('Homer', 36), ('Marge', 34) ]

def byAge(character):
    
    if isinstance(character[1], int):
        return character[1]
    else:
        return 1000
simps_sorted = sorted(simpsons, key=byAge)

print(simps_sorted)

print(simpsons[1][1])


