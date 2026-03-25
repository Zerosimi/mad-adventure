"""
=====================================================================
  Utils
=====================================================================

Utilities for the developers
"""

# Imports
import time
from config import settings

# ===================================================================

def sleep(seconds):
    """Sleeps the program for the provided amount of seconds"""
    if settings.DEBUG is False:
        time.sleep(seconds)
    return
