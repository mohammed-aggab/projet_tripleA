import psutil
import platform
import socket
from datetime import datetime

def sys_info():


    hostname = socket.gethostname()
    print(f"Nom de la Machine : {hostname}")

    os_name = platform.platform()
    print(f"Système d'exploitation : {os_name}")

    boot_time = psutil.boot_time()
    boot_datetime = datetime.fromtimestamp(boot_time)
    print(f"Heure de Démarrage : {boot_datetime.strftime('%Y - %m - %d %H : %M : %S')}")


    now = datetime.now()
    seconds = int((now - boot_datetime).total_seconds())
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    print(f"Temps écoulé depuis le démarrage : {hours} h et {minutes} min")

    users = psutil.users()
    print(f"Utilisateur Connectés : {len(users)}")

   
if __name__=="__main__":
    sys_info()
