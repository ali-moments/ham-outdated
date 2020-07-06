import requests
import os
import sys
import ipapi
from colorama import Fore
import time

def __start__():
    print(Fore.YELLOW+"\n [!] IP Location . . . \n")
    print(Fore.RED+" [!] Enter IP Address \n")
    print(Fore.YELLOW+" [!] Press Enter Key For Info Of Ur IP \n")
    print(Fore.RED+" [!] Enter Exit To Go To Main Menu \n")
    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"IP-Location"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    if site == "exit" or site == "Exit" or site == "EXIT":
        try:
            return
        except:
            return
    source = ipapi.location(ip=site, key=None, field=None)
    try:
        print(Fore.GREEN+" [!]"+Fore.RED+" Captured Informations =>")
        print (Fore.GREEN+" [!]"+Fore.LIGHTRED_EX+" ip = "+ source["ip"])
        print (Fore.GREEN+" [!]"+Fore.LIGHTRED_EX+" city = " + source["city"])
        print (Fore.GREEN+" [!]"+Fore.LIGHTRED_EX+" region = "+ source["region"])
        print (Fore.GREEN+" [!]"+Fore.LIGHTRED_EX+" id country = "+source["country"])
        print (Fore.GREEN+" [!]"+Fore.LIGHTRED_EX+" country = "+ source["country_name"])
        print (Fore.GREEN+" [!]"+Fore.LIGHTRED_EX+" Calling Code = "+source["country_calling_code"])
        print (Fore.GREEN+" [!]"+Fore.LIGHTRED_EX+" Languages = "+source["languages"])
        print (Fore.GREEN+" [!]"+Fore.LIGHTRED_EX+" org = "+ source["org"])
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+" Press Enter To Go Back To Menu ")
        except:
            print("\n sorry, there is a problem")
            time.sleep(2)
            sys.exit()
    except:
        print(Fore.RED+" [!]"+Fore.YELLOW+" Error : No Data Captured")
