#!/usr/bin/env python

# import
import os
import time
import sys
import subprocess
import socket
import ctypes
import threading
import uuid
import platform

# initialisation du code
def launch():
    load=1
    if load !=5:
            load =+1
            os.system("cls")
            print("chargement")
            time.sleep(0.5)
            os.system("cls")
            print("chargement.")
            time.sleep(0.5)
            os.system("cls")
            print("chargement..")
            time.sleep(0.5)
            os.system("cls")
            print("chargement...")
            time.sleep(0.5)
    load =-4

def loading():
    launch()
    launch()

loading()
os.system("pip install colorama")

from colorama import*

# mise en place des couleur
couleur = Fore.MAGENTA
command_colors= Fore.RED

print(couleur)

# affichage
BANNER =("""
     ███  ▄▄  ▄██████▄   ▄██████▄   ▄█       ▀█████████▄   ▄██████▄  ▀████    ▐████▀ 
 ▀██████████ ███    ███ ███    ███ ███         ███    ███ ███    ███   ███▌   ████▀  
    ▀███▀▀██ ███    ███ ███    ███ ███         ███    ███ ███    ███    ███  ▐███    
     ███   ▀ ███    ███ ███    ███ ███        ▄███▄▄▄██▀  ███    ███    ▀███▄███▀    
     ███     ███    ███ ███    ███ ███       ▀▀███▀▀▀██▄  ███    ███    ████▀██▄     
     ███     ███    ███ ███    ███ ███         ███    ██▄ ███    ███   ▐███  ▀███    
     ███     ███    ███ ███    ███ ███▌    ▄   ███    ███ ███    ███  ▄███     ███▄  
    ▄████▀    ▀██████▀   ▀██████▀  █████▄▄██ ▄█████████▀   ▀██████▀  ████       ███▄ 
                                                                                  
  _________________________________________________________________
 |       toute les commandes d'info du cmd fonctionnent !          |
 |                                                                 |
 | paramètre : affiche les paramètre                               |
 | IPinfo : donne toute les info ip de la machine                  |
 | MACinfo : donne toute les info MAC de la machine                |
 | aide : affiche plus de commande                                 |
 | clear : même fonction que 'cls' mais garde l'interface          |
 | close : ferme le cmd personnalisé                               |
 |_________________________________________________________________|

 """)

aide = ("""
  ____>>>toolox/aide<<<____________________________________________________
 |           toute les commandes d'info du cmd fonctionnent !              |
 |                                                                         |
 | paramètre : affiche les paramètre                                       |
 | chat : permet de discuter avec soi même                                 |
 | IPinfo : donne toute les info ip de la machine                          |
 | MACinfo : donne toute les info MAC de la machine                        |
 | os : donne le systeme d'exploitation (os) de la machine                 |
 | ipconfig/all : donne les info sur le materiel                           |
 | nslookup 'cite recherché' : donne l'adresse ip du cite                  |
 | tracert 'cite recherché' : détermine le chemin d'une info vers le cite  |
 | ping 'cite recherché' : calcul le temps de voyage de l'info vers le cite|
 | help : affiche l'aide du cmd                                            |
 | dir : affiche la liste des fichier du répertoire                        |
 | curl ipinfo.io : donne l'adrese ip public                               |  
 | clear : même fonction que 'cls' mais garde l'interface                  |
 | close : ferme le cmd personnalisé                                       |
 | credits : affiche les crdits ainsi que la version du systeme            |
 |_________________________________________________________________________| 

 """)

gen_parameters=("""
  ____>>>toolox/paramètre<<<_______________________________________________
 |                                                                         |
 | couleur : change la couleur de l'interface                              |
 | commande : accede au parametre des commandes                            |
 | info systeme : donne les totute les info de toolbox                     |
 | close : retourne dans toolbox                                           |
 |_________________________________________________________________________|
 """)

