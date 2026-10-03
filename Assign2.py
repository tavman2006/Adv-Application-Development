# Program Name: Assignment2.py
# Course: IT3883/Section W01
# Student Name: Tavion Manior
# Assignment Number: Assignment 2
# Due Date: 10/02/2026
# Purpose: This program reads student names and six scores from an input file.
# It calculates each student's final average and prints the students
# in descending order based on their average.
# Resources Used: Assignment 2 instructions and Assignment2input.txt

# Open the input file and read each line.
with open("Assignment2input.txt", "r") as input_file:
    students = []

    # Process each student's information.
    for line in input_file:
        parts = line.split()
        name = parts[0]

        # Convert the six scores from strings to numbers.
        scores = [float(score) for score in parts[1:]]

        # Calculate the student's average.
        average = sum(scores) / len(scores)

        # Store the name and average together.
        students.append((name, average))

# Sort students from the highest average to the lowest.
students.sort(key=lambda student: student[1], reverse=True)

# Print each student's name and average.
for name, average in students:
    print(f"{name} {average:.2f}")