import PySimpleGUI as sg
import cv2 as cv

from opencv import mosaic_arr, highlight_boxes
from solution import find_motif_occurrences

problem_title = "Mosaic Browsing"
problem_discription = """
Ihe International Center for the Preservation of Ceramics (ICPC) is searching for motifs in some ancient
mosaics. According to the ICPCs definition. a mosaic is a rectangular grid where each grid square
contains a colored tile. A motif is similar to a mosaic but some of the grid squares can be empty. Figure
G. I shows an example motif and mosaic.
Thc rows of an rg x cg mosaic are numlrred I to from top to bottom. and the columns are
I to from left to right.
A contiguous rectangular subgrid of the mosaic matches tir rm»tif if every tile of ttu• nx»tif matches tir
colcr of the corresr»nding tile of subgrid- Formally. an rp x nu»tif apsrars in an rq c. mosaic
at rx'sition (r, c) if for all i r I S cp.thctilc (r + i — i. c + j —I) exists in the mosaic and
either the square (i, j) in the megif is empty or the tile at in the motif has the same color as the tile
at (r + + J I) in thc rn(baic.
Given the full motif and mosaic. find all occurrences of the motif in mosaic.
"""

# Define the window's contents
layout_1 = [
    [sg.Text(problem_title)],
    [sg.Image(filename="images/hero.png")],
    [sg.Text(problem_discription)],
    [sg.Button("Start")],
]


def new_motif_InputText(i, enable_events=True):
    return sg.Frame("", [[sg.Text(f"Row {i + 1}"), sg.InputText(key=f"motif_{i}", enable_events=enable_events)]], key=f"motif_{i}_frame")


def new_mosaic_InputText(i, enable_events=True):
    return sg.Frame("", [[sg.Text(f"Row {i + 1}"), sg.InputText(key=f"mosaic_{i}", enable_events=enable_events)]], key=f"mosaic_{i}_frame")


layout_2 = [
    [sg.Text("Enter the number of rows and columns of motif:")],
    [sg.Text("Rows: "), sg.InputText(key="motif_rows", enable_events=True)],
    [sg.Text("Columns: "), sg.InputText(key="motif_cols", enable_events=True)],
    [sg.Column([], key="motif_list", scrollable=True, expand_x=True, size=(200, 150),
               vertical_scroll_only=True)],
    [sg.HorizontalSeparator()],
    [sg.Text("Enter the number of rows and columns of mosaic:")],
    [sg.Text("Rows: "), sg.InputText(key="mosaic_rows", enable_events=True)],
    [sg.Text("Columns: "), sg.InputText(
        key="mosaic_cols", enable_events=True)],
    [sg.Column([], key="mosaic_list", scrollable=True, expand_x=True, size=(200, 300),
               vertical_scroll_only=True)],
    [sg.Button("Solve")],
]

layout_3 = [[
    [[sg.Text("Found"), sg.Text(key="found"), sg.Text("occurrence(s).")],
     [
        sg.Column([[sg.Image(key="motif_image")]], size=(
            200, 200), scrollable=True, key="images"),
        sg.VerticalSeparator(),
        sg.Column([[sg.Image(key="mosaic_image")]], size=(
            200, 200), scrollable=True, key="images")],
     [sg.Button("Show", key="solve", enable_events=True)]],
    [sg.HorizontalSeparator()],
    [[sg.Listbox(values=[], size=(30, 6), key="occurrence_list")],
     [sg.Button("Next"), sg.Button("Previous")]],
    [sg.Button("Exit")]
]]

# Create the window
window_1 = sg.Window("Mosaic Browsing", layout_1)
window_2 = sg.Window("Mosaic Browsing", layout_2)
window_3 = sg.Window("Mosaic Browsing", layout_3)

state = 0

prev_motif_rows = 0
prev_mosaic_rows = 0

motif_rows = 0
motif_cols = 0
motif = []

mosaic_rows = 0
mosaic_cols = 0
mosaic = []


# --- For testing ---
# state = 2

