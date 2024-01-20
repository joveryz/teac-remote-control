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
cd_com_port = 32
cd_com_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cd_com_socket.connect((com_server_host, cd_com_port))

dac_com_port = 32
dac_com_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
dac_com_socket.connect((com_server_host, dac_com_port))

commandList = {
    "cd": {
        "power": "@POWER ON\r",
        "open": "@KEY 00\r",
        "play": "@KEY 01\r",
        "stop": "@KEY 03\r",
        "backward": "@KEY 0B\r",
        "next": "@KEY 0C\r",
        "mute": "@KEY 0D\r",
        "pause": "@KEY 02\r",
        "info": "@KEY 3C\r",
        "display": "@KEY 42\r",
    },
    "dac": {
        "power": "@POWER ON\r",
        "net": "@KEY 32\r",
        "line": "@KEY 38\r",
        "coaxial1": "@KEY 36\r",
        "coaxial2": "@KEY 37\r",
        "info": "@KEY 3C\r",
        "display": "@KEY 42\r",
        "hp63": "@AOUT TRS\r",
        "hpxlr4": "@AOUT XLR4 A\r",
        "xlr": "@AOUT XLR 2\r",
        "volumeup": "@KEY 13\r",
        "volumedown": "@KEY 12\r",
        "mute": "@KEY 1C\r",
    },
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
            return True
        except:
            if device == "cd":
                cd_com_socket.connect((com_server_host, cd_com_port))
            elif device == "dac":
                dac_com_socket.connect((com_server_host, dac_com_port))
            retry_count -= 1
    return False


@app.get("/keepalive")
def root():
    return "I'm alive"


@app.get("/{device}/{command}")
def send_command(device: str, command: str):
    res = send_with_retry(device, commandList[device][command])
    return {"result": "success" if res else "fail"}
