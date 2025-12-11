import psutil
import time


def process_info():

    time.sleep(1)

    processes = []

    for p in psutil.process_iter(['pid', 'name']):
        try:
            cpu = p.cpu_percent(interval=0.1)
            mem = p.memory_percent()
            name = p.info['name'] or "Inconnu"
            processes.append({
                "pid": p.pid,
                "name": name,
                "cpu": cpu,
                "mem": mem
            })
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

    print("Liste des processus :")
    print("{:>6}  {:<25} {:>7} {:>7}".format("PID", "Nom", "CPU%", "RAM%"))
    print("-" * 50)
    for proc in processes:
        name = proc["name"]
        if len(name) > 25:
            name = name[:23] + ".."
        print("{:>6}  {:<25} {:>7.2f} {:>7.2f}".format(
            proc["pid"], name, proc["cpu"], proc["mem"]
        ))

    print("\nTop 3 des processus les plus gourmands (CPU) :")
    processes_sorted = sorted(processes, key=lambda p: p["cpu"], reverse=True)
    top3 = processes_sorted[:3]

    if not top3:
        print("Aucun processus trouvé.")
    else:
        print("{:>6}  {:<25} {:>7} {:>7}".format("PID", "Nom", "CPU%", "RAM%"))
        print("-" * 50)
        for proc in top3:
            name = proc["name"]
            if len(name) > 25:
                name = name[:23] + ".."
            print("{:>6}  {:<25} {:>7.2f} {:>7.2f}".format(
                proc["pid"], name, proc["cpu"], proc["mem"]
            ))

if __name__=="__main__":
    process_info()