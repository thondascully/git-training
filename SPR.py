"""Calculates SPRs (Scout Precision Ranking).

Called by server.py"""
# External imports
import random
# No internal imports

SPRs = {
    "Aakash": 12.6,
    "Carl": 1.2,
    "David": 0.1,
    "Kyle": 0.7,
    "Sam C": 0.8,
}

def calculateSPRs():
    for scout, spr in SPRs.items():
        if scout == 'Aakash':
            SPRs[scout] = spr*random.randint(1,8)
        print(f'{scout} has an SPR of {SPRs[scout]}')
