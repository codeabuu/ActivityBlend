import subprocess
import sys
import get_pip
import os
import importlib
import contextlib

def install(package):
    subprocess.call([sys.executable, "-m", "pip", "install", package])

required = []
failed = []

try:
    file = open("requirements.txt", "r")
    file_lines = file.readlines()
    required = [line.strip().lower() for line in file_lines]
    file.close()