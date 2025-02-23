# ------------------------------------------------
# Julio Pochet
# 02/23/2025
# Assignment: Module 8.2 – JSON Practice
# Purpose: Reads student data from JSON, updates it, and saves changes.
# ------------------------------------------------

import json
import os

# Define the JSON file path
json_file = os.path.join(os.path.dirname(__file__), "student.json")

class Student:
    """Represents a student with first name, last name, ID, and email."""
    
    def __init__(self, first_name, last_name, student_id, email):
        self.first_name = first_name
        self.last_name = last_name
        self.student_id = student_id
        self.email = email

    def __str__(self):
        """Returns a formatted string representation of the student."""
        return f"{self.last_name}, {self.first_name} : ID = {self.student_id} , Email = {self.email}"

class StudentManager:
    """Manages student records, including loading, displaying, and saving them."""

    def __init__(self, json_path):
        self.json_path = json_path
        self.students = self.load_students()  # Load students from JSON file

    def load_students(self):
        """Loads student data from the JSON file into a list of Student objects."""
        try:
            with open(self.json_path, "r") as file:
                data = json.load(file)  # Convert JSON into a list of dictionaries
                return [Student(d["F_Name"], d["L_Name"], d["Student_ID"], d["Email"]) for d in data]
        except (FileNotFoundError, json.JSONDecodeError):
            print("\nError: Could not load student data. Ensure 'student.json' exists and has valid JSON format.")
            return []

    def print_students(self, message):
        """Prints all students in a formatted list."""
        print(f"\n{message}\n")
        for student in self.students:
            print(student)

    def add_student(self, first_name, last_name, student_id, email):
        """Adds a new student to the list."""
        new_student = Student(first_name, last_name, student_id, email)
        self.students.append(new_student)

    def save_students(self):
        """Writes the updated student list back to the JSON file."""
        with open(self.json_path, "w") as file:
            json.dump([vars(student) for student in self.students], file, indent=4)
        print("\nThe student.json file has been updated successfully!")

# Create an instance of StudentManager
manager = StudentManager(json_file)

# Output notification and print original student list
print("\nOriginal Student List:")
manager.print_students("Displaying current student records...")

# Add a new student record
manager.add_student("Julio", "Pochet", 99999, "jpochet@gmail.com")

# Output notification and print updated student list
print("\nUpdated Student List:")
manager.print_students("Displaying updated student records...")

# Save the updated student list back to the JSON file
manager.save_students()