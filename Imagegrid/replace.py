import re
import tkinter as tk
from tkinter import simpledialog

root = tk.Tk()
root.withdraw()

folder = simpledialog.askstring("Texteingabe", "Bitte geben Sie einen Ordner ein:")

def read_text_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.readlines()

def replace_text(input_text, replacement_text):
    # Finde alle Vorkommen von "Bild [Zahl]"
    matches = re.findall(r'Bild (\d+)', input_text)
    replaced_text = input_text
    for match in matches:
        try:
            # Lese die Zeile mit der entsprechenden Zahl aus dem Ersatztext
            replacement_line = "../assets/images/" + folder + "/" + replacement_text[int(match) - 1].strip()
            # Ersetze das Vorkommen von "Bild [Zahl]" durch den Ersatztext
            replaced_text = re.sub(f'Bild {match}(?!\d)', replacement_line, replaced_text, count=1)
        except IndexError:
            print(f"Warnung: Ersatz für 'Bild {match}' nicht gefunden.")
    return replaced_text

def main():
    # Pfade zu den Eingabe- und Ersatztextdateien
    input_file_path = 'code.txt'
    replacement_file_path = 'filenames.txt'

    # Lese den Eingabetext und den Ersatztext
    input_text = ''.join(read_text_file(input_file_path))
    replacement_text = read_text_file(replacement_file_path)

    # Ersetze die Zeichenfolgen und erhalte das Ergebnis
    replaced_text = replace_text(input_text, replacement_text)

    # Schreibe das Ergebnis in eine Ausgabedatei
    with open('code-new.txt', 'w', encoding='utf-8') as file:
        file.write(replaced_text)

if __name__ == "__main__":
    main()
