"""
HEALTH RISK CHECKER - ROOT ENTRY POINT
For desktop testing - imports from app/
"""

import sys
import os

# Add app directory to Python path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'app'))

from main import main

if __name__ == "__main__":
    import flet as ft
    ft.app(target=main)
