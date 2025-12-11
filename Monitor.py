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

# ------------------------------
# Monitor : affiche dans le terminal
# ------------------------------
def monitor():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = str(Path.home())

    CPU.cpu_info()
    File.file_analys(folder)
    RAM.ram_info()
    SYS.sys_info()
    Processus.process_info()
    NETWORK.network_info()


# ------------------------------
# Capturer le print() des modules
# ------------------------------
def capture(func, *args):
    # Crée une boite pour capturer print()
    boite = io.StringIO()
    with contextlib.redirect_stdout(boite):
        func(*args)   # Lance la fonction du module
    texte = boite.getvalue()
    texte = texte.replace("\n", "<br>")  # Remplace les sauts de ligne pour HTML
    return texte


# ------------------------------
# Générer le dashboard HTML
# ------------------------------
def generate_dashboard():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = str(Path.home())

    # On capture ce que chaque module affiche
    system_text = capture(SYS.sys_info)
    cpu_text = capture(CPU.cpu_info)
    ram_text = capture(RAM.ram_info)
    process_text = capture(Processus.process_info)
    files_text = capture(File.file_analys, folder)
    network_text = capture(NETWORK.network_info)

    # Horodatage actuel
    timestamp = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # Lire le template HTML
    template_path = Path("template.html")
    html = template_path.read_text(encoding="utf-8")

    # Remplacements dans le template
    html = html.replace("INSERT_SYSTEM", system_text)
    html = html.replace("INSERT_CPU", cpu_text)
    html = html.replace("INSERT_RAM", ram_text)
    html = html.replace("INSERT_PROCESS", process_text)
    html = html.replace("INSERT_FILES", files_text)
    html = html.replace("INSERT_NETWORK", network_text)
    html = html.replace("INSERT_TIMESTAMP", timestamp)

    # Écriture du fichier final
    output_path = Path("index.html")
    output_path.write_text(html, encoding="utf-8")

    print(" Dashboard HTML généré : index.html")


# ------------------------------
# MAIN
# ------------------------------
if __name__ == "__main__":
    monitor()             # Affiche dans le terminal
    generate_dashboard()  # Crée la page HTML avec horodatage
