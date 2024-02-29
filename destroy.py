import tkinter as tk

# Create the main window
window = tk.Tk()

# Your GUI setup goes here...

# Define a function to destroy the window after 5 seconds


def destroy_window():
    window.destroy()


# Schedule the destruction of the window after 5 seconds
window.after(5000, destroy_window)

# Start the main event loop
window.mainloop()
