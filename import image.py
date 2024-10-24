#!/usr/bin/env python
import os
import tkinter as TK
from tkinter import filedialog
from PIL import Image

def menu():
    print("Benvenuti al programma di conversione di immagini rapido"+"\n")
    print("scritta con Python"+"\n")
    input_menu=input("Vuoi convertire? ")

    match input_menu:
        case "si":
            select_folder()



def select_folder():
    root=TK.Tk()
    root.withdraw()
    desired_folder_path=filedialog.askdirectory(title="Seleziona la cartella desiderata per la conversione delle immagini")
    if desired_folder_path:
        output_path=input("Formato: ")
        convert_images(desired_folder_path,output_path)


def convert_images(folder,output_format):
    keep_image=input("Vuoi tenere l'immagine originale? "+"\n")
    print("Inizio alla conversione"+"\n")
    for file in os.listdir(folder):
        image_path=os.path.join(folder,file)

        if os.path.isfile(image_path):
            try:
                image=Image.open(image_path)
                # Crea un file con l'estensione desiderata dall'utente
                output_file_path=os.path.split(file)[0]+"."+output_format
                # L'immagine viene salvata nella cartella
                output_path=os.path.join(folder,output_file_path)

                # Controlla se il file non esiste già
                if not os.path.exists(output_path):
                    image.save(output_path,format=output_format)
                
                # Controlla se l'utente vuole tenere l'immagine con il formato originale
                if keep_image=="no":
                    # Verrà cancellato il file originale
                    if output_format != os.path.splitext(filename)[1]:
                        os.remove(file)
            except Exception as e:
                print(f"Errore di conversione '{image_path}': {str(e)}")
    
    print("Operazione completata"+"\n")
    print(input("Premi un qualsiasi tasto per terminare il programma"))

if __name__=="__main__":
    menu()
                




