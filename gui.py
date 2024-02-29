
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"/Users/visveshnaraharisetty/Desktop/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("480x320")
window.configure(bg="#FFFFFF")


canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=320,
    width=480,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    240.0,
    160.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    86.0,
    269.2799987792969,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    432.8800048828125,
    306.4000244140625,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    176.0,
    306.4000244140625,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    367.0,
    149.0,
    image=image_image_5
)

canvas.create_text(
    16.0,
    57.0,
    anchor="nw",
    text="Naveen Kumar",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    16.0,
    115.0,
    anchor="nw",
    text="18XJ1A0505",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    16.0,
    215.0,
    anchor="nw",
    text="Ecole Centrale School of Engineering",
    fill="#E31138",
    font=("Inter Bold", 14 * -1)
)

canvas.create_text(
    16.0,
    145.0,
    anchor="nw",
    text="Hostler ",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    16.0,
    174.0,
    anchor="nw",
    text="Suspended / Leave approved",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    160.0,
    16.0,
    anchor="nw",
    text="        58% ",
    fill="#000000",
    font=("Inter Bold", 16 * -1)
)

canvas.create_text(
    16.0,
    16.0,
    anchor="nw",
    text="D-1     IN GATE ",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_rectangle(
    15.0,
    48.0,
    253.00000113248734,
    49.0,
    fill="#000000",
    outline="")

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    241.0,
    25.0,
    image=image_image_6
)
window.resizable(False, False)
window.mainloop()
