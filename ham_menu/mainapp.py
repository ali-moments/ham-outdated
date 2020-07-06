import os
from colorama import Fore
import time
import sys

def Banner():
    os.system("clear")
    print(Fore.LIGHTRED_EX+"""\n
 ██╗  ██╗ █████╗ ███╗   ███╗███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
 ██║  ██║██╔══██╗████╗ ████║████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
 ███████║███████║██╔████╔██║██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
 ██╔══██║██╔══██║██║╚██╔╝██║██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
 ██║  ██║██║  ██║██║ ╚═╝ ██║██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
 ╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝

 ==============================================================================
 **                      Weblog : realham.blogsky.com                        **
 **                         Channel : @realham_tel                           **
 **                        Developers : H.A.M Team                           **
 **                    Team Members : Hamid.Ali.Mohammad                     **
 **                          Thank's : .::Amir::.                            **
 ==============================================================================
          """)

def infolist1():
    time.sleep(0.1)
    print(Fore.RED+" ["+Fore.WHITE+"卐"+Fore.RED+"]"+Fore.CYAN+" Choose an options \n")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+" [1] Information Gathering\n")
    time.sleep(0.1)
    print(Fore.RED+" [2] CMS Detection\n")
    time.sleep(0.1)
    print(Fore.YELLOW+" [3] Developer!\n")
    time.sleep(0.1)
    print(Fore.RED+" [4] Exit out\n")

def infolist2():
    time.sleep(0.1)
    print(Fore.GREEN+"  [1]"+Fore.CYAN+" - Bypass Cloud Flare")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.2)
    print(Fore.GREEN+"  [2]"+Fore.CYAN+" - Cms Detect")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [3]"+Fore.CYAN+" - Trace Toute")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [4]"+Fore.CYAN+" - Reverse IP")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [5]"+Fore.CYAN+" - Port Scan")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [6]"+Fore.CYAN+" - IP location Finder")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [7]"+Fore.CYAN+" - Show HTTP Header")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [8]"+Fore.CYAN+" - Find Shared DNS")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [9]"+Fore.CYAN+" - Whois")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [10]"+Fore.CYAN+" - DNS Lookup")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [11]"+Fore.CYAN+"- Robots Scanner")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [12]"+Fore.CYAN+" - Admin Page Finder")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [13]"+Fore.CYAN+" - Back To Menu")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [14]"+Fore.CYAN+" - Exit :) \n")

def infolist3():
      Banner()
      time.sleep(0.1)
      print (Fore.GREEN+" [*]"+Fore.CYAN+"  Develper : Ali-AAA >\n")
      time.sleep(0.1)
      print (Fore.GREEN+" [*]"+Fore.GREEN+"  Thank's : .::sedHAMIDreza::. >\n")
      time.sleep(0.1)
      print (Fore.GREEN+" [*]"+Fore.GREEN+"  Thank's : .::Mohammad_mahdi::. >\n")
      time.sleep(0.1)
      print (Fore.GREEN+" [*]"+Fore.MAGENTA+"  My Site : reslham.blogsky.com >\n")
      time.sleep(0.1)
      print (Fore.GREEN+" [*]"+Fore.BLUE+" Telegram CH : @realham_tel >\n")
      time.sleep(0.1)
      try:
            input(Fore.LIGHTRED_EX+" [*]  Press Enter for Back To Menu >>>")
      except:
            print("\n")
            print("sorry, there is a problem!")
            time.sleep(1)
            sys.exit()

def infolist4():
    Banner()
    print(Fore.GREEN+"  [1]"+Fore.CYAN+"- WordPress ")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [2]"+Fore.CYAN+" - Drupal"+Fore.RED+" Coming Soon . . .")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [3]"+Fore.CYAN+" - Joomla "+Fore.RED+" Coming Soon . . . ")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [4]"+Fore.CYAN+" - Back To Menu")
    print(Fore.BLUE+"  **********************\n")
    time.sleep(0.1)

def infowp():
    Banner()
    print(Fore.GREEN+"  [1]"+Fore.CYAN+" - Get Plugins ")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [2]"+Fore.CYAN+" - Get Username ")
    print(Fore.BLUE+"  **********************")
    time.sleep(0.1)
    print(Fore.GREEN+"  [3]"+Fore.CYAN+" - Back To Menu ")
    print(Fore.BLUE+"  **********************\n")
    time.sleep(0.1)
