import time
from src import config,webhook


def main():
    print("[+] starting up..")
    config.find()

    cfg = config.read()
    if not cfg:
        print("[!] config file error.")
        exit()
    
    while True:
        path_to_log = cfg["path_to_log"]
        hook = cfg["webhook"]
        loop_interval = cfg["interval"]

        webhook.read(hook,path_to_log,cfg)
        time.sleep(loop_interval)


if __name__ == "__main__":
    main()