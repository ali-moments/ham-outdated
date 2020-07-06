import requests, builtwith
from colorama import Fore
import sys
import os
import time
def __start__():
    print(Fore.RED+"[!] CMS ...")
    print(Fore.RED+" [!] Enter Domain \n")
    print(Fore.RED+" [!] Enter Exit To Go To Main Menu \n")
    target = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"CMS-Detect"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    if target == "exit" or target == "Exit" or target == "EXIT":
        try:
            return
        except:
            return
    if not 'https://' in target or not 'http://' in target:
        target = 'http://'+target
    info = builtwith.parse(target)
    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val)
        print(Fore.BLUE+"\n"+name+': '+value)
    try:
        input(Fore.GREEN+" [*] Press Enter To Go Back To Menu ")
    except:
        print("\n sorry,there is a problem")
        time.sleep(2)
        sys.exit()
