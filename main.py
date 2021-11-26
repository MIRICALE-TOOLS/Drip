##Imports
import requests, os, ctypes, json, pyperclip, time
from colorama import Fore, init


##Global Variables
color = Fore


##Convert Colorama for Windows Command Processors
init(convert=True)


##CLI Logo
def logo():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("API Dawg V0.6")
    print(color.YELLOW +"""
      ___  ______ _____  ______  ___  _    _ _____ 
     / _ \ | ___ \_   _| |  _  \/ _ \| |  | |  __ \\
    / /_\ \| |_/ / | |   | | | / /_\ \ |  | | |  \/
    |  _  ||  __/  | |   | | | |  _  | |/\| | | __ 
    | | | || |    _| |_  | |/ /| | | \  /\  / |_\ \\
    \_| |_/\_|    \___/  |___/ \_| |_/\/  \/ \____/
                                               
                                               
    """ + color.LIGHTYELLOW_EX)


##Main Menu
def menu():
    logo()
    motd()
    print("""
    [1] Module List
    [2] About
    [X] Exit
    """)
    
    choice = input("")


    if choice == '1':
        modules()


    elif choice == '2':
        logo()
        print("""
        I'm making this tool to expand my knowledge on the following topics: Web APIs, JSON & Web Requests


                        this tool was developed by: xshonda#9999 | github.com/xshonda
        """)
        time.sleep(10)
        menu()


    elif choice == 'x':
        exit


    else:
        menu()


##Module List
def modules():
    logo()
    print("""
    [1] URL Shortner
    [2] Discord ID Lookup
    [<] Go Back
    """)

    choice = input("")


    if choice == '1':
        urlshort()


    elif choice == '2':
        discordlookup()


    elif choice == '<':
        menu()


    else: 
        modules()


##URL Shortner
def urlshort():
    logo()
    print("""
    [1] owo.vc
    [2] 1pt.co
    [3] cleanuri.com
    [<] Go Back
    """)

    choice = input("Service: ")


    if choice == '1':
        logo()

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


    elif choice == '2':
        logo()

        link = input("URL: ")
        short = input("Custom URL: ")

        url = f"https://api.1pt.co/addURL?long={link}&short={short}"
        payload={}
        headers = {}

        r = requests.request("GET", url, headers=headers, data=payload)
        response = r.json()
        
        print("Shortened URL (Copied to Clipboard): 1pt.co/" + response['short'])

        pyperclip.copy("1pt.co/" + response['short'])
        time.sleep(3)
        modules()


    elif choice == '3':
        logo()

        link = input("URL: ")

        url = "https://cleanuri.com/api/v1/shorten"
        data = {"url": f"{link}"}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        r = requests.post(url, data=json.dumps(data), headers=headers)
        response = r.json()
        
        print("Shortened URL (Copied to Clipboard): " + response['result_url'])

        pyperclip.copy(response['result_url'])
        time.sleep(3)
        modules()


    elif choice == '<':
        modules()


    else:
        urlshort()


def discordlookup():
    logo()

    id = input('Discord ID: ')

    url = f"https://api.leaked.wiki/discorduser?json=yes&id={id}"
    payload = {}
    headers = {'Content-Type': 'text/plain'}

    r = requests.request("GET", url, headers=headers, data=payload)
    response = r.json()

    print('Username: ' + response['username'] + '#' + response['discriminator'])
    print('Avatar URL: ' + response['avatar'])

    time.sleep(5)
    modules()


##Message of the Day (Random Anime Quotes)
def motd():
    url = "https://animechan.vercel.app/api/random"
    payload={}
    headers = {}

    r = requests.request("GET", url, headers=headers, data=payload)
    response = r.json()

    print(response['quote']+" - "+response['character'])


menu()
