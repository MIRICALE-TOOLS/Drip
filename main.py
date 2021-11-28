##Imports
import requests, os, ctypes, json, pyperclip, time
from colorama import Fore, init


##Global Variables
orange = Fore.YELLOW
yellow = Fore.LIGHTYELLOW_EX
cyan = Fore.LIGHTCYAN_EX
blue = Fore.CYAN
red = Fore.LIGHTRED_EX
green = Fore.LIGHTGREEN_EX
reset = Fore.RESET
cmd = os.system

##Convert Colorama for Windows Command Processors
init(convert=True)


##CLI Logo
def logo():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("API Dawg V0.7")
    print(yellow +"""
                      ___  ______ _____  ______  ___  _    _ _____ 
                     / _ \ | ___ \_   _| |  _  \/ _ \| |  | |  __ \\
                    / /_\ \| |_/ / | |   | | | / /_\ \ |  | | |  \/
                    |  _  ||  __/  | |   | | | |  _  | |/\| | | __ 
                    | | | || |    _| |_  | |/ /| | | \  /\  / |_\ \\
                    \_| |_/\_|    \___/  |___/ \_| |_/\/  \/ \____/
                                               
                                               
    """ + reset)


##Main Menu
def menu():
    logo()
    motd()
    print(f"""
    [{red}1{reset}] URL Shortener 
    [{green}2{reset}] Discord ID Lookup
    [{blue}3{reset}] Discord Token Login Helper
    [{red}4{reset}] Social Media Hunter
    [{green}?{reset}] About
    [{blue}X{reset}] Exit
    """)
    
    choice = input("")


    if choice == '1':
        urlshort()


    elif choice == '2':
        discordlookup()


    elif choice == '3':
        dtlh()


    elif choice == '4':
        smhunter()


    elif choice == '?':
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


##Message of the Day (Random Anime Quotes)
def motd():
    url = "https://animechan.vercel.app/api/random"
    payload={}
    headers = {}

    r = requests.request("GET", url, headers=headers, data=payload)
    response = r.json()

    print(response['quote']+" - "+response['character'])


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
        menu()


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
        menu()


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
        menu()


    elif choice == '<':
        menu()


    else:
        urlshort()


##Discord ID Lookup
def discordlookup():
    logo()

    id = input('Discord ID: ')


    if id == '<':
        menu()
    
    
    else:
        url = f"https://api.leaked.wiki/discorduser?json=yes&id={id}"
        payload = {}
        headers = {'Content-Type': 'text/plain'}

        r = requests.request("GET", url, headers=headers, data=payload)
        response = r.json()

        print('Username: ' + response['username'] + '#' + response['discriminator'])
        print('Avatar URL: ' + response['avatar'])

        time.sleep(5)
        menu()


##Discord Token Login Helper
def dtlh():
    logo()
    token = input('Discord Token: ')
    script = """function login(token) {
    setInterval(() => {
    document.body.appendChild(document.createElement `iframe`).contentWindow.localStorage.token = `"${token}"`
    }, 50);
    setTimeout(() => {
    location.reload();
    }, 0);
    }
    login(""" + "\"" + token + "\")"
    pyperclip.copy(script)
    logo()
    print("Script Copied To Clipboard, Paste It In The Console In Discord!")
    time.sleep(3)
    menu()


##Social Media Hunter (OSINT Tool)
def smhunter():
    logo()
    name = input('Username: ')
    logo()
    print(f'Opening Possible Social Media Pages for {name}!\n')


    print('Opening TikTok...')
    cmd(f'start https://www.tiktok.com/@{name}')


    print('Opening GitHub...')
    cmd(f'start https://www.github.com/{name}')


    print('Opening Twitter...')
    cmd(f'start https://www.twitter.com/{name}')


    print('Opening Twitch...')
    cmd(f'start https://www.twitch.tv/{name}')


    print('Opening YouTube...')
    cmd(f'start https://www.youtube.com/c/{name}')


    print('Opening Roblox...\n')
    cmd(f'start https://www.roblox.com/search/users?keyword={name}')


    print('Done! Please check your webbrowser for results.')
    time.sleep(3)
    menu()


##Main Thread
menu()
