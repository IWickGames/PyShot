import os
import random
from io import BytesIO

import keyboard
import win32clipboard
import imageGrabber
from PIL import Image
import PySimpleGUI as sg


def send_to_clipboard(imagedata):
    location = f"C:\\Users\\{os.getlogin()}\\AppData\\Local\\Temp\\{random.randint(1, 999999)}.png"
    with open(location, "wb") as f:
        f.write(imagedata)

    image = Image.open(location)

    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    win32clipboard.CloseClipboard()

    os.remove(location)


def screenShotCall():
    grabbedImage = imageGrabber.shot()

    layout = [[sg.Text("Select a way to save the image")],
              [sg.FileSaveAs("Save to file"), sg.Button("Save")],
              [sg.Button("Copy to clipboard")],
              [sg.Button("Cancel")]]
    window = sg.Window("PyShot - Save Image", layout)
    while True:
        event, values = window.read()

        if event == "Save":
            saveLocation = values["Save to file"]

            if not saveLocation.lower().endswith(".png"):
                saveLocation += ".png"

            try:
                with open(saveLocation, "wb") as f:
                    f.write(grabbedImage)
            except Exception as errorInstance:
                sg.popup("Failed to save Image, make sure you have "
                         "permission to access that file or folder\n{}".format(errorInstance))
                break

            sg.popup("Saved image to disk")
            break

        if event == "Copy to clipboard":
            send_to_clipboard(grabbedImage)
            sg.popup("Exported image to your clipboard")
            break

        if event == "Cancel" or event == sg.WIN_CLOSED:
            break

    window.close()
    return


while True:
    if keyboard.is_pressed("Print_Screen"):
        screenShotCall()
