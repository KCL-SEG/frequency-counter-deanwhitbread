"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    for items_char in items:
        str(items_char)
        for key in frequencies.items():
            if frequencies.get(key) == items_char:
                counter = frequencies.get(key)
                counter = counter + 1
                frequencies[key] = counter
            else:
                frequencies[items_char] = 0

    return frequencies
