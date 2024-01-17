import PySimpleGUI as sg

sg.theme('DarkBlue3')

words = "This is a book".split(' ')
layout = [
    [sg.Input(key='-IN-')],
    [sg.Push()] + [sg.Button(word, size=4) for word in words],
]
window = sg.Window("Title", layout, finalize=True)

while True:

    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event in words:
        text = values['-IN-'].strip()
        text = text + (' ' if text else '') + event
        window['-IN-'].update(text)

window.close()
