import PySimpleGUI as sg
import cv2 as cv

from opencv import mosaic_arr, highlight_boxes, color_from_number
from solution import find_motif_occurrences

import elements as e

sg.set_options(background_color=e.WINDOW_BG,
               text_color=e.TEXT_COLOR, font=e.FONT, border_width=0)


# Define the window's contents
layout_1 = [
    [sg.Button("", image_filename="./images/start_screen.png",
               image_size=e.SIZE, border_width=0, pad=(0, 0), key="Start")],
]


def new_motif_InputText(i, cols, enable_events=True):
    return sg.pin(sg.Column([[sg.InputText(key=("motif", i, col, "box"), justification="center", enable_events=enable_events, size=(4, 4)) for col in range(cols)]], key=("motif", i, "frame")))


def new_mosaic_InputText(i, cols, enable_events=True):
    return sg.pin(sg.Column([[sg.InputText(key=("mosaic", i, col, "box"), justification="center", enable_events=enable_events, size=(4, 4)) for col in range(cols)]], key=("mosaic", i, "frame")))


layout_2 = [
    [sg.Text("Inputs", font=e.HEADING_FONT,
             background_color=e.WINDOW_BG, justification="center", expand_x=True, pad=((0, 0), (12, 32)))],
    [
        e.InputColumn("Motif"),
        sg.VerticalSeparator(color=e.SECONDARY),
        e.InputColumn("Mosaic")],
    [
        sg.pin(sg.Text("Invalid Input ☹️", key="invalid", visible=False,
               text_color="tomato", font=(e.FONT_FAMILY, 12), pad=(64, 0), background_color=e.WINDOW_BG)),
        e.HPush(),
        sg.Button("", image_filename="./images/solve_btn.png", image_size=(176, 57), size=(16, 3),
                  button_color=(e.WINDOW_BG, e.WINDOW_BG), pad=(32, 32), key="Solve")
    ],
]

