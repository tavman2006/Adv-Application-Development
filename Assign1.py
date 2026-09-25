# Program Name: Assignment1.py
# Course: IT3883/Section XXX
# Student Name: YOUR NAME
# Assignment Number: Assignment 1
# Due Date: XX/XX/2026
# Purpose: This program allows the user to add, clear, and display
#          text stored in an input buffer.
# Resources Used: Python documentation and instructor assignment instructions.

# Create an empty input buffer
input_buffer = ""

# Keep showing the menu until the user chooses option 4
while True:
    print("\n1. Append data to the input buffer")
    print("2. Clear the input buffer")
    print("3. Display the input buffer")
    print("4. Exit the program")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Ask the user for text and add it to the existing buffer
        data = input("Enter a string: ")
        input_buffer = input_buffer + data

    elif choice == "2":
        # Remove everything currently stored in the buffer
        input_buffer = ""
        print("Input buffer cleared.")

    elif choice == "3":
        # Show the current contents of the buffer
        print("Input buffer:", input_buffer)

    elif choice == "4":
        # End the program
        print("Program ending.")
        break

    else:
        # Tell the user when they enter something other than 1-4
        print("Invalid choice. Please enter 1, 2, 3, or 4.")