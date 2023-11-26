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

def launch():
    load=1
    if load !=5:
            load =+1
            os.system("cls")
            print(BANNER)
            print("telechargement")
            time.sleep(0.5)
            os.system("cls")
            print(BANNER)
            print("telechargement.")
            time.sleep(0.5)
            os.system("cls")
            print(BANNER)
            print("telechargement..")
            time.sleep(0.5)
            os.system("cls")
            print(BANNER)
            print("telechargement...")
            time.sleep(0.5)
    load =-4
    os.system("cls")
    print(BANNER)

def loading():
    launch()
    launch()
    launch()
    launch()


def fetch_file(url, filename):
    urllib.request.urlretrieve(url, filename)

def install_toolbox():
    system = platform.system()
    if system == "Windows":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toobox.py", "toolbox_win.py")
        loading()
        print("toolbox_win.py a été récupéré depuis GitHub.")
        print("installation terminé !")
    elif system == "Linux":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_linux.py", "toolbox_linux.py")
        loading()
        print("toolbox_linux.py a été récupéré depuis GitHub.")
        print("installation terminé !")
    else:
        print("Système non pris en charge. recommencez lorsque votre systeme sera pris en charge")
        return

    print("quelle version souhaitez vous installer en plus ? linux/win/aucun")
    optional_os = input(">>>")

    if optional_os =="win":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toobox.py", "toolbox_win.py")
        loading()
        print("toolbox_win.py a été récupéré depuis GitHub.")
        print("installation terminé !")

    elif optional_os == "linux":
        fetch_file("https://raw.githubusercontent.com/1ventorus/toolbox/main/toolbox_linux.py", "toolbox_linux.py")
        loading()
        print("toolbox_linux.py a été récupéré depuis GitHub.")
        print("installation terminé !")
    
    else:
        print("Système non pris en charge. recommencez lorsque se systeme sera pris en charge")

os_sys = platform.system()


if __name__ == "__main__":
    os.system("cls")
    print(BANNER)
    print("bienvenu sur toolbox setup, vous pouvez installer ou mettre a jour toolbox ici")
    
    while True:
        print("lancer le telechargement de toolbox version ", os_sys, "\n oui/non")
        print("help si vous êtes perdu")
        download = input(">>>")
        
        if download =="oui":
            os.system("cls")
            print(BANNER)
            install_toolbox()
            
        elif download =="non":
            break

        elif download =="help":
            os.system("cls")
            print(BANNER)
            print(Help)

        else:
            print(" je n'ai pas compris veuillez recommancer")
            time.sleep(2)
            os.system("cls")
            print(BANNER)

os.system("cls")
