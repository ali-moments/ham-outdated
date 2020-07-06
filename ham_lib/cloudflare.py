import socket
import sys
import time
from colorama import Fore
def __start__():
    print(Fore.LIGHTRED_EX+" [!] Cloudflare Bypasser . . . \n")
    print(Fore.LIGHTRED_EX+" [!] Enter The Target Website Address \n")
    print(Fore.LIGHTRED_EX+" [!] Enter Exit To Go To Main Menu \n")
    subdom = ['ftp', 'cpanel', 'webmail', 'localhost', 'local', 'mysql', 'forum', \
    'driect-connect', 'blog', 'vb', 'forums', 'home', 'direct', 'forums', 'mail', \
    'access', 'admin', 'administrator', 'email', 'downloads', 'ssh', 'owa', 'bbs', \
    'webmin', 'paralel', 'parallels', 'www0', 'www', 'www1', 'www2', 'www3', 'www4', \
    'www5', 'shop', 'api', 'blogs', 'test', 'mx1', 'cdn', 'mysql', 'mail1', 'secure', \
    'server', 'ns1', 'ns2', 'smtp', 'vpn', 'm', 'mail2', 'postal', 'support', 'web', 'dev']

    site = input(Fore.RED+" ┌─["+Fore.LIGHTGREEN_EX+"HAMMASTER"+Fore.BLUE+"~"+Fore.WHITE+"@HOME"+Fore.RED+"/"+Fore.CYAN+"IG"+Fore.RED+"/"+Fore.LIGHTYELLOW_EX+"Bypass-CloudFlare"+Fore.RED+"""]
 └──╼ """+Fore.WHITE+"卐 ")
    if site == "":
        try:
            print(Fore.RED+" [!] "+Fore.YELLOW+" Error : Empty Field ... \n")
            time.sleep(2)
            sys.exit()
        except:
            return
    elif site == "exit" or site == "Exit" or site == "EXIT":
        try:
            return
        except:
            return
    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            print (" [#] CloudFlare Bypass " + str(bypass) + ' | ' + str(hosts))
        except Exception:
            pass
    try:
        input(Fore.GREEN+" [*] Press Enter for Back To Menu ... ")
    except:
        print("\n there is a problem")
        time.sleep(1)
        sys.exit()
