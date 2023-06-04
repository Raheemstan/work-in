import time
import os
import pygame
import sys

"""
Version: 1.3
Author: Michael Raheem
Name: Workout Routine
Desc: Script for a daily workout session
"""

routine_file = "routine.txt"  # Path to the external routine file
duration = int(input("Enter the start time per routine in seconds (e.g., 45): "))
rest = duration // 3  # resting time

with open(routine_file, "r") as file:
    routine = file.read().splitlines()

playlist_folder = "playlist/"

# Initialize the pygame mixer
pygame.mixer.init()

# Get a list of all files in the playlist folder
playlist_files = os.listdir(playlist_folder)
# Filter the files to include only supported audio formats (e.g., mp3, wav, etc.)
supported_formats = (".mp3", ".wav")
playlist_files = [file for file in playlist_files if file.lower().endswith(supported_formats)]

# Play each song in the playlist folder
for song_file in playlist_files:
    song_path = os.path.join(playlist_folder, song_file)
    pygame.mixer.music.load(song_path)
    print(f"Now playing: {song_file}")
    pygame.mixer.music.play()

    # Wait until the current song finishes playing
    while pygame.mixer.music.get_busy():
        for index, exercise in enumerate(routine):
            print(f"Countdown started for {exercise}")
            time.sleep(1)

            for i in range(duration, 0, -1):
                print(f"{i} seconds remaining...")
                time.sleep(1)

            if index < len(routine) - 1:
                print(f"{rest} seconds rest \nGet in position for {routine[index + 1]}")
            else:
                print("Great Workout Today! \nSee you tomorrow")
                pygame.mixer.music.stop()
                sys.exit()

            time.sleep(rest)
            continue
print("Playlist finished playing.")