command_sys=("""
  ____>>>toolox/paramètre/commande<<<______________________________________
 |                                                                         |
 | couleur : change la couleur des commandes                               |
 | linux : modifie le texte de commande pour celui de linux                |
 | win : modifie le texte de commande pour celui de windows                |
 | defaut : modifie le texte de commande pour celui par défaut de toolbox  |
 | back : revient au parametre generaux                                    |
 |_________________________________________________________________________|
 """)

cred=("""
 credits : 
 conception : 1ventorus

 merci de me contacter pour plus d'info a l'adresse mail suivante
    1ventorus@gmail.com
 """)

new=("""
 version actuel de toolbox :
    beta 0.10.8
 
 dernier ajout :
    -couleur suplementaire et info sur les couleur possible
    -ajout de info systeme
    -modifcation du systeme des couleur
    -ajout d'info utile dans le code source
 """)

# fonction complex
def TEXT_DELAY(TEXT, DELAY):
    for CHAR in TEXT:
        print(CHAR, end='', flush=True)
        time.sleep(DELAY)
    print()

def hall1():
    os.system("cls")
    TEXT_DELAY(couleur + BANNER, 0.004)
    print("vous êtes acutellement sur le disque :\n")
    os.system("cd")
    print()

def hall():
    os.system("cls")
    print(couleur + BANNER)
    print("vous êtes acutellement sur le disque :\n")
    os.system("cd")
    print()

def General_Parameters():
    os.system("cls")
    print(couleur + gen_parameters)
    print()
    print("modifier les paramètres de toolbox")
    print()

def Command_Parameters():
    os.system("cls")
    print(couleur + command_sys)
    print()
    print("modifier les paramètres de commande de toolbox")
    print()

def get_ipv4_address():
    # Obtention de l'adresse IPv4
    ip = socket.gethostbyname(socket.gethostname())
    return ip

def get_ipv6_address():
    # Obtention de l'adresse IPv6
    ip = [l for l in ([ip for ip in socket.getaddrinfo(socket.gethostname(), None) if ':' in ip[4][0]]) if l]
    return ip[0][4][0] if ip else None

def get_mac_address():
    # Obtention de l'adresse MAC
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8 * 6, 8)][::-1])
    return mac

def close():
    load3=1
    if load3 !=5:
            load =+1
            os.system("cls")
            print("fermeture")
            time.sleep(0.5)
            os.system("cls")
            print("fermeture.")
            time.sleep(0.5)
            os.system("cls")
            print("fermeture..")
            time.sleep(0.5)
            os.system("cls")
            print("fermeture...")
            time.sleep(0.5)
    load3 =-4

def closing():
    close()
    close()
    print(Style.RESET_ALL)
    close()
    close()

# variable d'association
ipv4 =get_ipv4_address()
ipv6 =get_ipv6_address()
mac_adress =get_mac_address()

# systeme de commande
entry =">>> "
linux_command=("""
 ┌─[toolbox 0.10.8]─[administrator tool]─[~]
 └──╼[★]$>>> """)
win_command=os.getcwd() + ">>>"       # os.getcwd() permet d'obtenir la position sous format str 

# finalisation de linitialisation
loading()
hall1()