# motif_rows, motif_cols = 2, 2
# motif = np.array([[1, 0], [0, 1]])
# mosaic_rows, mosaic_cols = 3, 4
# mosaic = np.array([[1, 2, 1, 2], [2, 1, 1, 1], [2, 2, 1, 3]])
# --- For testing ---

updated = False
cur_highlight = 0


def highlight_cur():
    r1, c1 = occurrences[cur_highlight]
    r1, c1 = r1 - 1, c1 - 1
    r2, c2 = r1 + motif_rows, c1 + motif_cols
    window_3["mosaic_image"].update(data=cv.imencode(
        ".png", highlight_boxes(mosaic_img, r1, c1, r2, c2))[1].tobytes())


# Display and interact with the Window using an Event Loop
while True:
    match state:
        case 0:
            event, values = window_1.read()
            if event == "Start":
                window_1.close()
                state = 1
            elif event == sg.WIN_CLOSED:
                window_1.close()
                break
        case 1:
            event, values = window_2.read()
            if event == "motif_rows" or event == "mosaic_rows":
                if event == "motif_rows":
                    prefix = "motif"
                    prev = prev_motif_rows
                    new_InputText = new_motif_InputText
                else:
                    prefix = "mosaic"
                    prev = prev_mosaic_rows
                    new_InputText = new_mosaic_InputText

                if values[f"{prefix}_rows"].strip() != "":
                    try:
                        int(values[f"{prefix}_rows"])
                    except ValueError:

                        window_2[f"{prefix}_rows"].update(
                            values[f"{prefix}_rows"][:-1])
                    else:
                        cur = int(values[f"{prefix}_rows"])
                        for i in range(prev):
                            window_2[f"{prefix}_{i}_frame"].update(
                                visible=False)
                            window_2[f"{prefix}_{i}_frame"].Widget.pack_forget()

                        window_2[f"{prefix}_list"].Widget.update()
                        window_2[f"{prefix}_list"].contents_changed()

                        window_2.extend_layout(window_2[f"{prefix}_list"], [
                            [new_InputText(i)] for i in range(cur)])
                        window_2[f"{prefix}_list"].Widget.update()
                        window_2[f"{prefix}_list"].contents_changed()

                    if prefix == "motif":
                        prev_motif_rows = cur
                    else:
                        prev_mosaic_rows = cur
            elif event == "Solve":
                try:
                    motif_rows = int(values["motif_rows"])
                    motif_cols = int(values["motif_cols"])
                    mosaic_rows = int(values["mosaic_rows"])
                    mosaic_cols = int(values["mosaic_cols"])
                except ValueError:
                    pass
                else:
                    motif = [
                        [x for x in map(int, values[f"motif_{i}"].split())] for i in range(motif_rows)]
                    mosaic = [[x for x in map(int, values[f"mosaic_{i}"].split())] for i in range(
                        mosaic_rows)]
                    print(motif)
                    print(mosaic)

                    window_2.close()
                    state = 2
            elif event == sg.WIN_CLOSED:
                window_2.close()
                break
        case 2:
            event, values = window_3.read()
            if (event == "solve") or not updated:
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
                window_3["occurrence_list"].update(
                    [f"{'✅' if i == cur_highlight else '  '} ({x}, {y})" for i, (x, y) in enumerate(occurrences)])
                updated = True
                highlight_cur()

            if event == sg.WIN_CLOSED or event == "Exit":
                window_3.close()
                break

            if event == "Next":
                if cur_highlight + 1 < len(occurrences):
                    cur_highlight += 1
                else:
                    cur_highlight = 0

                highlight_cur()
                window_3["occurrence_list"].update(
                    [f"{'✅' if i == cur_highlight else '  '} ({x}, {y})" for i, (x, y) in enumerate(occurrences)])

            if event == "Previous":
                if cur_highlight - 1 >= 0:
                    cur_highlight -= 1
                else:
                    cur_highlight = len(occurrences) - 1

                highlight_cur()
                window_3["occurrence_list"].update(
                    [f"{'✅' if i == cur_highlight else '  '} ({x}, {y})" for i, (x, y) in enumerate(occurrences)])
