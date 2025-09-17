import os
import subprocess
import time
import webbrowser
#import requests
import winreg

git_dir = r"C:\Users\Airami\OneDrive\Desktop\Programacion_de_redes"
repos = [name for name in os.listdir(git_dir)
         if os.path.isdir(os.path.join(git_dir, name)) and
         os.path.exists(os.path.join(git_dir, name, ".git"))]


if repos:
    print("Found the following GitHub repositor")
    for idx, repo in enumerate(repos, 1):
        print(f"{idx}, {repo}")

    else:
        print("No Git Hub repositiries found in")
        print("Please provide a GitHub repository")