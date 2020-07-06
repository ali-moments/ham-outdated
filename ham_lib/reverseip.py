import os
import requests
import json
from colorama import Fore
import sys
import time

def __start__():
    try:
        print(Fore.YELLOW+"\n [!] Reverse IP . . . ")
        print(Fore.RED+"\n [!] Enter The Domain/ip\n")
        print(Fore.YELLOW+" [!] Enter Exit To Go To Main Menu")
        website = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Reverse_IP"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
        if website == "exit" or website == "Exit" or website == "EXIT":
            try:
                return
            except:
                return
        mysite = {"remoteAddress":website}
        link = requests.post("https://domains.yougetsignal.com/domains.php" , mysite)
        source = json.loads(link.content)
        print(source)
        for data in source["domainArray"]:
            print(" "+data[0]+"\n")
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+"Press Enter To Go Back To Menu ")
        except:
            print("\n sorry, there is a problem")
            time.sleep(2)
            sys.exit()
    except:
        print(" ")
