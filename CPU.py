import psutil

def cpu_info():
    print("=== CPU ===")

    physical = psutil.cpu_count(logical = False)
    logical = psutil.cpu_count(logical = True)
    print(f"Coeurs Physiques : {physical}")
    print(f"Coeurs Logiques : {logical}")

    freq = psutil.cpu_freq()
    if freq is not None:
        print(f"Fréquence Actuelle : {round(freq.current / 1000 , 2)} GHz")
    else:
        print("Fréquence Actuelle : Inconnue")

    cpu_percent = psutil.cpu_percent(1)
    print(f"Utiisation CPU : {cpu_percent}")


if __name__=="__ main __":
    cpu_info()