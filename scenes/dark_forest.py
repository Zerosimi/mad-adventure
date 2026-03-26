"""
=====================================================================
  Scenes / Dark Forest
=====================================================================
"""

# Imports
from ._registry import register
from engine import choose_option, chance_roll
from utils import sleep

# ===== Scene =======================================================

@register    # You need to register the entry scene of your arc (and add the module to the scenes.__init__.py file.
def entry_scene():
    
    print(f"\nA **wild** forest appears!")
    sleep(2.0) # Add some suspense by adding breaks between text (this would add a 2 seconds break)
    print("It is a scary and dark place.", end=' ', flush=True)
    sleep(2.0)
    print("Should I really go?")
    sleep(1.0)

    # You can add options for the player to choose from like this:
    next_scene = choose_option([
        ('Scary. Better walk slowly..', continuation_scene), # If you want option 1 to lead to a continuation_scene
        ('Start running.', continuation_scene)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene

# -----------------------------------------------

def continuation_scene():
    
    print(f"\nThese trees look particularly scary.")
    sleep(1.0)
    print("Maybe I should move?")
    sleep(2.0)

    example_roll = chance_roll(75) # You can use a chance roll like this, where 25 is the probability of success

    # You can add options for the player to choose from like this:
    next_option = continuation_scene if example_roll else None    

    next_scene = choose_option([
        ('Speed up.', next_option), # If you want option 1 to lead to a continuation_scene
        ('Turn right.', next_option)                # If you want option 2 to exit this scene and continue the game
    ])

    return next_scene
