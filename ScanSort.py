import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import os

# Globals to hold image and path
img_path = None
image = None

def open_image():
    global img_path, image
    img_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png *.bmp *.gif")])
    if img_path:
        image = Image.open(img_path)
        image.thumbnail((400, 400))
        img = ImageTk.PhotoImage(image)
        panel.config(image=img)
        panel.image = img

def save_metadata():
    global img_path, image
    year = year_entry.get().strip()
    notes = notes_entry.get().strip()

    if not (img_path and year):
        messagebox.showwarning("Missing Info", "Please open an image and enter a year.")
        return

    base_name = os.path.basename(img_path)
    name_part = os.path.splitext(base_name)[0]
    filename = f"{name_part}_{year}.jpg"

    # Choose save path
    save_path = filedialog.asksaveasfilename(defaultextension=".jpg", initialfile=filename,
                                             filetypes=[("JPEG", "*.jpg"), ("PNG", "*.png")])
    if save_path:
        image.convert("RGB").save(save_path)
        notes_path = save_path.replace(".jpg", ".txt").replace(".png", ".txt")
        with open(notes_path, 'w') as f:
            f.write(f"Year: {year}\nNotes: {notes}")
        messagebox.showinfo("Saved", f"Image saved as:\n{save_path}\n\nNotes saved as:\n{notes_path}")

# Setup GUI
root = tk.Tk()
root.title("ScanSort")
root.geometry("500x600")

panel = tk.Label(root)
panel.pack(pady=10)

open_btn = tk.Button(root, text="Open Image", command=open_image)
open_btn.pack(pady=5)

tk.Label(root, text="Year:").pack(pady=2)
year_entry = tk.Entry(root)
year_entry.pack(pady=2)

tk.Label(root, text="Notes:").pack(pady=2)
notes_entry = tk.Entry(root)
notes_entry.pack(pady=2)

save_btn = tk.Button(root, text="Save Metadata", command=save_metadata)
save_btn.pack(pady=10)

root.mainloop()
