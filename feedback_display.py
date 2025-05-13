import tkinter as tk
from PIL import Image, ImageTk  # Zorg dat Pillow geïnstalleerd is
import serial
import threading

# Veilig proberen verbinding te maken met Arduino
try:
    arduino = serial.Serial('/dev/tty.usbmodem312301', 9600)
except Exception as e:
    print("❌ Kan geen verbinding maken met de Arduino:")
    print(e)
    exit()

score_yes = 0
score_no = 0

def read_serial():
    global score_yes, score_no
    while True:
        try:
            line = arduino.readline().decode('utf-8').strip()
            if line == "COUNTING:":
                yes_line = arduino.readline().decode('utf-8').strip()
                no_line = arduino.readline().decode('utf-8').strip()

                score_yes = int(yes_line.split(": ")[1])
                score_no = int(no_line.split(": ")[1])

                update_display()
        except Exception as e:
            print("🔴 Serial error:", e)

def update_display():
    label_yes.config(text=f"YES: {score_yes}")
    label_no.config(text=f"NO: {score_no}")

# GUI
root = tk.Tk()
root.title("Fontys Feedback Machine")
root.configure(bg='#4B306A')

# Zet venster op tweede scherm (rechts van MacBook bij 1920px breedte)
try:
    root.geometry("+1920+0")  # of +2560+0 als je scherm nog groter is
except Exception as e:
    print("⚠️ Kon venster niet verplaatsen:", e)

root.attributes('-fullscreen', True)

def herstel_fullscreen(event=None):
    root.attributes('-fullscreen', True)

# Als focus verloren gaat (klikken naast venster), herstel fullscreen
root.bind("<FocusOut>", herstel_fullscreen)


# Stelling in meerdere regels, gecentreerd
stelling_text = "Is this a fun and effective\nway to share your opinion?"
stelling = tk.Label(root, text=stelling_text,
                    font=("Arial", 80, 'bold'),
                    fg="white", bg='#4B306A',
                    justify='center')
stelling.pack(pady=(100, 50))

# Score onderaan
score_frame = tk.Frame(root, bg='#4B306A')
score_frame.pack(side='bottom', pady=100)

label_yes = tk.Label(score_frame, text="YES: 0", font=("Arial", 70, 'bold'),
                     fg="#7CFC00", bg='#4B306A', padx=90)
label_yes.pack(side='left')

label_no = tk.Label(score_frame, text="NO: 0", font=("Arial", 70, 'bold'),
                    fg="#FF5F1F", bg='#4B306A', padx=90)
label_no.pack(side='left')

# ESC sluit scherm
def sluit_af(event):
    root.destroy()

root.bind("<Escape>", sluit_af)

# Start serial reader
threading.Thread(target=read_serial, daemon=True).start()

root.mainloop()
