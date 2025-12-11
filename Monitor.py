import sys
import io
import contextlib
from pathlib import Path
from datetime import datetime

import CPU
import File
import RAM
import SYS
import Processus
import NETWORK



# 1) Afficher les infos dans le terminal

def monitor():
    # Si l'utilisateur donne un dossier en argument, on le prend
    # Sinon on prend le dossier "Maison" (Home)
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = str(Path.home())

    # Chaque module affiche ses infos avec print()
    CPU.cpu_info()
    File.file_analys(folder)
    RAM.ram_info()
    SYS.sys_info()
    Processus.process_info()
    NETWORK.network_info()



# 2) Capturer ce que print() affiche, pour le mettre en HTML

def capture_print(fonction, *arguments):
    """
    Cette fonction lance une autre fonction (ex: CPU.cpu_info)
    et récupère tout ce qu'elle affiche avec print().
    """
    boite = io.StringIO()  # une "boite" où on va stocker le texte

    # Tout ce qui est print() pendant l'exécution ira dans "boite"
    with contextlib.redirect_stdout(boite):
        fonction(*arguments)

    texte = boite.getvalue()            # on récupère le texte
    texte = texte.replace("\n", "<br>") # pour que ça saute des lignes en HTML
    return texte



# 3) Générer la page HTML (index.html) à partir du template

def generate_dashboard():
    # Même logique pour le dossier
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = str(Path.home())

    # On "capture" ce que chaque module affiche
    system_text  = capture_print(SYS.sys_info)
    cpu_text     = capture_print(CPU.cpu_info)
    ram_text     = capture_print(RAM.ram_info)
    process_text = capture_print(Processus.process_info)
    files_text   = capture_print(File.file_analys, folder)
    network_text = capture_print(NETWORK.network_info)

    # Date et heure actuelle (horodatage)
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # On récupère le dossier où se trouve ce fichier .py
    base_dir = Path(__file__).resolve().parent

    # On pointe vers template.html et index.html dans le même dossier
    template_path = base_dir / "template.html"
    output_path = base_dir / "index.html"

    # Lire le template
    html = template_path.read_text(encoding="utf-8")

    # Remplacer les zones "INSERT_..." par les vrais textes
    html = html.replace("INSERT_SYSTEM", system_text)
    html = html.replace("INSERT_CPU", cpu_text)
    html = html.replace("INSERT_RAM", ram_text)
    html = html.replace("INSERT_PROCESS", process_text)
    html = html.replace("INSERT_FILES", files_text)
    html = html.replace("INSERT_NETWORK", network_text)
    html = html.replace("INSERT_TIMESTAMP", timestamp)

    # Écrire le résultat final dans index.html
    output_path.write_text(html, encoding="utf-8")

    print("Dashboard HTML généré :", output_path)



# 4) Programme principal

if __name__ == "__main__":
    monitor()            # affiche dans le terminal
    generate_dashboard() # crée index.html
