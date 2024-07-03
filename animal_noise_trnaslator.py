import tkinter as tk
import random
import pygame
import threading
import os

# Initialize Pygame mixer
pygame.mixer.init()

# Define the path to the directory containing sound files
sound_dir = "C:/Users/rocky/OneDrive/Documents/Desktop/hackclub/noise translator/"

# Dictionary to hold animal sounds with full paths
animal_sounds = {
    "Cat": os.path.join(sound_dir, "cat_meow.mp3"),
    "Dog": os.path.join(sound_dir, "dog_bark.mp3"),
    "Cow": os.path.join(sound_dir, "cow_moo.mp3"),
    "Sheep": os.path.join(sound_dir, "sheep_baa.mp3"),
    "Lion": os.path.join(sound_dir, "lion_roar.mp3")
}

# Function to play the animal sound
def play_sound(animal):
    sound_file = animal_sounds[animal]
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play()

# Function to handle button click
def translate():
    animal = random.choice(list(animal_sounds.keys()))
    result_label.config(text=f"{animal} says...")
    threading.Thread(target=play_sound, args=(animal,), daemon=True).start()

# Create the main window
root = tk.Tk()
root.title("Random Animal Noise Translator")

# Create and place the widgets
instruction_label = tk.Label(root, text="Press the button to hear a random animal noise!")
instruction_label.pack(pady=20)

translate_button = tk.Button(root, text="Translate", command=translate)
translate_button.pack(pady=20)

result_label = tk.Label(root, text="", font=("Helvetica", 24))
result_label.pack(pady=20)

# Start the Tkinter event loop
root.mainloop()
