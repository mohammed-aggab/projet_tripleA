import socket

def network_info():


    hostname = socket.gethostname()

    try:
        ip = socket.gethostbyname(hostname)
    except:
        ip = "Inconnue"

    print(f"Adresse IP : {ip}")
