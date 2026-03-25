"""
=====================================================================
  Engine
=====================================================================

Core engine tools for the game
"""
import random
import string
from collections.abc import Callable

# ===================================================================

def choose_option(options: list) -> Callable:
    """
    Display provided options and returns the scene from the selected one.

    Parameters
    ----------
    options: list
        Containing options as tuples with (string, scene function)
    """

    assert all([isinstance(option, tuple) for option in options]), \
        "Options should be provided as tuple[text, func]"
    assert all([(option[1] is None) or (len(option[0]) <= 32) for option in options]), \
        "Options should have a text length of 32 characters at most"

    display_text = ""
    for i in range(len(options)):
        if i % 2 == 0:
            display_text += "\n"
        display_text += f"{string.ascii_lowercase[i]}) {options[i][0]:<32}"
        if i % 1 == 1:
            display_text += "  "
    print(display_text)

    choice_letter = input("> ")

    try:
        idx = list(string.ascii_lowercase).index(choice_letter.lower())
        choice = options[idx][1]
    except (IndexError,  ValueError):
        return choose_option(options)

    return choice

# -------------------------------------------------------------------

def chance_roll(chance) -> float:
    """
    Randomly returns True or False based on the chances provided.
    """
    if chance < 1 or chance > 100:
        raise ValueError("Chance should be a number between 1 and 100.")

    number = random.randint(0, 100)
    return number <= chance
