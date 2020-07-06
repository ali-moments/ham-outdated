import sys
import requests
from colorama import Fore
import time
import os
def __start__():
    print(Fore.RED+" [!] DnsLookup . . . \n")
    print(Fore.RED+" [!] Enter The Domain\n")
    print(Fore.RED+" [!] Enter Exit To Go To Main Menu \n")
    target = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"NS-Lookup"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    if target == "exit" or target == "Exit" or target == "EXIT":
        try:
            return
        except:
            return
    result = requests.get('http://api.hackertarget.com/dnslookup/?q=' + target).text
    print(Fore.LIGHTBLUE_EX+result)
    try:
        input(Fore.GREEN+" [*] Press Enter To Go Back To Menu")
    except:
        print("\n sorry,there is a problem")
        time.sleep(2)
        sys.exit()
