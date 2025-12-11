import sys
from pathlib import Path

import CPU
import File
import RAM
import SYS
import Processus

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

if __name__=="__main__":
    monitor()