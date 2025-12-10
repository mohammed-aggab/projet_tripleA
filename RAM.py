import psutil

def ram_info():
    print("=== Mémoire ===")

    mem = psutil.virtual_memory()

    used_gb = round(mem.used / (1024 ** 3), 2)
    total_gb = round(mem.total / (1024 ** 3), 2)

    print(f"Mémoire Utilisée : {used_gb} Go")
    print(f"Mémoire Total : {total_gb} Go")
    print(f"Utilisation : {mem.percent} %")

if __name__ == "__ main __":
    ram_info()