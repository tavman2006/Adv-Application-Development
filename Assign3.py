# Program Name: Assignment3.py
# Course: IT3883/Section W01
# Student Name: Tavion Manior
# Assignment Number: Assignment 1
# Due Date: 10/10/2026
# Purpose: This program creates a GUI that converts miles per gallon (MPG)
# to kilometers per liter (km/L). The result updates as the user types.
# Resources Used: Assignment 3 instructions, Python Tkinter documentation

import tkinter as tk

# Conversion factor provided in the assignment.
MPG_TO_KM_PER_LITER = 0.425143707


def update_conversion(*args):
    # Read the value currently typed into the input box.
    entered_value = mpg_value.get().strip()

    # Do not show a result when the input is blank.
    if entered_value == "":
        result_value.set("")
        status_value.set("Enter a number of miles per gallon.")
        return

    # Handle letters or other invalid input without crashing.
    try:
        mpg = float(entered_value)
    except ValueError:
        result_value.set("")
        status_value.set("Please enter a valid number.")
        return

    # Convert the number and show the result to four decimal places.
    km_per_liter = mpg * MPG_TO_KM_PER_LITER
    result_value.set(f"{km_per_liter:.4f}")
    status_value.set("")


# Create and configure the application window.
window = tk.Tk()
window.title("MPG to km/L Converter")
window.geometry("360x220")
window.resizable(False, False)

# StringVar lets the program respond whenever the input changes.
mpg_value = tk.StringVar()
result_value = tk.StringVar()
status_value = tk.StringVar()

# Add the title and input field.
title_label = tk.Label(
    window,
    text="Miles per Gallon to Kilometers per Liter",
    font=("Arial", 12, "bold"),
    wraplength=330
)
title_label.pack(pady=(15, 12))

input_label = tk.Label(window, text="Miles per gallon (MPG):")
input_label.pack()

mpg_entry = tk.Entry(window, textvariable=mpg_value, width=22)
mpg_entry.pack(pady=5)

# Recalculate automatically every time the input text changes.
mpg_value.trace_add("write", update_conversion)

# Display the converted result.
result_label = tk.Label(window, text="Kilometers per liter (km/L):")
result_label.pack(pady=(8, 0))

result_display = tk.Label(
    window,
    textvariable=result_value,
    font=("Arial", 12, "bold"),
    width=18
)
result_display.pack(pady=4)

# Display a message for blank or invalid input.
status_label = tk.Label(
    window,
    textvariable=status_value,
    fg="red",
    wraplength=330
)
status_label.pack()

# Focus on the input box and run the GUI.
mpg_entry.focus_set()
window.mainloop()
