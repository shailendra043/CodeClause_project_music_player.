import pygame
from tkinter import *
from tkinter import filedialog

# Initialize Pygame
pygame.init()

# Create a Tkinter window
root = Tk()
root.title("Music Player")
root.geometry("500x200")
root.config(bg="#2C3E50") # Set background color

# Create Pygame mixer object
pygame.mixer.init()

# Function to play a selected song
def play_music():
    # Get the selected file from file dialog
    file_path = filedialog.askopenfilename()
    # Load the selected file into Pygame mixer
    pygame.mixer.music.load(file_path)
    # Start playing the music
    pygame.mixer.music.play()

# Create a button to select and play music
play_button = Button(root, text="Select and Play Music", command=play_music, bg="#E74C3C", fg="#FFF")
play_button.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
