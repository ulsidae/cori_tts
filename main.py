import tkinter as tk
from tkinter import filedialog
import subprocess
import os
import sys
from PIL import Image, ImageTk

# ===== BASE PATH  =====
if getattr(sys, 'frozen', False):
    BASE_DIR = os.path.dirname(sys.executable) 
else:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_DIR = os.path.join(BASE_DIR, "models")
ASSET_PATH = os.path.join(BASE_DIR, "character.png")

OUTPUT_DIR = os.path.join(BASE_DIR, "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

OUTPUT_FILE = os.path.join(OUTPUT_DIR, "output.wav")


# ===== AUTO MODEL FIND =====
def find_model():
    if not os.path.exists(MODEL_DIR):
        return None
    for f in os.listdir(MODEL_DIR):
        if f.endswith(".onnx"):
            return os.path.join(MODEL_DIR, f)
    return None


MODEL = find_model()

if MODEL is None:
    raise Exception("No .onnx model found in models folder")


# ===== SELECT FILE =====
def select_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt")]
    )
    if file_path:
        entry.delete(0, tk.END)
        entry.insert(0, file_path)


# ===== RUN TTS =====
def run_tts():
    input_path = entry.get()

    if not os.path.exists(input_path):
        status_label.config(text="file not found")
        return

    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read().strip()

    PIPER_EXE = os.path.join(BASE_DIR, "piper", "piper.exe")

    if not os.path.exists(PIPER_EXE):
        status_label.config(text="piper.exe not found")
        return

    subprocess.run([
        PIPER_EXE,
        "--model", MODEL,
        "--output_file", OUTPUT_FILE
    ], input=text.encode("utf-8"), creationflags=subprocess.CREATE_NO_WINDOW)

    status_label.config(text="complete")

    if os.path.exists(OUTPUT_DIR):
        os.startfile(OUTPUT_DIR)


# ===== UI =====
root = tk.Tk()
root.title("cori tts - by ulsidae")
root.geometry("300x340")
root.resizable(False, False)

# ===== IMAGE SAFE LOAD =====
if os.path.exists(ASSET_PATH):
    img = Image.open(ASSET_PATH).resize((200, 200))
    photo = ImageTk.PhotoImage(img)

    img_label = tk.Label(root, image=photo)
    img_label.image = photo
    img_label.pack(pady=10)

# ===== ENTRY =====
entry = tk.Entry(root, width=40)
entry.pack(pady=10)

btn_select = tk.Button(root, text="Select TXT", command=select_file)
btn_select.pack(pady=5)

btn_run = tk.Button(root, text="RUN TTS", command=run_tts)
btn_run.pack(pady=5)

status_label = tk.Label(root, text="")
status_label.pack(pady=10)

root.mainloop()
