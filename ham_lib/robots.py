import requests
import sys
import time
from colorama import Fore

search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

def __start__():
    try:
        print(Fore.YELLOW+"\n [!] Robots . . . ")
        print(Fore.RED+" [!] Plase Enter WebSite Address \n")
        print(Fore.YELLOW+" [!] Enter Exit To Go To Main Menu")
        url = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Robots_Scanner"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
        if url == "exit" or url == "Exit" or url == "EXIT":
            try:
                return
            except:
                return
        if 'http' in url:
            pass
        elif 'http' != url:
            url = ('http://'+url)
        for i in search:
            time.sleep(0.1)
            ur = (url+"/"+i)
            "http://pythons.ir/robots.txt"
            reqs = requests.get(ur)
            if reqs.status_code == 200 or reqs.status_code == 405:
                print(Fore.GREEN+" [+] "+ ur)
            else:
                print(Fore.RED+" [-] "+ur)
        try:
            input(Fore.RED+" [!] "+Fore.GREEN+"Press Enter To Go Back To Menu ")
        except:
            print("\n sorry, there is a problem")
            time.sleep(2)
            sys.exit()
    except:
        print(" ")
