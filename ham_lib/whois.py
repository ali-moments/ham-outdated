import sys
import requests
from colorama import Fore
import time

def __start__():
    try:
        print(Fore.YELLOW+"\n [!] Whois . . . \n")
        print(Fore.RED+" [!] Plase Enter Domain/IP \n")
        print(Fore.YELLOW+" [!] Enter Exit To Go To Main Menu \n")
        inp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Whois"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
        if inp == "exit" or inp == "Exit" or inp == "EXIT":
            try:
                return
            except:
                return
        result = requests.get('http://api.hackertarget.com/whois/?q=' + inp).text
        print(Fore.BLUE+result)
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+" Press Enter To Go Back To Menu ")
        except:
            print("\n sorry, there is a problem")
            time.sleep(2)
            sys.exit()
    except:
        print(" ")
