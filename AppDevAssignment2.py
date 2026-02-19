# Program Name: Assignment2.py
# Course: IT3883/Section 12893
# Student Name: Motunrayo Iruedo
# Assignment Number: Assignment 2
# Due Date:02/18/2026
# Purpose: This program reads student grade data from a file,
# calculates each student’s final average, and prints the
# results in descending order by average.
# Resources Used: Class notes,Youtube and  practice.

# Create an empty list to store student names and averages
student_results = []

# Open the input file for reading
with open("Assignment2input.txt", "r") as file:


    # Loop through each line in the file
    for line in file:

        # Remove leading/trailing spaces and newline characters
        line = line.strip()

        # Split the line into individual parts
        parts = line.split()

        # The first item in the list is the student's name
        name = parts[0]

        # The remaining items are the student's scores
        scores = parts[1:]

        # Convert each score from string to integer
        scores = [int(score) for score in scores]

        # Calculate the average by dividing the sum by number of scores
        average = sum(scores) / len(scores)

        # Store the name and average together as a tuple
        student_results.append((name, average))

# Sort students by average in descending order (highest first)
student_results.sort(key=lambda x: x[1], reverse=True)

# Print each student’s name and average formatted to 2 decimal places
for student in student_results:
    print(student[0], format(student[1], ".2f"))
