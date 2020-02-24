#!/usr/bin/python3

import subprocess
import random


def figlet():
    fonts = ["3-D.flf", "5lineoblique.flf", "Acrobatic.flf", "Alligator2.flf", "Alligator.flf", "Block.flf", "Catwalk.flf", "Cosmike.flf", "Cyberlarge.flf",
             "Digital.flf", "Doh.flf", "Doom.flf", "Epic.flf", "Isometric1.flf", "Isometric3.flf", "Lean.flf", "Poison.flf", "sblood.flf", "Slant.flf"]
    print()
    subprocess.call(
        ["figlet", "-f", "./figlet-fonts/bests_fonts/{}".format(random.choice(fonts)), "Olympus"])
    print()


def help():
    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| help     - display all cammands  |
| clear    - clear the terminal    |
| info     - information gathering |
| scan     - scanning              |
| wireless - wireless attacks      |
| passwd   - password attacks      |
| exit     - exit program          |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		""")


def clear():
    subprocess.call(["clear"])


def wordlists():
    subprocess.call(["ls", "/usr/share/wordlists/dirb/"])
    print("/usr/share/wordlists/dirb/")


def module():
    print("""
    afp cvs ftp http imap mssql mysql
    nntp pcanywhere pop3 postgres rdp rexec
    rlogin rsh  smbnt smtp-vrfy smtp snmp
    ssh  svn telnet  vmauthd  vnc  web-form
    wrapper
	""")


def info():
    while True:
        data = input("(info)>>> ")
        if data == "help" or data == "?":
            print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| help         - display all cammands                               |
| clear        - clear the terminal                                 |
| back         - back to main                                       |
| theHarvester - E-mails, subdomains and names Harvester            |
| dmitry       - Deepmagic Information Gathering Tool               |
| knockpy      - enumerate subdomains on a target domain            |
| gobuster     - tool used to brute-force directories and files     |
| dnsenum      - enumerate information on a domain                  |
| fierce       - DNS reconnaissance tool for locating IP            |
| dnsrecon     - DNS Enumeration Script                             |
| wafw00f      - Identify Web Application Firewall products         |
| netdiscover  - active/passive ARP reconnaissance tool             |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
				""")
        elif data == "clear":
            clear()
        elif data == "back":
            break
        elif data == "exit":
            quit()
        elif data == "theHarvester":
            try:
                target = input("target>>> ")
                subprocess.call(["theHarvester", "-d", target, "-l", "500",
                                 "-n", "-c", "-f", "{}.html".format(target), "-b", "google"])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "dmitry":
            try:
                target = input("target>>> ")
                subprocess.call(["dmitry", "-winseo", target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "knockpy":
            try:
                target = input("target>>> ")
                wordlists()
                wordlist = input("wordlist>>> ")
                subprocess.call(["knockpy", "-w", wordlist, target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "gobuster":
            try:
                target = input("target (full URL)>>> ")
                wordlists()
                wordlist = input("wordlist>>> ")
                subprocess.call(
                    ["gobuster", "dir", "-w", wordlist, "-u", target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "dnsenum":
            try:
                target = input("target>>> ")
                subprocess.call(["dnsenum", target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "dnsrecon":
            try:
                target = input("target>>> ")
                subprocess.call(["dnsrecon", "-d", target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "fierce":
            try:
                target = input("target>>> ")
                subprocess.call(["fierce", "-dns", target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "wafw00f":
            try:
                target = input("target (full URL)>>> ")
                subprocess.call(["wafw00f", target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "netdiscover":
            try:
                target = input("target>>> ")
                subprocess.call(["netdiscover", "-r", target])
            except KeyboardInterrupt:
                print()
                continue
        else:
            print("""
~~~~~~~~~~~~~
| try help  |
~~~~~~~~~~~~~
        		""")


def scan():
    while True:
        data = input("(scan)>>> ")
        if data == "help" or data == "?":
            print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| help     - display all cammands                       |
| clear    - clear the terminal                         |
| back     - back to main                               |
| nmap     - Network exploration tool and port scanner  |
| skipfish - web application security scanner           |
| wpscan   - WordPress Security Scanner                 |
| nikto    - Scan web server for known vulnerabilities  |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
				""")
        elif data == "clear":
            clear()
        elif data == "back":
            break
        elif data == "exit":
            quit()
        elif data == "nmap":
            try:
                target = input("target>>> ")
                subprocess.call(["nmap", "-A", "-T4", "-Pn", target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "skipfish":
            try:
                target = input("target (full URL)>>> ")
                output = input("ouput_dir>>> ")
                subprocess.call(["skipfish", "-o", output, target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "wpscan":
            try:
                target = input("target (full URL)>>> ")
                subprocess.call(["wpscan", "--url", target])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "nikto":
            try:
                target = input("target (full URL)>>> ")
                subprocess.call(["nikto", "-h", target])
            except KeyboardInterrupt:
                print()
                continue
        else:
            print("""
~~~~~~~~~~~~~
| try help  |
~~~~~~~~~~~~~
        		""")


def wireless():
    while True:
        data = input("(wireless)>>> ")
        if data == "help" or data == "?":
            print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| help        - display all cammands                   |
| clear       - clear the terminal                     |
| back        - back to main                           |
| aircrack-ng - 802.11 WEP / WPA-PSK key cracker       |
| airodump-ng - wireless packet capture tool           |
| aireplay-ng - inject packets into a wireless network |
| reaver      - WPS Cracker                            |
| bully       - WPS brute force attacker               |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
				""")
        elif data == "clear":
            clear()
        elif data == "back":
            break
        elif data == "aircrack-ng":
            try:
                cap = input("cap_file>>> ")
                subprocess.call(
                    ["aircrack-ng", "-w", "/usr/share/wordlists/rockyou.txt", cap])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "airodump-ng":
            try:
                interface = input("interface>>> ")
                while True:
                    subprocess.call(["airodump-ng", interface])
                    bssid = input("target_mac>>> ")
                    channel = input("channel>>> ")
                    file = input("file_name>>> ")
                    subprocess.call(["airodump-ng", "--bssid", bssid,
                                     "--channel", channel, "--write", file, interface])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "aireplay-ng":
            while True:
                data = input("(wireless/aireplay-ng)>>> ")
                if data == "help":
                    print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| help      - display all cammands             |
| clear     - clear the terminal               |
| back      - back to main                     |
| deauth    - deauthenticate 1 or all stations |
| fakeauth  - fake authentication with AP      |
| arpreplay - standard ARP-request replay      |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
						""")
                elif data == "clear":
                    clear()
                elif data == "back":
                    break
                elif data == "deauth":
                    try:
                        bssid = input("target_mac>>> ")
                        target = input("target_mac>>> ")
                        interface = input("interface>>> ")
                        subprocess.call(
                            ["aireplay-ng", "--deauth", "0", "-a", bssid, "-c", target, interface])
                    except KeyboardInterrupt:
                        print()
                        continue
                elif data == "fakeauth":
                    try:
                        bssid = input("target_mac>>> ")
                        target = input("your_mac>>> ")
                        interface = input("interface>>> ")
                        subprocess.call(
                            ["aireplay-ng", "--fakeauth", "30", "-a", bssid, "-h", mac, interface])
                    except KeyboardInterrupt:
                        print()
                        continue
                elif data == "arpreplay":
                    try:
                        bssid = input("target_mac>>> ")
                        target = input("your_mac>>> ")
                        interface = input("interface>>> ")
                        subprocess.call(
                            ["aireplay-ng", "--arpreplay", "-b", bssid, "-h", mac, interface])
                    except KeyboardInterrupt:
                        print()
                        continue
        elif data == "reaver":
            try:
                bssid = input("target_mac>>> ")
                channel = input("channel>>> ")
                interface = input("interface>>> ")
                subprocess.call(
                    ["reaver", "--bssid", bssid, "--channel", channel, "--interface", interface])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "bully":
            try:
                bssid = input("target_mac>>> ")
                essid = input("target_essid>>> ")
                channel = input("channel>>> ")
                interface = input("interface>>> ")
                subprocess.call(["bully", "-b", bssid, "-e",
                                 essid, "-c", channel, interface])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "exit":
            quit()
        else:
            print("""
~~~~~~~~~~~~~
| try help  |
~~~~~~~~~~~~~
        		""")


def passwd():
    while True:
        data = input("(passwd)>>> ")
        if data == "help" or data == "?":
            print("""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
| help             - display all cammands                         |
| clear            - clear the terminal                           |
| back             - back to main                                 |
| crunch           - generate wordlists from a character set      |
| hashcat          - Advanced CPU-based password recovery utility |
| hash-identifier  - WordPress Security Scanner                   |
| john             - a tool to find weak passwords of your users  |
| medusa           - Parallel Network Login Auditor               |
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
					""")
        elif data == "clear":
            clear()
        elif data == "back":
            break
        elif data == "exit":
            quit()
        elif data == "crunch":
            try:
                minimum = input("min>>> ")
                maximum = input("max>>> ")
                strings = input("characters>>> ")
                subprocess.call(["crunch", minimum, maximum,
                                 strings, "-o", "wordlist.txt"])
            except KeyboardInterrupt:
                print()
                continue
        elif data == "hashcat":
            try:
                file = input("md5_hashs>>> ")
                subprocess.call(
                    ["hashcat", "-m", "0", "-a", "0", file, "/usr/share/wordlists/rockyou.txt"])

            except KeyboardInterrupt:
                print()
                continue
        elif data == "hash-identifier":
            while True:
                try:
                    subprocess.call(["hash-identifier"])
                except KeyboardInterrupt:
                    break
        elif data == "john":
            try:
                passwd_file = input("passwd>>> ")
                shadow_file = input("shadow>>> ")
                subprocess.call("unshadow {} {} > password.txt".format(
                    passwd_file, shadow_file), shell=True)
                subprocess.call(["john", "password.txt"])

            except KeyboardInterrupt:
                print()
                continue
        elif data == "medusa":
            try:
                host = input("host>>> ")
                username = input("username_file>>> ")
                password = input("password_file>>>")
                module()
                module_name = input("module>>> ")
                subprocess.call(["medusa", "-h", host, "-U",
                                 username, "-P", password, "-M", module_name])
            except KeyboardInterrupt:
                print()
                continue


figlet()

while True:
    try:
        data = input(">>> ")
        if data == "help" or data == "?":
            help()
        elif data == "clear":
            clear()
        elif data == "info":
            info()
        elif data == "scan":
            scan()
        elif data == "wireless":
            wireless()
        elif data == "passwd":
            passwd()
        elif data == "exit" or data == "quit":
            quit()
    except KeyboardInterrupt:
        print("\n\nPeace Out!\n")
        break
