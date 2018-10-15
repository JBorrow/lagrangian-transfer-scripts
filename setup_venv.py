"""
Sets up the virtual environment with the correct packages.
"""

import shared_variables

import subprocess
import os

print("Cloning Lagrangian Transfer")
subprocess.call(
    [
        "git", "clone",
        "https://github.com/JBorrow/lagrangian-transfer.git"
    ]
)

print("Cloning caesar")
subprocess.call(
    [
        "hg", "clone",
        "https://JBorrow@bitbucket.org/laskalam/caesar"
    ]
)

print(f"Creating virtual environment {shared_variables.environment_name}")
subprocess.call(
    [
        "python3",
        "-m",
        "venv",
        shared_variables.environment_name
    ]
)

print("Installing pypi packages")
subprocess.call(
    [
        f"{shared_variables.environment_name}/bin/pip",
        "install",
        "cython", "numpy", "matplotlib", "scipy", "h5py"
    ]
)

def install(path):
    print(f"Installing local package at {path}")
    current_path = os.getcwd()
    os.chdir(path)
    subprocess.call(
        [
            f"{current_path}/{shared_variables.environment_name}/bin/pip",
            "install",
            "-e",
            "."
        ]
    )
    os.chdir("..")

install("caesar")
install("lagrangian-transfer")

