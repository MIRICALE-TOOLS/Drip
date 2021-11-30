##Imports
import requests, os, ctypes, json, pyperclip, time, webbrowser
from colorama import Fore, init
from urllib.request import urlopen

from requests.models import Response


##Global Variables
orange = Fore.YELLOW
yellow = Fore.LIGHTYELLOW_EX
cyan = Fore.LIGHTCYAN_EX
reset = Fore.RESET
cmd = os.system
web = webbrowser
red = Fore.LIGHTRED_EX
grn = Fore.LIGHTGREEN_EX
uid1 = 'SnowyJX'
uid2 = 'HJKILOP'
uid3 = 'asdfsvtr'
uid4 = ''
uid5 = ''
key1 = 'EWE8Y1jxg77R3XfDWwof86CBDgwSIvxAVF1bCL7uaw4bszRL'
key2 = 'yQQfj55Ewvl46AZfDsgkWeruZSPeg2x095YIeHQTHTneni2V'
key3 = 'KrQWPLOLWqVBYBiFVQBl4Gren4Y5ScYlRpAPbsYS2uCoqIWd'
key4 = ''
key5 = ''  

##Convert Colorama for Windows Command Processors
init(convert=True)


##CLI Logo
def logo():
    os.system('cls')
    ctypes.windll.kernel32.SetConsoleTitleW("Drip - V0.9")
    print(cyan +"""
                                                     
      ##### ##                                   
   /#####  /##                  #                
 //    /  / ###                ###               
/     /  /   ###                #                
     /  /     ###                                
    ## ##      ## ###  /###   ###        /###    
    ## ##      ##  ###/ #### / ###      / ###  / 
    ## ##      ##   ##   ###/   ##     /   ###/  
    ## ##      ##   ##          ##    ##    ##   
    ## ##      ##   ##          ##    ##    ##   
    #  ##      ##   ##          ##    ##    ##   
       /       /    ##          ##    ##    ##   
  /###/       /     ##          ##    ##    ##   
 /   ########/      ###         ### / #######    
/       ####         ###         ##/  ######     
#                                     ##         
 ##                                   ##         
                                      ##         
                                       ##        
                                               
 Coded by: xshonda#9999 | github.com/xshonda                                   
    """ + reset)


