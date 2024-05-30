import subprocess
import sys
import get_pip
import os
import importlib
import contextlib

def install(package):
    '''
    Function to install a package using pip
    '''
    subprocess.call([sys.executable, "-m", "pip", "install", package])

# Lists to store required packages and failed installations
required = []
failed = []

# Try to open requirements.txt file and read all required packages
try:
    file = open("requirements.txt", "r")
    file_lines = file.readlines()
    # Extract package names and "strip"
    required = [line.strip().lower() for line in file_lines]
    file.close()
except FileNotFoundError:
    print("[ERROR] No such file found")

# Check if there are packages to install
if len(required) > 0:
    # Prompt user for confirmation to install packages
    if True:
        for package in required:
            try:
                print("[LOG] Looking for", package)
                with contextlib.redirect_stdout(None):
                    __import__(package)
                print("[LOG]", package, "is already installed, so skipping..")
            except ImportError:
                print("[LOG]", package, "not installed")

                try:
                    print("[LOG] Trying to install", package, "using pip")
                    try:
                        import pip
                    except:
                        print("[EXCEPTION] Pip is not installed")
                        print("[LOG] Installing pip..")
                        get_pip.main()
                        print("[LOG] Pip has been installed")
                    
                    print("[LOG] Installing", package)
                    install(package)
                    with contextlib.redirect_stdout(None):
                        __import__(package)
                    print("[LOG]", package, "has been installed, smilee")
                except Exception as e:
                    print("[ERROR] Could not install", package, "-", e)
                    failed.append(package)
    else:
        print("[STOP] Operation terminated by the user")
else:
    print("[LOG] No packages to install")       