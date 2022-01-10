import requests
from src import output

# Global variables
duplicate = ""

def sendhook(msg,url):
    Message = {
    "content": msg }
    print("[->] Sending; ",msg)
    requests.post(url, data=Message)


def read(url,logfile,cfg):
    global duplicate 
    cache = list()
    with open(logfile,"r") as file:
        send = False
        for i in file.readlines():
            line = i.replace("\n","")
            cache.append(line)
            
            output.create_json(line, cfg["path_to_output"])

        last = cache[-1]
        if "[Server thread/WARN]" in last or "[Server thread/INFO]: [Server]" in last:
            if not duplicate == last:
                send = True
                duplicate = last

        if send:
            sendhook(last,url)
            print(f"[+] log: {last}")