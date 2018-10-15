"""
Cleans up a bad venv.
"""

import shared_variables

import shutil

for folder in [
    "lagrangian-transfer",
    "caesar",
    shared_variables.environment_name,
    "__pycache__"
    ]:
    
    try:
        shutil.rmtree(folder)
    except FileNotFoundError:
        continue

