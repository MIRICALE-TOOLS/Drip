##Imports
import requests, os, ctypes, json, pyperclip, time
from colorama import Fore, init

##Global Variables
cmd = os.system
color = Fore
p = print
##Convert Colorama for Windows Command Processors
init(convert=True)

##CLI Logo
def logo():
    cmd('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("API Dawg V0.5")
    p(color.YELLOW +"""
      ___  ______ _____  ______  ___  _    _ _____ 
     / _ \ | ___ \_   _| |  _  \/ _ \| |  | |  __ \\
    / /_\ \| |_/ / | |   | | | / /_\ \ |  | | |  \/
    |  _  ||  __/  | |   | | | |  _  | |/\| | | __ 
    | | | || |    _| |_  | |/ /| | | \  /\  / |_\ \\
    \_| |_/\_|    \___/  |___/ \_| |_/\/  \/ \____/
                                               
                                               
    """ + color.LIGHTYELLOW_EX)

##CLI Menus
def menu():
    logo()
    p("""
    [1] Module List
    [2] About
    [X] Exit
    """)
    choice = input("")
    if choice == '1':
        modules()
    elif choice == '2':
        p("coming soon")
        menu()
    elif choice == 'x':
        exit
    else:
        menu()

def modules():
    logo()
    p("""
    [1] URL Shortner
    [2] Password Generator
    [3] Discord ID Lookup
    [<] Go Back
    """)
    choice = input("")
    if choice == '1':
        urlshort()
    elif choice == '2':
        modules()
    elif choice == '3':
        modules()
    elif choice == '<':
        menu()

##URL Shortner
def urlshort():
    link = input("URL: ")
    url = "https://owo.vc/generate"
    data = {"link": f"{link}",
    "generator": "owo",
    "preventScrape": "true",
    "owoify": "true"}
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    response = r.json()
    print("Shortened URL (Copied to Clipboard): " + response['result'])
    pyperclip.copy(response['result'])
    time.sleep(3)
    modules()
menu()
