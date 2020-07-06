#!/usr/bin/env python3
import sys
import socket
import os
import time
from ham_menu import mainapp
from ham_lib import cms
from ham_lib import Traceroute
from ham_lib import reverseip
from ham_lib import portscan
from ham_lib import iplocation
from ham_lib import httpheader
from ham_lib import findsharedns
from ham_lib import whois
from ham_lib import dnslookup
from ham_lib import robots
from ham_lib import finder
from ham_lib import cloudflare
from ham_lib import wordpress

try:
    from colorama import Fore
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install colorama\n
    sudo -H pip3 install colorama
        """)

try:
    import requests
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install requests\n
    sudo -H pip3 install requests
        """)

try:
    import ipapi
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install ipapi\n
    sudo -H pip3 install ipapi
        """)

try:
    import builtwith
except:
    os.system("clear")
    print(Fore.RED+"""\n Please Install builtwith\n
    sudo -H pip3 install builtwith
        """)

while True:

    try:
        mainapp.Banner()
        mainapp.infolist1()
        number = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    except:
        print("sorry, there is a problem...")
        time.sleep(1)
        sys.exit()
    if number == '4':
        time.sleep(0.5)
        print("Thnaks for choosing H.A.M ...")
        time.sleep(0.6)
        print("good luck")
        sys.exit()

    elif number == "3":
        mainapp.infolist3()

    elif number == "":
        print(Fore.RED+" [!]"+Fore.YELLOW+" Wrong input, empty field \n press enter to continue...")
        input("")

    elif number == '1':
        try:
            mainapp.Banner()
            mainapp.infolist2()
            infor = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"Information Gathering"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")

            if infor == "1":
                mainapp.Banner()
                cloudflare.__start__()

                #####################

            elif infor == "2":
                mainapp.Banner()
                cms.__start__()

                #####################

            elif infor == "3":
                mainapp.Banner()
                Traceroute.__start__()

                #####################

            elif infor == "4":
                mainapp.Banner()
                reverseip.__start__()

                #####################

            elif infor == "5":
                mainapp.Banner()
                portscan.__start__()

                #####################

            elif infor == "6":
                mainapp.Banner()
                iplocation.__start__()

                #####################

            elif infor == "7":
                mainapp.Banner()
                httpheader.__start__()

                #####################

            elif infor == "8":
                mainapp.Banner()
                findsharedns.__start__()

                #####################

            elif infor == "9":
                mainapp.Banner()
                whois.__start__()

                #####################

            elif infor == "10":
                mainapp.Banner()
                dnslookup.__start__()
                #####################

            elif infor == "11":
                mainapp.Banner()
                robots.__start__()
                #####################

            elif infor == "12":
                mainapp.Banner()
                finder.__start__()

                #####################

            elif infor == "13":
                input(Fore.RED+" [!]"+Fore.GREEN+" Press Enter for Back To Menu ... ")

                #####################
            elif infor == "14":
                time.sleep(1)
                print("Thnaks for choosing H.A.M ...")
                time.sleep(1)
                print("good luck")
                sys.exit()

                #####################
            elif infor == "":
                input(Fore.RED+" [!]"+Fore.YELLOW+" Wrong input , empty field \n press enter to continue ...")
        except KeyboardInterrupt:
            print("")
            print("sorry, there is a problem...")
            time.sleep(1)
            sys.exit()

#------------------------------------------------------------------------------------------------
    elif number == "2":
        mainapp.infolist4()
        try:
            numcms = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"CMS Detection"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ").lower()

        except:
            print("")
            print("sorry, there is a problem...")
            time.sleep(1)
            sys.exit()
        if numcms == "1":
            mainapp.infowp()
            try:
                wp = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"CMN"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"WordPress"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ").lower()
            except:
                print("")
                print("sorry, there is a problem...")
                time.sleep(1)
                sys.exit()
            if wp == "1":
                mainapp.Banner()
                wordpress.wpplug()

            elif wp == "2":
                mainapp.Banner()
                wordpress.user()

            elif wp == "3":
                try:
                    input(Fore.GREEN+" [*] Press Enter for Back To Menu ... ")
                except:
                    print("\n")
                    print("sorry, there is a problem...")
                    time.sleep(1)
                    sys.exit()

        elif numcms == "2":
            mainapp.Banner()
            print(Fore.RED+" [!]"+Fore.BLUE+" Coming Soon ! ")
            try:
                input(Fore.GREEN+" [*] Press Enter for Back To Menu ... ")
            except:
                print("")
                print("sorry, there is a problem...")
                time.sleep(1)
                sys.exit()

        elif numcms == "3":
            mainapp.Banner()
            print(Fore.RED+" [!]"+Fore.BLUE+" Coming Soon ! ")
            try:
                input(Fore.GREEN+" [*] Press Enter for Back To Menu ... ")
            except:
                print("")
                print("sorry, there is a problem...")
                time.sleep(1)
                sys.exit()

        elif numcms == "4":
            try:
                input(Fore.GREEN+" [*] Press Enter for Back To Menu ... ")
            except:
                print("")
                print("sorry, there is a problem...")
                time.sleep(1)
                sys.exit()

        elif numcms == "" or False:
            try:
                input(Fore.GREEN+" [*] Press Enter for Back To Menu ... ")
            except:
                print("")
                print("sorry, there is a problem...")
                time.sleep(1)
                sys.exit()
