import sys
import os

# Codice per path librerie #
Cdir = os.getcwd()

Platform = sys.platform

if Platform == "win32":
    sys.path.insert(0, f"{Cdir}\\venv\lib\site-packages")
else:
    Version = f"python{sys.version_info[0]}.{sys.version_info[1]}"
    sys.path.insert(0, f"{Cdir}/venv/lib/{Version}/site-packages")
# Fine codice #