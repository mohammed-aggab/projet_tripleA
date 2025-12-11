import os
from pathlib import Path
import sys


def file_analys(folder_path):
    print("=== Analyse de fichiers ===")
    print("Dossier analysé :", folder_path)

    path = Path(folder_path)

    if not path.exists():
        print("⚠ Le dossier n'existe pas.")
        return

    if not path.is_dir():
        print("⚠ Le chemin indiqué n'est pas un dossier.")
        return

    exts = [".txt", ".py", ".pdf", ".jpg"]
    counts = {".txt": 0, ".py": 0, ".pdf": 0, ".jpg": 0}
    total_files = 0

    for root, _, files in os.walk(path):
        for name in files:
            total_files += 1
            ext = Path(name).suffix.lower()
            if ext in counts:
                counts[ext] += 1

    print("Nombre total de fichiers scannés :", total_files)
    print("Extensions suivies : .txt, .py, .pdf, .jpg\n")

    total_tracked = counts[".txt"] + counts[".py"] + counts[".pdf"] + counts[".jpg"]

    if total_tracked == 0:
        print("Aucun fichier avec ces extensions n'a été trouvé.")
        return

    print("{:<10} {:>8} {:>12}".format("Extension", "Nombre", "Pourcentage"))
    print("-" * 32)
    for ext in exts:
        count = counts[ext]
        percent = (count / total_tracked) * 100
        print("{:<10} {:>8} {:>11.2f}%".format(ext, count, percent))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = str(Path.home())

    file_analys(folder)