##Main Menu
def menu():
    logo()
    motd()

    blu = Fore.CYAN
    red = Fore.LIGHTRED_EX
    grn = Fore.LIGHTGREEN_EX
    r = Fore.RESET

    print(f"""
    [{red}1{r}] URL Shortener 
    [{grn}2{r}] Discord ID Lookup
    [{blu}3{r}] Discord Token Login Helper
    [{red}4{r}] Social Media Hunter
    [{grn}5{r}] Rust Code Checker
    [{blu}6{r}] File/Paste Sniper
    [{red}7{r}] BIN Lookup
    [{grn}?{r}] About
    [{blu}X{r}] Exit
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


    elif choice == '5':
        rustcodechecker()


    elif choice == '6':
        dorkaid()


    elif choice == '7':
        binlookup()

    elif choice == '?':
        logo()
        print("""
                I'm making this tool to expand my knowledge on the python language and have fun!


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


##Rust Code Checker
def rustcodechecker():
    logo()
    pin = input('Code (4 Digit Numerical PIN): ')
    url = 'https://raw.githubusercontent.com/xshonda/The-List/main/codes.txt'
    data = requests.get(url).text
    list = data.splitlines()

    try:
        idx = list.index(pin)


    except ValueError:  # pin is not in list
        idx = -1
        print('Your Code is Strong AF! (Your Code Is Not In The List)')

        time.sleep(5)
        menu()


    else:
        print(f'Your Code Strength Is: {idx}/10000')
        time.sleep(5)
        menu()


##Dork Aid
def dorklogo():
    cmd('cls')
    print(f"""
    {grn}$$$$$$$\   $$$$$$\  $$$$$$$\  $$\   $$\        {red}$$$$$$\  $$$$$$\ $$$$$$$\  
    {grn}$$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |      {red}$$  __$$\ \_$$  _|$$  __$$\ 
    {grn}$$ |  $$ |$$ /  $$ |$$ |  $$ |$$ |$$  /       {red}$$ /  $$ |  $$ |  $$ |  $$ |
    {grn}$$ |  $$ |$$ |  $$ |$$$$$$$  |$$$$$  /        {red}$$$$$$$$ |  $$ |  $$ |  $$ |
    {grn}$$ |  $$ |$$ |  $$ |$$  __$$< $$  $$<         {red}$$  __$$ |  $$ |  $$ |  $$ |
    {grn}$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |\$$\        {red}$$ |  $$ |  $$ |  $$ |  $$ |
    {grn}$$$$$$$  | $$$$$$  |$$ |  $$ |$$ | \$$\       {red}$$ |  $$ |$$$$$$\ $$$$$$$  |
    {grn}\_______/  \______/ \__|  \__|\__|  \__|      {red}\__|  \__|\______|\_______/{reset}
                                                                          
                                                                              
    """)

def dorkaid():
    dorklogo()

    print(f"""

    [{grn}1{reset}] Bing
    [{grn}2{reset}] Google
    [{grn}3{reset}] DuckDuckGo
    [{grn}<{reset}] Go Back
    
    """)
    engine = input('Engine: ')

    if engine == '1':
        bing()


    elif engine == '2':
        google()


    elif engine == '3':
        duckduckgo()

    
    elif engine == '<':
        menu()


    else:
        dorkaid()


def bing():
    dorklogo()
    
    engine = 'https://www.bing.com/search?q='
    
    anonfile = f'{engine}site:anonfile.com%20'
    anonfiles = f'{engine}site:anonfiles.com%20'
    mega = f'{engine}site:mega.nz%20'
    mediafire = f'{engine}site:mediafire.com%20'
    drive = f'{engine}site:drive.google.com%20'

    pastebin = f'{engine}site:pastebin.com%20'
    throwbin = f'{engine}site:throwbin.io%20'
    privatebin = f'{engine}site:privatebin.net%20'
    hatebin = f'{engine}site:hatebin.com%20'
    zerobin = f'{engine}site:0bin.net%20'

    print(f"""
    File Hosting Services 
    [{grn}1{reset}] Anonfile
    [{grn}2{reset}] Mediafire
    [{grn}3{reset}] Google Drive
    [{grn}4{reset}] Mega
    
    Paste Hosting Services
    [{grn}5{reset}] PasteBin
    [{grn}6{reset}] HateBin
    [{grn}7{reset}] ThrowBin
    [{grn}8{reset}] PrivateBin
    [{grn}9{reset}] 0Bin
    """)

    choice = input('Service: ')

    if choice == '1':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{anonfile}{keyword}')
        web.open(f'{anonfiles}{keyword}')
        dorkaid()

    elif choice == '2':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{mediafire}{keyword}')
        dorkaid()
    
    elif choice == '3':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{drive}{keyword}')
        dorkaid()

    elif choice == '4':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{mega}{keyword}')
        dorkaid()

    elif choice == '5':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{pastebin}{keyword}')
        dorkaid()

    elif choice == '6':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{hatebin}{keyword}')
        dorkaid()

    elif choice == '7':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{throwbin}{keyword}')
        dorkaid()

    elif choice == '8':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{privatebin}{keyword}')
        dorkaid()

    elif choice == '9':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{zerobin}{keyword}')
        dorkaid()



def google():
    dorklogo()
    
    engine = 'https://www.google.com/search?q='
    
    anonfile = f'{engine}site:anonfile.com%20'
    anonfiles = f'{engine}site:anonfiles.com%20'
    mega = f'{engine}site:mega.nz%20'
    mediafire = f'{engine}site:mediafire.com%20'
    drive = f'{engine}site:drive.google.com%20'

    pastebin = f'{engine}site:pastebin.com%20'
    throwbin = f'{engine}site:throwbin.io%20'
    privatebin = f'{engine}site:privatebin.net%20'
    hatebin = f'{engine}site:hatebin.com%20'
    zerobin = f'{engine}site:0bin.net%20'

    print(f"""
    File Hosting Services 
    [{grn}1{reset}] Anonfile
    [{grn}2{reset}] Mediafire
    [{grn}3{reset}] Google Drive
    [{grn}4{reset}] Mega
    
    Paste Hosting Services
    [{grn}5{reset}] PasteBin
    [{grn}6{reset}] HateBin
    [{grn}7{reset}] ThrowBin
    [{grn}8{reset}] PrivateBin
    [{grn}9{reset}] 0Bin
    """)

    choice = input('Service: ')

    if choice == '1':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{anonfile}{keyword}')
        web.open(f'{anonfiles}{keyword}')
        dorkaid()

    elif choice == '2':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{mediafire}{keyword}')
        dorkaid()
    
    elif choice == '3':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{drive}{keyword}')
        dorkaid()

    elif choice == '4':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{mega}{keyword}')
        dorkaid()

    elif choice == '5':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{pastebin}{keyword}')
        dorkaid()

    elif choice == '6':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{hatebin}{keyword}')
        dorkaid()

    elif choice == '7':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{throwbin}{keyword}')
        dorkaid()

    elif choice == '8':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{privatebin}{keyword}')
        dorkaid()

    elif choice == '9':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{zerobin}{keyword}')
        dorkaid()

def duckduckgo():
    dorklogo()
    
    engine = 'https://www.duckduckgo.com/search?q='
    
    anonfile = f'{engine}site:anonfile.com%20'
    anonfiles = f'{engine}site:anonfiles.com%20'
    mega = f'{engine}site:mega.nz%20'
    mediafire = f'{engine}site:mediafire.com%20'
    drive = f'{engine}site:drive.google.com%20'

    pastebin = f'{engine}site:pastebin.com%20'
    throwbin = f'{engine}site:throwbin.io%20'
    privatebin = f'{engine}site:privatebin.net%20'
    hatebin = f'{engine}site:hatebin.com%20'
    zerobin = f'{engine}site:0bin.net%20'

    print(f"""
    File Hosting Services 
    [{grn}1{reset}] Anonfile
    [{grn}2{reset}] Mediafire
    [{grn}3{reset}] Google Drive
    [{grn}4{reset}] Mega
    
    Paste Hosting Services
    [{grn}5{reset}] PasteBin
    [{grn}6{reset}] HateBin
    [{grn}7{reset}] ThrowBin
    [{grn}8{reset}] PrivateBin
    [{grn}9{reset}] 0Bin
    """)

    choice = input('Service: ')

    if choice == '1':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{anonfile}{keyword}')
        web.open(f'{anonfiles}{keyword}')
        dorkaid()

    elif choice == '2':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{mediafire}{keyword}')
        dorkaid()
    
    elif choice == '3':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{drive}{keyword}')
        dorkaid()

    elif choice == '4':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{mega}{keyword}')
        dorkaid()

    elif choice == '5':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{pastebin}{keyword}')
        dorkaid()

    elif choice == '6':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{hatebin}{keyword}')
        dorkaid()

    elif choice == '7':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{throwbin}{keyword}')
        dorkaid()

    elif choice == '8':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{privatebin}{keyword}')
        dorkaid()

    elif choice == '9':
        dorklogo()
        keyword = input('Keyword: ')
        web.open(f'{zerobin}{keyword}')
        dorkaid()
    

##BIN Lookup
def binlookup():
    logo()

    bin = input('BIN: ')
    url = 'https://neutrinoapi.net/bin-lookup'
    data = {
        'api-name': 'bin-lookup',
        'bin-number': bin,
        'customer-ip':  '',
        'api-key': key1,
        'user-id': uid1,
    }

    response = requests.post(url, data=data)
    r = response.text
    data = response.json()
    
    logo()
    
    if r == '{"api-error":2,"api-error-msg":"DAILY API LIMIT EXCEEDED"}':
        logo()
        print("Account Limited, Attempting Lookup with Different Account. Switch IPs & Press Any Key to Continue")
        key = input("> ")
        if key == 'a':
            attempt2()
        else:
            attempt2()

    elif r == '{"api-error":4,"api-error-msg":"ACCOUNT OR IP BANNED"}':
        logo()
        print("Your Account or IP has been banned. Check Account Status and Change IP")
        time.sleep(5)
        menu()

    else:
        print("BIN: " + bin)
        print("Type: " + data['card-type'])
        print("Category: " + data['card-category'])
        print("Brand: " + data['card-brand'])
        print("Issuer: " + data['issuer'])
        print("Country: " + data['country'])
        print("")
        print("Lookup Complete, Press Any Key To Continue.")
        key = input(" ")
        if key == '':
            menu()
        else:
            menu()
    

def attempt2():
    logo()

    bin = input('BIN: ')
    url = 'https://neutrinoapi.net/bin-lookup'

    data = {
        'api-name': 'bin-lookup',
        'bin-number': bin,
        'customer-ip':  '',
        'api-key': key2,
        'user-id': uid2,
    }

    response = requests.post(url, data=data)
    r = response.text
    data = response.json()
    
    logo()

    

    if r == '{"api-error":2,"api-error-msg":"DAILY API LIMIT EXCEEDED"}':
        logo()
        print("Account Limited, Attempting Lookup with Different Account. Switch IPs & Press Any Key to Continue")
        key = input(" ")
        if key == 'a':
            attempt3()
        else:
            attempt3()
    elif r == '{"api-error":4,"api-error-msg":"ACCOUNT OR IP BANNED"}':

        print("Your Account or IP has been banned. Check Account Status and Change IP")
        time.sleep(5)
        menu()
    else:
        print("BIN: " + bin)
        print("Type: " + data['card-type'])
        print("Category: " + data['card-category'])
        print("Brand: " + data['card-brand'])
        print("Issuer: " + data['issuer'])
        print("Country: " + data['country'])
        print("")
        print("Lookup Complete, Press Any Key To Continue.")
        key = input(" ")
        if key == 'a':
            menu()
        else:
            menu()


def attempt3():
    logo()
    
    bin = input('BIN: ')
    url = 'https://neutrinoapi.net/bin-lookup'

    data = {
        'api-name': 'bin-lookup',
        'bin-number': bin,
        'customer-ip':  '',
        'api-key': key3,
        'user-id': uid3,
    }
    response = requests.post(url, data=data)
    r = response.text
    data = response.json()
    
    logo()


    if r == '{"api-error":2,"api-error-msg":"DAILY API LIMIT EXCEEDED"}':
        logo()
        print("damn bro, you limited all your accounts? why you looking up so much bins lmao")
        key = input("> ")
        if key == 'a':
            attempt2()
        else:
            attempt2()
    elif r == '{"api-error":4,"api-error-msg":"ACCOUNT OR IP BANNED"}':
        logo()
        print("Your Account or IP has been banned. Check Account Status and Change IP")
        time.sleep(5)
        menu()
    else:
        print("BIN: " + bin)
        print("Type: " + data['card-type'])
        print("Category: " + data['card-category'])
        print("Brand: " + data['card-brand'])
        print("Issuer: " + data['issuer'])
        print("Country: " + data['country'])
        print("")
        print("Lookup Complete, Press Any Key To Continue.")
        key = input("> ")
        if key == 'a':
            menu()
        else:
            menu()
        
##Main Thread
menu()
