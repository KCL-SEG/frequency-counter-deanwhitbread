"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for key in items:
        key = str(key)

        if frequencies.get(key) != None:
            value = frequencies.get(key)
            frequencies.update({key : value + 1})
        else:
            frequencies.update({key : 1})
            
    return frequencies
