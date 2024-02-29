import tkinter as tk
import requests
from Main_screen2.build.gui import first_window
from second_screen import id_screen
# Function to simulate reading from the RFID reader
from PIL import Image, ImageTk
from io import BytesIO
import time
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / \
    Path(r"/Users/visveshnaraharisetty/Desktop/build/assets/frame0/")


def read_rfid():
    # Placeholder function, replace with actual code to read RFID reader output
    # For demonstration, return a sample RFID value
    return "c912317c"

# Function to handle RFID reader output and trigger API call


image_path = "/Users/visveshnaraharisetty/Desktop/build/assets/frame0/"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


def get_image_from_url(url, target_width, target_height):
    response = requests.get(url)
    print(response)
    img = Image.open(BytesIO(response.content))
    img = img.resize((target_width, target_height))

    # print("helo")
    return ImageTk.PhotoImage(img)


def handle_rfid_output():
    # Read from the RFID reader
    rfid_value = read_rfid()
    print(rfid_value)
    # Check if RFID value is received
    if rfid_value:
        # Call the API with the RFID value
        fetch_data_and_show_second_window(rfid_value)

# Function to make the API call and show the second window


def fetch_data_and_show_second_window(rfid_value):
    try:

        # Make the API call with the RFID value
        response = requests.get(
            f"https://api-dot-mahindrauni2.el.r.appspot.com/outpass/gateinout/1/{rfid_value}")

        if response.status_code == 200:
            # If API call is successful, show the second window
            show_second_window(response.json())
        else:
            print("Failed to fetch data from the API")

    except Exception as e:
        print("Error fetching data:", e)

        first_window.after(10000, handle_rfid_output)
        print("hello")

# Function to show the second window


def show_second_window(data):
    # second_window = tk.Toplevel()
   # Create the second window
    print(data["HTNO"])
    # id_screen(first_window, data, image_path)

    window = tk.Toplevel(first_window)
    window.overrideredirect(True)
    window.geometry("480x320")
    window.configure(bg="#FFFFFF")
    window.attributes('-alpha',)

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
        file=image_path + "image_1.png")
    image_1 = canvas.create_image(
        240.0,
        160.0,
        image=image_image_1
    )

    image_image_2 = PhotoImage(
        file=image_path + "image_2.png")
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

    # image_image_6 = PhotoImage(
    #     file=relative_to_assets("image_6.png"))
    # image_6 = canvas.create_image(
    #     241.0,
    #     25.0,
    #     image=image_image_6
    # )

    name_text = canvas.create_text(
        16.0,
        57.0,
        anchor="nw",
        text=data["NAME"],
        fill="#000000",
        font=("Inter Bold", 16 * -1, "bold")
    )

    id_text = canvas.create_text(
        16.0,
        115.0,
        anchor="nw",
        text=data["HTNO"],
        fill="#000000",
        font=("Inter Bold", 16 * -1, "bold")
    )

    school_text = canvas.create_text(
        16.0,
        174.0,
        anchor="nw",
        text=data["SCHOOL"],
        fill="#000000",
        font=("Inter Bold", 16 * -1,  'bold')
    )

    a_type = canvas.create_text(
        16.0,
        145.0,
        anchor="nw",
        text=data["A_TYPE"],
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

    # battery = canvas.create_text(
    #     160.0,
    #     16.0,
    #     anchor="nw",
    #     text="        58% ",
    #     fill="#000000",
    #     font=("Inter Bold", 16 * -1, "bold")
    # )

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

    photo = get_image_from_url(
        "https://musecportal.s3.ap-south-1.amazonaws.com/2021/" + data["HTNO"].lower() + ".jpg", 200, 277)
    print(photo)
    current_image = photo
    image_label.configure(image=current_image)
    image_label.image = current_image
    print("before")

    def close_second_window():
        window.destroy()
        first_window.after(5000, lambda: show_second_window(data))

    # Schedule the close function to run after 5000 milliseconds (5 seconds)
    window.after(5000, close_second_window)

    window.mainloop()
    # window.mainloop()
    print("After loop")
    # return window


def close_window_and_show_first(window):
    # Close the provided window
    window.destroy()
    # Show the first window again
    first_window.after(10000, handle_rfid_output)


# Start a loop to continuously handle RFID reader output
# You might need to adjust the frequency based on your requirements
first_window.after(10000, handle_rfid_output)

# Start the Tkinter event loop for the first window
first_window.mainloop()
