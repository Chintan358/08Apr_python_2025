import tkinter as tk
from tkinter import filedialog, ttk
import pygame
import os
import time
import threading
import random

# Initialize pygame mixer
pygame.mixer.init()

# App setup
root = tk.Tk()
root.title("🎵 Visual Music Player")
root.geometry("500x600")
root.configure(bg="#121212")
root.resizable(False, False)

current_song = tk.StringVar()
current_song.set("🎶 No song selected")
is_playing = False
song_path = ""

# Load song
def load_song():
    global song_path
    file = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if file:
        song_path = file
        pygame.mixer.music.load(file)
        current_song.set("🎶 " + os.path.basename(file))
        progress_bar["value"] = 0
        duration_label.config(text="00:00 / 00:00")

# Play song
def play_song():
    global is_playing
    if song_path:
        pygame.mixer.music.play()
        is_playing = True
        update_progress()
        animate_beats()

# Pause song
def pause_song():
    global is_playing
    pygame.mixer.music.pause()
    is_playing = False

# Resume song
def resume_song():
    global is_playing
    pygame.mixer.music.unpause()
    is_playing = True
    update_progress()
    animate_beats()

# Stop song
def stop_song():
    global is_playing
    pygame.mixer.music.stop()
    is_playing = False
    progress_bar["value"] = 0
    duration_label.config(text="00:00 / 00:00")

# Progress updater
def update_progress():
    def run():
        while is_playing and pygame.mixer.music.get_busy():
            pos = pygame.mixer.music.get_pos() // 1000
            if song_path:
                try:
                    audio = pygame.mixer.Sound(song_path)
                    duration = int(audio.get_length())
                    percent = (pos / duration) * 100 if duration > 0 else 0
                    progress_bar["value"] = percent
                    duration_label.config(text=f"{time.strftime('%M:%S', time.gmtime(pos))} / {time.strftime('%M:%S', time.gmtime(duration))}")
                except:
                    pass
            time.sleep(1)
    threading.Thread(target=run, daemon=True).start()

# Beat animation
def animate_beats():
    def run():
        while is_playing and pygame.mixer.music.get_busy():
            for bar in beat_bars:
                bar_height = random.randint(10, 100)
                bar.config(height=bar_height)
            time.sleep(0.2)
    threading.Thread(target=run, daemon=True).start()

# UI Components
tk.Label(root, text="🎧 Visual Music Player", font=("Segoe UI", 20, "bold"), bg="#121212", fg="#00e6e6").pack(pady=20)
tk.Label(root, textvariable=current_song, font=("Segoe UI", 12), bg="#121212", fg="#00ffff").pack(pady=5)

btn_frame = tk.Frame(root, bg="#121212")
btn_frame.pack(pady=20)

button_cfg = {"font": ("Segoe UI", 11, "bold"), "width": 12, "height": 2, "bg": "#1f1f1f", "fg": "#00e6e6", "bd": 0, "activebackground": "#2a2a2a"}

tk.Button(btn_frame, text="📂 Load", command=load_song, **button_cfg).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="▶️ Play", command=play_song, **button_cfg).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="⏸️ Pause", command=pause_song, **button_cfg).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="▶️ Resume", command=resume_song, **button_cfg).grid(row=1, column=1, padx=5, pady=5)
tk.Button(root, text="⏹️ Stop", command=stop_song, **button_cfg).pack(pady=10)

# Progress Bar
tk.Label(root, text="Progress", bg="#121212", fg="white", font=("Segoe UI", 12)).pack(pady=(10, 0))
progress_bar = ttk.Progressbar(root, orient="horizontal", length=400, mode="determinate")
progress_bar.pack(pady=5)

# Duration label
duration_label = tk.Label(root, text="00:00 / 00:00", bg="#121212", fg="gray", font=("Segoe UI", 10))
duration_label.pack()

# Beat Visualizer
tk.Label(root, text="Beat Visualizer", bg="#121212", fg="white", font=("Segoe UI", 12)).pack(pady=(20, 0))
visualizer_frame = tk.Frame(root, bg="#121212")
visualizer_frame.pack(pady=10)

beat_bars = []
for i in range(20):
    bar = tk.Frame(visualizer_frame, width=10, height=20, bg="#00e6e6")
    bar.grid(row=0, column=i, padx=2)
    beat_bars.append(bar)

# Footer
tk.Label(root, text="Made with ❤️ using Tkinter", bg="#121212", fg="#555", font=("Segoe UI", 9)).pack(side="bottom", pady=10)

root.mainloop()
