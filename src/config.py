import json

#Global variables
config_file = "config.json"

def find():
    try:
        with open(config_file, "r") as file:
            print("[+] config file found")
            return True
    except Exception as e:
        print(f"[!] {e}.")
        return False

def read():
    try:
        with open(config_file, "r") as file:
            data = json.load(file)
            return data

    except Exception as e:
        print(f"[!] ERROR: {e}.")
        return False