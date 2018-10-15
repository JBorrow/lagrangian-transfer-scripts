"""
Shared variables throughout scripts.
"""

import yaml

environment_name = "simba_env"

try:
    with open("parameters.yml", "r") as f:
        parameters = yaml.load(f)
except FileNotFoundError:
    pass