layout_3 = [[
    [[sg.Column([[
            sg.Text("Found", background_color=e.WINDOW_BG,
                    font=(e.FONT_FAMILY, 14)),
            sg.Text(key="found", background_color=e.WINDOW_BG,
                    font=(e.FONT_FAMILY, 16)),
            sg.Text("occurrence(s).", background_color=e.WINDOW_BG,
                    font=(e.FONT_FAMILY, 14))
            ]], justification="center")],
     [
        sg.Column([[sg.Image(key="motif_image")]], expand_x=True,
                  expand_y=True, scrollable=True, key="images"),
        sg.VerticalSeparator(color=e.SECONDARY),
        sg.Column([[sg.Image(key="mosaic_image")]], expand_x=True,
                  expand_y=True, scrollable=True, key="images")
    ]],
    [sg.Text("Occurrences", background_color=e.WINDOW_BG, pad=((0, 0), (16, 0)))],
    [
        sg.Column(
            [[sg.Listbox(values=[], size=(35, 7), background_color=e.WINDOW_BG, text_color=e.TEXT_COLOR, key="occurrence_list")]], size=(400, 200)),
        sg.Column([
            [e.HPush(), sg.Button("", image_filename="./images/previous_btn.png",
                                  image_size=(205 // 1.5, 57 // 1.5), key="Previous"), e.HPush()],
            [e.HPush(), sg.Button("", image_filename="./images/next_btn.png",
                                  image_size=(205 // 1.5, 57 // 1.5), key="Next"), e.HPush()],
        ], size=(400, 200), element_justification="center")],
]]

SIZE = e.SIZE

# Create the window
window_1 = sg.Window("Mosaic Browsing", layout_1, margins=(0, 0), size=SIZE)
window_2 = sg.Window("Mosaic Browsing", layout_2, size=SIZE)
window_3 = sg.Window("Mosaic Browsing", layout_3, size=SIZE, finalize=True)
window_3.hide()


# State and Variables
state = 0

prev_motif_rows = 0
motif_rows_to_remove = 0
prev_mosaic_rows = 0
mosaic_rows_to_remove = 0

motif_rows = 0
motif_cols = 0
motif = []

mosaic_rows = 0
mosaic_cols = 0
mosaic = []

cur_highlight = 0
occurrences = []
mosaic_img = None


def hide_all_frames(prefix, to_remove):
    for i in range(to_remove):
        window_2[(prefix, i, "frame")].update(visible=False)
        # window_2[f"{prefix}_{i}_frame"].Widget.pack_forget()

    window_2[f"{prefix}_list"].Widget.update()
    window_2[f"{prefix}_list"].contents_changed()


def highlight_cur():
    r1, c1 = occurrences[cur_highlight]
    r1, c1 = r1 - 1, c1 - 1
    r2, c2 = r1 + motif_rows, c1 + motif_cols
    window_3["mosaic_image"].update(data=cv.imencode(
        ".png", highlight_boxes(mosaic_img, r1, c1, r2, c2))[1].tobytes())


def occurrence_list():
    return [f"{'✅ㅤ' if i == cur_highlight else 'ㅤㅤ'}({x}, {y})" for i, (x, y) in enumerate(occurrences)]


def draw_images():
    global occurrences, mosaic_img
    window_3.un_hide()
    motif_img = mosaic_arr(motif_rows, motif_cols, motif)
    mosaic_img = mosaic_arr(mosaic_rows, mosaic_cols, mosaic)
    window_3["motif_image"].update(data=cv.imencode(
        ".png", motif_img)[1].tobytes())
    window_3["mosaic_image"].update(data=cv.imencode(
        ".png", mosaic_img)[1].tobytes())
    occurrences = find_motif_occurrences(mosaic, motif)
    window_3["images"].Widget.update()
    window_3["images"].contents_changed()
    window_3["found"].update(len(occurrences))
    window_3["occurrence_list"].update(occurrence_list())
    highlight_cur()


# --- For testing ---
# state = 2
# import numpy as np

# motif_rows, motif_cols = 2, 2
# motif = np.array([[1, 0], [0, 1]])
# mosaic_rows, mosaic_cols = 3, 4
# mosaic = np.array([[1, 2, 1, 2], [2, 1, 1, 1], [2, 2, 1, 3]])
# draw_images()
# --- For testing ---


# Display and interact with the Window using an Event Loop
while True:
    if state == 0:
        event, values = window_1.read()
        if event == "Start":
            window_1.close()
            state = 1
        elif event == sg.WIN_CLOSED:
            window_1.close()
            break
    elif state == 1:
        event, values = window_2.read()
        if event == "motif_rows" or event == "mosaic_rows":
            if event == "motif_rows":
                prefix = "motif"
                prev = prev_motif_rows
                to_remove = motif_rows_to_remove
                new_InputText = new_motif_InputText
            else:
                prefix = "mosaic"
                prev = prev_mosaic_rows
                to_remove = mosaic_rows_to_remove
                new_InputText = new_mosaic_InputText

            if values[f"{prefix}_rows"].strip() != "":
                try:
                    int(values[f"{prefix}_rows"])
                except ValueError:

                    window_2[f"{prefix}_rows"].update(
                        values[f"{prefix}_rows"][:-1])
                else:
                    cur = int(values[f"{prefix}_rows"])
                    hide_all_frames(prefix, to_remove)

                    window_2.extend_layout(window_2[f"{prefix}_list"], [
                        [new_InputText(i, motif_cols)] for i in range(to_remove, to_remove + cur)])
                    window_2[f"{prefix}_list"].Widget.update()
                    window_2[f"{prefix}_list"].contents_changed()

                    if prefix == "motif":
                        prev_motif_rows = cur
                        motif_rows_to_remove += cur
                    else:
                        prev_mosaic_rows = cur
                        mosaic_rows_to_remove += cur

        elif event == "motif_cols" or event == "mosaic_cols":
            if event == "motif_cols":
                prefix = "motif"
                prev = prev_motif_rows
                to_remove = motif_rows_to_remove
                new_InputText = new_motif_InputText
            else:
                prefix = "mosaic"
                prev = prev_mosaic_rows
                to_remove = mosaic_rows_to_remove
                new_InputText = new_mosaic_InputText

            if values[f"{prefix}_cols"].strip() != "":
                try:
                    int(values[f"{prefix}_cols"])
                except ValueError:
                    window_2[f"{prefix}_cols"].update(
                        values[f"{prefix}_cols"][:-1])
                else:
                    cur = int(values[f"{prefix}_cols"])
                    hide_all_frames(prefix, to_remove)

                    window_2.extend_layout(window_2[f"{prefix}_list"], [
                        [new_InputText(i, cur)] for i in range(to_remove, to_remove + prev)])
                    window_2[f"{prefix}_list"].Widget.update()
                    window_2[f"{prefix}_list"].contents_changed()

                    if prefix == "motif":
                        motif_rows_to_remove += prev
                        motif_cols = cur
                    else:
                        mosaic_rows_to_remove += prev
                        mosaic_cols = cur

        elif event == "Solve":
            try:
                motif_rows = int(values["motif_rows"])
                motif_cols = int(values["motif_cols"])
                mosaic_rows = int(values["mosaic_rows"])
                mosaic_cols = int(values["mosaic_cols"])
                for i in range(motif_rows_to_remove - motif_rows, motif_rows_to_remove):
                    for j in range(motif_cols):
                        int(values[("motif", i, j, "box")])

                for i in range(mosaic_rows_to_remove - mosaic_rows, mosaic_rows_to_remove):
                    for j in range(mosaic_cols):
                        int(values[("mosaic", i, j, "box")])
                window_2["invalid"].update(visible=False)
            except ValueError:
                window_2["invalid"].update(visible=True)
            else:
                motif = [
                    [int(values[("motif", i, col, "box")]) for col in range(motif_cols)] for i in range(motif_rows_to_remove - motif_rows, motif_rows_to_remove)]
                print(motif)
                mosaic = [[int(values[("mosaic", i, col, "box")]) for col in range(mosaic_cols)] for i in range(
                    mosaic_rows_to_remove - mosaic_rows, mosaic_rows_to_remove)]
                print(mosaic)

                draw_images()
                window_2.close()
                state = 2
        elif event == sg.WIN_CLOSED:
            window_2.close()
            break
        elif event[3] == "box":
            if values[event].strip() != "":
                try:
                    x = int(values[event])
                    window_2["invalid"].update(visible=False)
                    window_2[event].update(
                        background_color=color_from_number(x)[0])
                except ValueError:
                    window_2[event].update(values[event][:-1])

    elif state == 2:
        event, values = window_3.read()

        if event == sg.WIN_CLOSED or event == "Exit":
            window_3.close()
            break

        if event == "Next" or event == "Previous":
            change = 1 if event == "Next" else -1
            if 0 <= cur_highlight + change < len(occurrences):
                cur_highlight += change
            else:
                cur_highlight = 0 if change == 1 else len(occurrences) - 1

            highlight_cur()
            window_3["occurrence_list"].update(occurrence_list())
