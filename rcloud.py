import PySimpleGUIQt as sg
import os

# sg.theme("DarkAmber")  # Add a touch of color
# All the stuff inside your window.
layout = [
    [sg.Text("Cloud Mount")],
    [sg.Button("OneDrive")],
    [sg.Button("DreamHost")],
    [sg.Button("GoogleDrive")],
    [sg.Button("DropBox")],
    [sg.Button("Cancel")],
]

# Create the Window
window = sg.Window("Cloud Mount", layout, font=("Helvetica", 20))
# Event Loop to process "events" and get the "values" of the inputs
while True:
    event, values = window.read()
    if (
        event == sg.WIN_CLOSED or event == "Cancel"
    ):  # if user closes window or clicks cancel
        break
    os.system(f"/Users/carvalho/bin/cloudmount {event}")

window.close()
