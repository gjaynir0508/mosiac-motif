import PySimpleGUI as sg

FONT_FAMILY = "Merriweather"
FONT_SIZE = 12
FONT = (FONT_FAMILY, FONT_SIZE)

HEADING_FONT_SIZE = 20
HEADING_FONT = (FONT_FAMILY, HEADING_FONT_SIZE)

SIZE = (800, 600)
WINDOW_BG = "#222222"
TEXT_COLOR = "#EEEEEE"
SECONDARY = "#333333"


problem_title_text = "Mosaic Browsing"


def HPush(): return sg.Push(background_color=WINDOW_BG)
def VPush(): return sg.VPush(background_color=WINDOW_BG)


def InputColumn(prefix):
    return sg.Column(
        [
            [sg.Text(f"{prefix}", pad=((0, 0), (0, 16)), font=(
                FONT_FAMILY, 13), background_color=WINDOW_BG)],
            [sg.Text(f"No. of Rows in {prefix}: ", background_color=WINDOW_BG, pad=((48, 0), (0, 12))), HPush(), sg.InputText(
                key=f"{prefix.lower()}_rows", enable_events=True, size=(3, 1), justification="center", pad=((0, 16), (0, 12)))],
            [sg.Text(f"No. of Columns in {prefix}: ", background_color=WINDOW_BG, pad=((48, 0), (0, 12))), HPush(), sg.InputText(
                key=f"{prefix.lower()}_cols", enable_events=True, size=(3, 1), justification="center", pad=((0, 16), (0, 12)))],
            [sg.Column([], key=f"{prefix.lower()}_list", scrollable=True, expand_x=True, size=(200, 150),
                       vertical_scroll_only=True)]],
        expand_x=True, expand_y=True, key=f"{prefix}", justification="center", pad=(20, 16)
    )


problem_title = [
    sg.Text(problem_title_text, font=HEADING_FONT, expand_x=True, justification="center", background_color=WINDOW_BG, text_color="white", pad=(0, 64))]

start_button = [
    sg.Button("Start", button_color=("#1E1E1E", "white"), enable_events=True,
              font=FONT, pad=(0, 0), expand_x=True, mouseover_colors=("white", "#333"), key="Start"),
]
