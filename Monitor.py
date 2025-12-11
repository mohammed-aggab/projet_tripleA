import sys
import io
import contextlib
from pathlib import Path



import CPU
import File
import RAM
import SYS
import Processus
import NETWORK




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




#   CAPTURER LES PRINT()

def capture(func, *args):
    # On crée une boite vide pour stocker ce que print() affiche
    boite = io.StringIO()

    # Tout ce que print() écrit va aller dans la boite
    with contextlib.redirect_stdout(boite):
        func(*args)   # On lance ta fonction (CPU, RAM, etc.)

    # On récupère le texte de la boite
    texte = boite.getvalue()

    # On remplace les retours à la ligne par <br> pour le HTML
    texte = texte.replace("\n", "<br>")
    
    return texte




#   GÉNÉRER DASHBOARD HTML

def generate_dashboard():
    # même logique que ton monitor()
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

    # Lire le template HTML
    template_path = Path("template.html")
    html = template_path.read_text(encoding="utf-8")

    # Remplacements
    html = html.replace("INSERT_SYSTEM", system_text)
    html = html.replace("INSERT_CPU", cpu_text)
    html = html.replace("INSERT_RAM", ram_text)
    html = html.replace("INSERT_PROCESS", process_text)
    html = html.replace("INSERT_FILES", files_text)
    html = html.replace("INSERT_NETWORK", network_text)

    # Écriture du fichier final
    output_path = Path("index.html")
    output_path.write_text(html, encoding="utf-8")

    print("✅Dashboard HTML généré : index.html")


#            MAIN

if __name__ == "__main__":
    monitor()             # Affiche dans le terminal 
    generate_dashboard()  # Crée la page HTML
