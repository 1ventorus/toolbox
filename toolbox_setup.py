#!/usr/bin/env python

import os
import time
import sys
import platform
import subprocess
import urllib.request


BANNER =("""
     ███  ▄▄  ▄██████▄   ▄██████▄   ▄█       ▀█████████▄   ▄██████▄  ▀████    ▐████▀ 
 ▀██████████ ███    ███ ███    ███ ███         ███    ███ ███    ███   ███▌   ████▀  
    ▀███▀▀██ ███    ███ ███    ███ ███         ███    ███ ███    ███    ███  ▐███    
     ███   ▀ ███    ███ ███    ███ ███        ▄███▄▄▄██▀  ███    ███    ▀███▄███▀    
     ███     ███    ███ ███    ███ ███       ▀▀███▀▀▀██▄  ███    ███    ████▀██▄     
     ███     ███    ███ ███    ███ ███         ███    ██▄ ███    ███   ▐███  ▀███    
     ███     ███    ███ ███    ███ ███▌    ▄   ███    ███ ███    ███  ▄███     ███▄  
    ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ ▄█████████▀   ▀██████▀  ████       ███▄ 
  
  ┌─┐┌─┐┌┬┐┬ ┬┌─┐
  └─┐├┤  │ │ │├─┘
  └─┘└─┘ ┴ └─┘┴  
  
""")

Help = ("""
 installer toolbox : 
 suivez les consignes et tout se passera bien
 toolbox s'installe au meme emplacement que toolbox_setup
 avec tout les requierments

""")

os_sys = platform.system()
if os_sys =="Windows":
    clear ="cls"

elif os_sys =="Linux":
    clear ="clear"

else:
    clear ="erreur"

def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def install_toolbox():
    os.system(clear)
    print(BANNER)
    system = platform.system()
    
    if system == "Windows":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_win.py", "toolbox_win.py")
    
    elif system == "Linux":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_linux.py", "toolbox_linux.py")
    
    else:
        print("Système non pris en charge. recommencez lorsque votre systeme sera pris en charge")
        return

def install_requierment():
    fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_maj.py", "toolbox_maj.py")
               
    fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/save_config.txt", "save_config.txt")
    os.system("pip install colorama")
    
def uninstall():
    os.system(clear)
    print(BANNER)
    if os.path.exists("toolbox_win.py"):
        os.remove("toolbox_win.py")

    if os.path.exists("toolbox_linux.py"):
        os.remove("toolbox_linux.py")

    if os.path.exists("toolbox_maj.py"):
        os.remove("toolbox_maj.py")


if __name__ == "__main__":
    os.system(clear)
    print(BANNER)
    while True:
        
        print("lancer le telechargement de toolbox version ", os_sys, "\n\noui/non/supprimer")
        print("help si vous êtes perdu\n")
        download = input(">>>")
        
        if download =="oui":
            try:
                install_requierment()
                install_toolbox()
                os.system("python toolbox_config.py")


            except OSError:
                print("pas de connection internet, veuillez vous connecter")
            
        elif download =="non":
            break

        elif download =="help":
            print(Help)

        elif download =="supprimer":
            uninstall()
        else:
            print("je n'ai pas compris veuillez recommencer")
            time.sleep(2)
