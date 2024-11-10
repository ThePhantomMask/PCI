#!/usr/bin/env python
import subprocess

def PCI_install():
     # Controlla se la libreria PIL è installata
    try:
        import PIL
    except ImportError:
        print("PIL is not installed. Installing it...")
        import pip
        pip.main(['install', 'Pillow'])
        print("PIL has been installed.")
    command="pyinstaller --onefile PCI.py"

    try:
        print("Avvio installazione PCI")
        subprocess.run(command,check=True,shell=True)
        print("Installazione completata")
    except subprocess.CalledProcessError as e:
        print(f"Error {e}")




if __name__ == "__main__":
   PCI_install()
