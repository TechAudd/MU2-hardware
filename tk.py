
# This file was generated by the Tkinter Designer by Parth Jadhav

from PIL import Image, ImageTk
import requests
from io import BytesIO

from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"/Users/visveshnaraharisetty/Desktop/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_image_from_url(url, target_width, target_height):
    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((target_width, target_height))
    return ImageTk.PhotoImage(img)


data = [
    {
        "HTNO": "18XJ1A0505",
        "NAME": "Naveen Kumar",
        "BLOOD GROUP": "OB+",
        "SCHOOL": "Ecole Centrale School of Engineering",
        "IMG": "https://musecportal.s3.ap-south-1.amazonaws.com/2019/19XJ1A0101.JPG",
    },
    {
        "HTNO": "18XJ1A0506",
        "NAME": "Lokesh",
        "BLOOD GROUP": "B+",
        "SCHOOL": "Ecole Centrale School of Engineering",
        "IMG": "https://musecportal.s3.ap-south-1.amazonaws.com/2019/19XJ1A0103.JPG"
    },
    {
        "HTNO": "18XJ1A0507",
        "NAME": "Abhi",
        "BLOOD GROUP": "OB-",
        "SCHOOL": "Ecole Centrale School of Managment",
        "IMG": "https://musecportal.s3.ap-south-1.amazonaws.com/2019/19XJ1A0107.JPG"
    },
    {
        "HTNO": "18XJ1A0508",
        "NAME": "Kumar",
        "BLOOD GROUP": "AB-",
        "SCHOOL": "Ecole Centrale School of Engineering",
        "IMG": "https://musecportal.s3.ap-south-1.amazonaws.com/2019/19XJ1A0104.JPG"
    },
    {
        "HTNO": "18XJ1A0509",
        "NAME": "Naveen Kumar",
        "BLOOD GROUP": "O+",
        "SCHOOL": "Ecole Centrale School of Law",
        "IMG": "https://musecportal.s3.ap-south-1.amazonaws.com/2019/19XJ1A0105.JPG"
    }
]

window = Tk()

window.geometry("480x320")
window.configure(bg="#FFFFFF")
window.attributes('-type', 'dock')

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
# print(image_image_1)
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

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    241.0,
    25.0,
    image=image_image_6
)
name_text = canvas.create_text(
    16.0,
    57.0,
    anchor="nw",
    text="DayScholar",
    fill="#000000",
    font=("Inter Bold", 16 * -1, "bold")
)

id_text = canvas.create_text(
    16.0,
    115.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter Bold", 16 * -1, "bold")
)

school_text = canvas.create_text(
    16.0,
    174.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter Bold", 16 * -1,  'bold')
)

a_type = canvas.create_text(
    16.0,
    145.0,
    anchor="nw",
    text="DayScholar",
    fill="#000000",
    font=("Inter Bold", 16 * -1, "bold")
)

status = canvas.create_text(
    16.0,
    215.0,
    anchor="nw",
    text="Suspended / Leave approved",
    fill="#E31138",
    font=("Inter Bold", 16 * -1, "bold")
)

battery = canvas.create_text(
    160.0,
    16.0,
    anchor="nw",
    text="        58% ",
    fill="#000000",
    font=("Inter Bold", 16 * -1, "bold")
)

canvas.create_text(
    16.0,
    16.0,
    anchor="nw",
    text="D-1     IN GATE ",
    fill="#000000",
    font=("Inter Bold", 20 * -1, "bold")
)

canvas.create_rectangle(
    15.0,
    48.0,
    253.00000113248734,
    49.0,
    fill="#000000",
    outline="")

image_label = Label(window)
image_label.place(x=260, y=9)
current_index = 0


def update_display():

    global current_index

    # Get the current data entry
    current_data = data[current_index]

    # Update the displayed information
    canvas.itemconfigure(name_text, text=current_data["NAME"])
    canvas.itemconfigure(id_text, text=current_data["HTNO"])
    # canvas.itemconfigure(blood_group_text, text=current_data["BLOOD GROUP"])
    canvas.itemconfigure(school_text, text=current_data["SCHOOL"])

    # Get the image URL from the current data entry and update the displayed image
    img_url = current_data["IMG"]
    print(img_url)
    img = get_image_from_url(img_url, 200, 277)
    print(img)
    current_image = img

    image_label.configure(image=current_image)
    image_label.image = current_image
    # Increment the index for the next update
    current_index = (current_index + 1) % len(data)

    # Schedule the next update after 3000 milliseconds (3 seconds)
    window.after(3000, update_display)


update_display()

window.resizable(False, False)


window.mainloop()
