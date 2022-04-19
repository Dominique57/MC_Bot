import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERV_ID = os.getenv('DISCORD_SERV_ID')
MCRCON_PSWD = os.getenv('MCRCON_PSWD')
SERVER_TYPE = os.getenv('SERVER_TYPE')

if TOKEN is None:
    exit("Missing token in environment variables !")
if SERV_ID is None:
    exit("Missing serv_id in environment variables !")
if MCRCON_PSWD is None:
    exit("Missing mcrcon_pswd in environment variables !")
if SERVER_TYPE is None:
    exit("Missing server_type in environment variables !")
if SERVER_TYPE not in ['RPI', 'TOWER']:
    exit("Server_type invalid value, must be in [RPI, TOWER]}")


SERV_ID = int(SERV_ID)
