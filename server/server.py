import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import socket

app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

com_server_host = "172.16.68.188"
cd_com_port = 23
cd_com_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cd_com_socket.connect((com_server_host, cd_com_port))

dac_com_port = 26
dac_com_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dac_com_socket.connect((com_server_host, dac_com_port))

commandList = {
    "cd": {
        "power": "@POWER ON\r",
        "open": "@KEY 00\r",
        "display": "@KEY 42\r",
        "info": "@KEY 3C\r",
        "play": "@KEY 01\r",
        "pause": "@KEY 02\r",
        "stop": "@KEY 03\r",
        "backward": "@KEY 0B\r",
        "forward": "@KEY 0C\r",
    },
    "dac": {
        "power": "@POWER ON\r",
        "display": "@KEY 42\r",
        "info": "@KEY 3C\r",
        "net": "@KEY 32\r",
        "line": "@KEY 38\r",
        "coaxial1": "@KEY 36\r",
        "coaxial2": "@KEY 37\r",
        "hp63": "@AOUT TRS\r",
        "hpxlr4": "@AOUT XLR4 A\r",
        "xlr": "@AOUT XLR 2\r",
        "volumeup": "@KEY 13\r",
        "volumedown": "@KEY 12\r",
        "mute": "@KEY 1C\r",
    },
    "roon": {
        "backward": "roon -c previous -z AVERY-UD701",
        "forward": "roon -c next -z AVERY-UD701",
        "play": "roon -c play -z AVERY-UD701",
        "pause": "roon -c pause -z AVERY-UD701",
        "stop": "roon -c stop -z AVERY-UD701",
        "getinfo": "roon -N -z AVERY-UD701",
    }
}


def send_with_retry(device: str, command: str):
    retry_count = 5
    while retry_count > 0:
        try:
            if device == "cd":
                cd_com_socket.sendall(command.encode())
                print(':'.join(hex(ord(x))[2:] for x in command))
            elif device == "dac":
                dac_com_socket.sendall(command.encode())
            elif device == "roon":
                os.system(command)
            return True
        except:
            if device == "cd":
                cd_com_socket.connect((com_server_host, cd_com_port))
            elif device == "dac":
                dac_com_socket.connect((com_server_host, dac_com_port))
            elif device == "root":
                return False
            retry_count -= 1
    return False


@app.get("/keepalive")
def root():
    return "I'm alive"


@app.get("/{device}/{command}")
def send_command(device: str, command: str):
    res = send_with_retry(device, commandList[device][command])
    return {"result": "success" if res else "fail"}
