from tkinter import *
from tkinter import messagebox
import pyttsx3
import pyperclip

# Initialize the speech engine
engine = pyttsx3.init()

def ottomancio(text):
    # The translation logic is proprietary and is omitted for personal reasons.
    # This placeholder just returns the input text.
    # You can use the .exe file to test the actual program
    return text

def translate():
    original_text = original_textbox.get("1.0", END).strip()
    if not original_text:
        messagebox.showwarning("Advertencia", "Debe ingresar texto para traducir.")
        return

    translated_text = ottomancio(original_text)

    translated_textbox.delete("1.0", END)
    translated_textbox.insert(END, translated_text, "ottomnsio")

    translated_textbox.tag_configure("ottomnsio", font=("Ottomnsio", 14))

    translated_sound_text = f"Reproducir audio ({translated_text.strip()})"
    sound_button.config(text=translated_sound_text)

    engine.say(translated_text)
    engine.runAndWait()

    pyperclip.copy(translated_text)
    messagebox.showinfo("Información", "Texto traducido copiado al portapapeles.")

def play_audio():
    original_text = original_textbox.get("1.0", END).strip()
    if not original_text:
        messagebox.showwarning("Advertencia", "Debe ingresar texto para reproducir el audio.")
        return

    translated_text = ottomancio(original_text)

    engine.say(translated_text)
    engine.runAndWait()

def copy_to_clipboard():
    translated_text = translated_textbox.get("1.0", END).strip()
    pyperclip.copy(translated_text)
    messagebox.showinfo("Información", "Texto traducido copiado al portapapeles.")

# Initialize Tkinter window
window = Tk()
window.title("Traductor Ottomancio")
window.geometry("600x400")

# Original text area
original_textbox = Text(window, height=5, width=50)
original_textbox.grid(row=0, column=0, padx=10, pady=10)

# Translated text area
translated_textbox = Text(window, height=5, width=50)
translated_textbox.grid(row=1, column=0, padx=10, pady=10)

# Translate button
translate_button = Button(window, text="Traducir", command=translate)
translate_button.grid(row=2, column=0)

# Sound button
sound_button = Button(window, text="Reproducir audio", command=play_audio)
sound_button.grid(row=3, column=0)

# Copy button
copy_button_frame = Frame(window)
copy_button_frame.grid(row=2, column=1, sticky="e")
copy_button = Button(copy_button_frame, text="Copiar al portapapeles", command=copy_to_clipboard)
copy_button.pack(side=LEFT)

# Start the GUI
window.mainloop()