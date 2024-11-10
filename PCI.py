#!/usr/bin/env python
import os
import tkinter as tk
from tkinter import filedialog
from PIL import Image

def start_software():
    # Controlla se la libreria PIL è installata
    try:
        import PIL
        menu()
    except ImportError:
        print("PIL is not installed. Installing it...")
        import pip
        pip.main(['install', 'Pillow'])
        print("PIL has been installed.")
    

def menu():
    print("Benvenuti al programma di conversione di immagini rapido scritto con Python"+"\n")
    input_menu=input("Scrivi la prima lettera della azioni che vuoi fare (e.g: ca -> convert all): ")

    match input_menu:
        case "c":
            select_image()
        case "ca":
            select_folder()
        case "h":
            print(input("Help"))


def select_folder():
    root=tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory(title="Select folder to convert")
    if folder_path:
        output_format = input("Enter desired output format (e.g. jpg, png): ")
        convert_images(folder_path, output_format)
    
def select_image():
    root=tk.TK()
    root.withdraw()
    print("Prova")

def convert_images(folder_path, output_format):
    keepImage=input("Want to keep the original images?")
    # Convert images
    for filename in os.listdir(folder_path):
        image_path = os.path.join(folder_path, filename)

        if os.path.isfile(image_path):
            try:
                image = Image.open(image_path)

                # Create a new file name with the extension specified by the user
                output_filename = os.path.splitext(filename)[0] + '.' + output_format

                # Save the image in the new format
                output_path = os.path.join(folder_path, output_filename)

                if not os.path.exists(output_path):
                    image.save(output_path, format=output_format)

                print(f"Converted: {image_path} -> {output_path}")

                if keepImage=="no":
                    # Delete the original image
                    if output_format != os.path.splitext(filename)[1]:
                        os.remove(image_path)
                        print(f"Deleted: {image_path}")
            except Exception as e:
                print(f"Error converting '{image_path}': {str(e)}")
    returnToMenu=input("Want return to the menu? ")
    if returnToMenu=="yes" or returnToMenu=="y":
        menu()



if __name__ == "__main__":
    start_software()
