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
 mettre a jour toolbox :
 supprimer la version que vous avez et installer la derniere version depuis se systeme

 installer toolbox : 
 suivez les consignes et tout se passera bien
 toolbox s'installe au meme emplacement que toolbox_setup

""")




def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def install_toolbox():
    system = platform.system()
    if system == "Windows":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_win.py", "toolbox_win.py")
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_maj.py", "toolbox_maj.py")
        os.system("pip install colorama")
        print("toolbox_win.py a été récupéré depuis GitHub.")
        print("installation terminé !")
    elif system == "Linux":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_linux.py", "toolbox_linux.py")
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_maj.py", "toolbox_maj.py")
        os.system("pip install colorama")
        print("toolbox_linux.py a été récupéré depuis GitHub.")
        print("installation terminé !")
    else:
        print("Système non pris en charge. recommencez lorsque votre systeme sera pris en charge")
        return

    print("quelle version souhaitez vous installer en plus ? linux/win/aucun")
    optional_os = input(">>>")

    if optional_os =="win":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_win.py", "toolbox_win.py")
        print("toolbox_win.py a été récupéré depuis GitHub.")
        print("installation terminé !")

    elif optional_os == "linux":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_linux.py", "toolbox_linux.py")
        print("toolbox_linux.py a été récupéré depuis GitHub.")
        print("installation terminé !")

    elif optional_os =="aucun":
        print(BANNER)
    
    else:
        print("Système non pris en charge. recommencez lorsque se systeme sera pris en charge\n")

os_sys = platform.system()


if __name__ == "__main__":
    print(BANNER)
    print("bienvenu sur toolbox setup, vous pouvez installer ou mettre a jour toolbox ici")
    
    while True:
        print("lancer le telechargement de toolbox version ", os_sys, "\n\noui/non/supprimer")
        print("help si vous êtes perdu\n")
        download = input(">>>")
        
        if download =="oui":
            print(BANNER)
            install_toolbox()
            
        elif download =="non":
            break

        elif download =="help":
            print(BANNER)
            print(Help)

        elif download =="supprimer":
            if os.path.exists("toolbox_win.py"):
                os.remove("toolbox_win.py")

            if os.path.exists("toolbox_linux.py"):
                os.remove("toolbox_linux.py")

        else:
            print(" je n'ai pas compris veuillez recommancer")
            time.sleep(2)
            print(BANNER)
