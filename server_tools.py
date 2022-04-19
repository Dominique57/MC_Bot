import socket
import subprocess


def try_wake_server():
    args = ["sudo", "/usr/sbin/etherwake", "-i", "eth0", "10:bf:48:80:61:5a"]
    subprocess.call(args)

def check_server_up() -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1)
    result = sock.connect_ex(('192.168.1.98', 22))
    return result == 0