# programme
while True:

    command =input(command_colors + entry)
    print(couleur)

 # parametre
    if command =="parametre":
        General_Parameters()
        while True:
            control = input(command_colors + entry)
  # couleur general
            if control == "couleur":
                General_Parameters()
                print(couleur +"quelle couleur ? vert/jaune/rouge/majenta/cyan/blanc/bleu/violet/rose")
                color = input(command_colors + entry)

                if color == "jaune": 
                    Command_Parameters()
                    couleur = Fore.YELLOW
                    
                elif color == "vert":
                    couleur = Fore.GREEN
                    Command_Parameters()

                elif color == "blanc":
                    couleur = Fore.WHITE
                    Command_Parameters()

                elif color == "bleu":
                    couleur = Fore.BLUE
                    Command_Parameters()

                elif color == "majenta":
                    couleur = Fore.MAGENTA
                    Command_Parameters()

                elif color == "rouge":
                    couleur = Fore.RED
                    Command_Parameters()

                elif color == "cyan":
                    couleur = Fore.CYAN
                    Command_Parameters()

                elif color == "violet":
                    couleur = Fore.MAGENTA + Style.DIM
                    Command_Parameters()

                elif color == "rose":
                    couleur = Fore.MAGENTA + Style.BRIGHT
                    command_parameters()

                else:
                    Command_Parameters()
                    print("Cette couleur ne fonctionne pas")

  # parametre de l'entré des commande
            elif control=="commande":
                while True:
                    Command_Parameters()
                    command_system = input(command_colors + entry)
    
    # couleur de commande
                    if command_system == "couleur":
                        print(couleur +"quelle couleur ? vert/jaune/rouge/majenta/cyan/blanc/bleu/violet/rose")
                        color = input(command_colors + entry)

                        if color == "jaune": 
                            command_colors = Fore.YELLOW

                        elif color == "vert":
                            command_colors = Fore.GREEN

                        elif color == "blanc":
                            command_colors = Fore.WHITE

                        elif color == "bleu":
                            command_colors = Fore.BLUE

                        elif color == "majenta":
                            command_colors = Fore.MAGENTA

                        elif color == "rouge":
                            command_colors = Fore.RED

                        elif color == "cyan":
                            command_colors = Fore.CYAN
                            
                        elif color == "violet":
                            command_colors = Fore.MAGENTA + Style.DIM

                        elif color == "rose":
                            command_colors = Fore.MAGENTA + Style.BRIGHT
                        
                        else:
                            print("Cette couleur ne fonctionne pas")
                        
                        Command_Parameters()

    # style visuel commande
                    elif command_system=="linux":
                        entry=linux_command
                        Command_Parameters()
                        break

                    elif command_system=="win":
                        entry=win_command
                        Command_Parameters()
                        break

                    elif command_system=="defaut":
                        entry=">>> "
                        Command_Parameters()
                        break

                    elif command_system=="back":
                        Command_Parameters()
                        break

                    else:
                        print("veuillez recommencer")
                        time.sleep(2)
                        Command_Parameters()

  # maj
            elif control=="maj":
                os.system("pip download colorama")
                print("maj fini, colorama est a jour !")
                time.sleep(4)
                General_Parameters()

  # info systeme
            elif control=="info systeme":
                print(couleur + new)

  # fermeture des parametre
            elif control=="close":
                hall()
                break

  # erreur
            else:
                print("veuillez recommencer")
                time.sleep(2)
                General_Parameters()

 # ip info
    elif command =="IPinfo":
        hall()
        print(command_colors + "ip :\n\n ipv4 : ", ipv4, "\n ipv6 : ", ipv6)

 # mac info
    elif command =="MACinfo":
        hall()
        print(command_colors + "adresse MAC : \n\n", mac_adress)
        print()

 # os info
    elif command =="os":
        hall()
        system_name = os.name
        
        if system_name == "posix":
            print("système d'exploitation Unix")
            pint("cette os correspond a toute les version de linux et macOS")
            unix_version = platform.uname()
            print("Informations sur la version d'Unix :", unix_version)
        
        elif system_name == "nt":
            print("système d'exploitation Windows")
            windows_version = platform.version()
            print("Version de Windows :", windows_version)
        
        else:
            print("Système d'exploitation non reconnu.")

 # systeme chat
    elif command =="chat":
        hall()
        while True:
           
            chat = input(couleur + "que voulez vous dire ? ")

            if chat == chat:
                hall()
                print(couleur + chat)

            if chat =="clear":
                hall()

            if chat =="exit":
                hall()
                break

 # help
    elif command =="aide":
        os.system("cls")
        print(couleur + aide)

 # clear
    elif command =="clear":
        hall()

 # credits
    elif command =="credits":
        hall()
        print(couleur + cred)
        print("")
 
 # extinction systeme
    elif command =="close":
        os.system("cls")
        closing()
        os.system("cls")
        print("au revoir !")
        time.sleep(2)
        os.system("cls")
        break

 # commande de cmd
    elif command == command:
        hall()
        print(command_colors + "\n>>> " + command + "\n")
        os.system(command)