from tkinter import *
import customtkinter
import pyttsx3
import pygame

languages = {}
engine = pyttsx3.init(debug=True, driverName=None)
voices = engine.getProperty('voices')
for voice in voices:
    languages[voice.name.split("-")[1]] = voice.id
engine.runAndWait()

languagesArray = []
for language in languages:
    languagesArray.append(language)


def convert_text_to_speech():
    # make sure pygame does not block files from being changed or deleted
    pygame.quit()

    # input text to be converted to speech
    text = inputField.get()

    # speed is measured in words per minute
    speed = speedSlider.get()
    volume = volumeSlider.get()
    language = languageSelection.get()

    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init(debug=True, driverName=None)

    # set properties
    engine.setProperty('rate', speed)
    engine.setProperty('volume', volume)
    engine.setProperty('voice', languages[language])

    # use engine to save audio to a file
    engine.save_to_file(text, 'output.wav')
    engine.runAndWait()


    # use pygame to play the audio file
    pygame.mixer.init()
    pygame.mixer.music.load('./output.wav')
    pygame.mixer.music.play()


# pause and unpause the audio
def pause_audio():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

# update the volume label
def updateVolumeLabel(event):
    currentVolume = volumeSlider.get()
    volumeDisplay.configure(text="volume: " + str("%.2f" % round(currentVolume,2)))

# update the speed label
def updateSpeedLabel(event):
    currentSpeed = speedSlider.get()
    speedDisplay.configure(text="speed: " + str("%.2f" % round(currentSpeed,2)))


# 
# custometkinter ui

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()

root.geometry("500x500")

# 
# title label
titleLabel = customtkinter.CTkLabel(root, text="Text-to-Speech Program", font=("Arial", 20))

titleLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

languageSelection = customtkinter.CTkOptionMenu(root, values=languagesArray)

languageSelection.place(relx=0.5, rely=0.2, anchor=CENTER)

# 
# input field
inputField = customtkinter.CTkEntry(root,placeholder_text="enter text", width=150, height=20)

inputField.place(relx=0.5, rely=0.3, anchor=CENTER)

# 
# create volume slider
volumeSlider = customtkinter.CTkSlider(root, from_=0, to=1, number_of_steps=100, command=updateVolumeLabel)

volumeSlider.set(0.5)

volumeSlider.place(relx=0.5, rely=0.4, anchor=CENTER)

# 
# volume display
currentVolume = volumeSlider.get()
volumeDisplay = customtkinter.CTkLabel(root, text="volume: " + str(currentVolume * 10))

volumeDisplay.place(relx=0.8, rely=0.4, anchor=CENTER)


# 
# speed slider
speedSlider = customtkinter.CTkSlider(root, from_=50, to=300, command=updateSpeedLabel)

speedSlider.set(150)

speedSlider.place(relx=0.5, rely=0.5, anchor=CENTER)

# 
# speed display
currentSpeed = speedSlider.get()
speedDisplay = customtkinter.CTkLabel(root, text="speed: " + str(currentSpeed))

speedDisplay.place(relx=0.8, rely=0.5, anchor=CENTER)

# 
# record button
recordButton = customtkinter.CTkButton(root, text="record", command=convert_text_to_speech)

recordButton.place(relx=0.5, rely=0.6, anchor=CENTER)

# 
# pause/play button 
pausePlayButton = customtkinter.CTkButton(root, text="pause/play", command=pause_audio)

pausePlayButton.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()