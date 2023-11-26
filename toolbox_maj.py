#!/usr/bin/env python

import os
import time
import sys
import platform
import subprocess
import urllib.request

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def install_toolbox():
    system = platform.system()
    if system == "Windows":
        fichier ="toolbox_win.py"

        if os.path.exists(fichier):
            os.remove(fichier)
            time.sleep(0.5)
            fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_win.py", "toolbox_win.py")
            print("toolbox_win.py a été récupéré depuis GitHub.")
            print("installation terminé !")
        else:
            print("Le fichier n'existe pas.")
        
    elif system == "Linux":
        fichier ="toolbox_linux.py"

        if os.path.exists(fichier):
            os.remove(fichier)
            time.sleep(0.5)
            fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_linux.py", "toolbox_linux.py")
            print("toolbox_linux.py a été récupéré depuis GitHub.")
            print("installation terminé !")
        else:
            print("Le fichier n'existe pas.")
            
    else:
        print("Système non pris en charge. recommencez lorsque votre systeme sera pris en charge")
        return

