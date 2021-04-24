import socket


def check():
    try:
        socket.gethostbyname('usebottles.com')
        return True
    except socket.error:
        return False
