import json

# Global variables

# .json structure
online_status = dict()
server_status = {"Status":0,"player_status":online_status}

def create_json(line,path):
    global server_status
    global online_status

        # Server Status
    if 'For help, type "help"' in line:
        server_status["Status"] = "ONLINE"
        
    if 'INFO]: Stopping' in line:
        server_status["Status"] = "OFFLINE"
        
        # Player Joined
    if "the game" in line:
        player = line.split(" ")[3]
        action = line.split(" ")[4]

        if action == "joined":
            online_status[player] = "ONLINE"

        if action == "left":
            online_status[player] = "OFFLINE"

    
    with open(f"{path}server_status.json","w+") as file:
        json.dump(server_status, file)