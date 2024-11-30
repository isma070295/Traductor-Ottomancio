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

# Function to display alerts/messages to the user
def display_alert(message):
    alert_label.config(text=message)  # Set the message in the alert label
    alert_label.after(2000, lambda: alert_label.config(text=""))  # Clear the message after 2 seconds

def display_pronunciation(message):
    pronunciation_label.config(text=message)  # Set the message in the pronunciation label

# Function to handle the translation process
def translate():
    original_text = original_textbox.get("1.0", END).strip()
    if not original_text:
        display_alert("Debe ingresar texto para traducir.")
        return

    translated_text = ottomancio(original_text) # Translate the text using the ottomancio function

    # Update the translated text area to show the original text (visually)
    translated_textbox.config(state=NORMAL)
    translated_textbox.delete("1.0", END)
    translated_textbox.insert(END, original_text, "ottomnsio")
    translated_textbox.tag_configure("ottomnsio", font=("Ottomnsio", 14)) # Shows ottomancio text
    translated_textbox.config(state=DISABLED)

    # Update the button text to include the translated text
    display_pronunciation(f"Pronunciación: {translated_text.strip()}")

    # Use pyttsx3 to play the pronunciation of the translated text
    engine.say(translated_text)
    engine.runAndWait()

    # Attempt to copy the translated text to the clipboard
    try:
        pyperclip.copy(translated_text)
        display_alert("Texto traducido copiado al portapapeles.")  # Notify the user if copy is successful
    except pyperclip.PyperclipException:  # Handle errors related to clipboard copying
        display_alert("Error al copiar texto al portapapeles.")

# Function to handle playing the audio pronunciation of the translated text
def play_audio():
    original_text = original_textbox.get("1.0", END).strip()  # Get the original text
    if not original_text:  # If no text is provided, show an alert
        display_alert("Debe ingresar texto para reproducir el audio.")
        return

    translated_text = ottomancio(original_text)  # Translate the text
    engine.say(translated_text)  # Play the pronunciation using pyttsx3
    engine.runAndWait()

# Function to handle copying the translated text to the clipboard
def copy_to_clipboard():
    # Directly access the translated text instead of the text box
    translated_text = ottomancio(original_textbox.get("1.0", END).strip())  # Get the translated text again using the function
    if not translated_text:  # If there's no translated text, show an alert
        display_alert("No hay texto para copiar.")
        return
    try:
        pyperclip.copy(translated_text)  # Attempt to copy to the clipboard
        display_alert("Texto traducido copiado al portapapeles.")  # Notify user of success
    except pyperclip.PyperclipException:  # Handle any errors during the copy process
        display_alert("Error al copiar texto al portapapeles.")  # Notify user of failure


# Initialize Tkinter window
window = Tk()
window.title("Traductor Ottomancio")
window.geometry("600x400")  # Initial window size (can be resized)
window.resizable(True, True)  # Allow window to be resized

# Original text area where user can input text
original_textbox = Text(window, height=5, width=50)
original_textbox.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")  # Use grid layout for flexibility

# Translated text area where translated text will be shown (non-editable)
translated_textbox = Text(window, height=5, width=50)
translated_textbox.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")  # Use grid layout for flexibility
translated_textbox.config(state=DISABLED)  # Make it non-editable by default

# Translate button to trigger the translation function
translate_button = Button(window, text="Traducir", command=translate)
translate_button.grid(row=0, column=1, padx=10, pady=10)  # Place button next to the original text area

# Sound button to trigger the audio pronunciation
sound_button = Button(window, text="Reproducir pronunciación", command=play_audio)
sound_button.grid(row=1, column=1, padx=10, pady=10)  # Place button next to the translated text area

# Frame and button for copying text to the clipboard
copy_button_frame = Frame(window)
copy_button_frame.grid(row=2, column=1, sticky="e")  # Frame to position the button to the right
copy_button = Button(copy_button_frame, text="Copiar al portapapeles", command=copy_to_clipboard)
copy_button.pack(side=LEFT)  # Place the copy button inside the frame

# Alert label to display messages (e.g., success or error)
alert_label = Label(window, text="", fg="red", anchor="w", justify="left", wraplength=580)
alert_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # Position it below the text areas

# Pronunciation Label label to display messages (e.g., success or error)
pronunciation_label = Label(window, text="", fg="Black", anchor="w", justify="left", wraplength=580)
pronunciation_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky="w")  # Position it below the text areas

# Update grid weights to ensure the window is resizable
window.grid_rowconfigure(0, weight=1)  # Allow row 0 to stretch
window.grid_rowconfigure(1, weight=1)  # Allow row 1 to stretch
window.grid_columnconfigure(0, weight=1)  # Allow column 0 to stretch
window.grid_columnconfigure(1, weight=0)  # Keep column 1 fixed (buttons won't stretch)

# Start the Tkinter GUI loop
window.mainloop()