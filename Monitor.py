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
    print("Timestamp généré :", timestamp)

    # Chemins ABSOLUS pour être sûr qu'on touche les bons fichiers
    base_dir = Path(__file__).resolve().parent
    template_path = base_dir / "template.html"
    output_path = base_dir / "index.html"

    print("Template utilisé :", template_path)
    print("Index généré   :", output_path)

    # Lire le template HTML
    html = template_path.read_text(encoding="utf-8")

    # Vérifier que le placeholder existe bien
    if "INSERT_TIMESTAMP" not in html:
        print("⚠️ ATTENTION : 'INSERT_TIMESTAMP' n'est PAS dans template.html")
    else:
        print("✅ 'INSERT_TIMESTAMP' trouvé dans template.html")

    # Remplacements dans le template
    html = html.replace("INSERT_SYSTEM", system_text)
    html = html.replace("INSERT_CPU", cpu_text)
    html = html.replace("INSERT_RAM", ram_text)
    html = html.replace("INSERT_PROCESS", process_text)
    html = html.replace("INSERT_FILES", files_text)
    html = html.replace("INSERT_NETWORK", network_text)
    html = html.replace("INSERT_TIMESTAMP", timestamp)

    # Écriture du fichier final
    output_path.write_text(html, encoding="utf-8")

    print("✅Dashboard HTML généré :", output_path)


# ------------------------------
# MAIN
# ------------------------------
if __name__ == "__main__":
    monitor()             # Affiche dans le terminal
    generate_dashboard()  # Crée la page HTML avec horodatage
