from PIL import Image, ImageDraw, ImageFont
import PySimpleGUI as sg

# Create 10 Images for the execution of this script
# font = ImageFont.truetype("arial.ttf", 80)
# for i in range(10):
#     im = Image.new("RGBA", (320, 240), "blue")
#     draw = ImageDraw.Draw(im, mode='RGBA')
#     draw.text((160, 120), f'{i:0>2d}.png',
#               font=font, anchor='mm', align='center')
#     im.save(f'{i:0>2d}.png')

image_set = [f'{i:0>2d}.png' for i in range(10)]

sg.set_options(dpi_awareness=True)  # For WINDOWS, maybe not necessary

layout2 = [[sg.Image(filename=image_set[0], size=(320, 240), key='-IMAGE-')]]
window2 = sg.Window("Image", layout2, finalize=True, no_titlebar=True)
x, y = window2.current_location()

layout1 = [[sg.RButton("OK"), sg.Button("Cancel")]]
window1 = sg.Window("Count", layout1, location=(x-200, y), finalize=True)

index = 0
while True:

    event, values = window1.read()
    if event in (sg.WIN_CLOSED, 'Cancel'):
        break
    elif event == 'OK':
        index = (index + 1) % 10
        window2['-IMAGE-'].update(filename=image_set[index])

window2.close()
window1.close()
