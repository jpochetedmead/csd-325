# Julio Pochet Edmead
# Date: 01/26/2025
# Assignment: Module 4.2 - High/Low Temperatures
# Purpose: Reads temperature data from a CSV file and allows users to choose 
#          between viewing high or low temperatures using Matplotlib.

import csv
from datetime import datetime
import matplotlib.pyplot as plt
import sys

# Define the CSV filename
filename = "sitka_weather_2018_simple.csv"

# Lists to store extracted data
dates, highs, lows = [], [], []

try:
    # Open and read the CSV file
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        header_row = next(reader)  # Read the header row

        # Identify column indexes dynamically
        try:
            date_index = header_row.index("DATE")
            high_index = header_row.index("TMAX")
            low_index = header_row.index("TMIN")
        except ValueError:
            print("Error: Required columns not found in the CSV file.")
            sys.exit()

        # Read and process each row of data
        for row in reader:
            try:
                current_date = datetime.strptime(row[date_index], "%Y-%m-%d")
                high = int(row[high_index])  # Convert temperature to integer
                low = int(row[low_index])

                dates.append(current_date)
                highs.append(high)
                lows.append(low)

            except ValueError:
                print(f"Warning: Missing or invalid data for {row[date_index]}")

except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
    sys.exit()

# Function to plot temperatures
def plot_temperatures(dates, temperatures, title, color):
    """
    Plots temperatures using Matplotlib.
    
    :param dates: List of datetime objects.
    :param temperatures: List of temperature values.
    :param title: Title of the graph.
    :param color: Color of the graph line.
    """
    plt.figure(figsize=(12, 6))
    plt.plot(dates, temperatures, color=color, label=title, linewidth=1.5)

    plt.title(title, fontsize=14)
    plt.xlabel("Date", fontsize=12)
    plt.ylabel("Temperature (°F)", fontsize=12)
    plt.xticks(rotation=45)
    plt.legend()
    plt.grid()

    plt.show()

# Function to display the menu and handle user choices
def main_menu():
    """
    Displays the menu and processes user input to show temperature graphs or exit.
    """
    while True:
        print("\n📊 **Sitka Weather Data Viewer (2018)** 📊")
        print("1️⃣ View High Temperatures (Red Graph)")
        print("2️⃣ View Low Temperatures (Blue Graph)")
        print("3️⃣ Exit Program")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            plot_temperatures(dates, highs, "Daily High Temperatures - Sitka, AK (2018)", "red")
        elif choice == "2":
            plot_temperatures(dates, lows, "Daily Low Temperatures - Sitka, AK (2018)", "blue")
        elif choice == "3":
            print("\n✅ Exiting the program. Have a great day! 🌤️")
            sys.exit()
        else:
            print("\n⚠️ Invalid choice. Please enter 1, 2, or 3.")

# Run the menu system
if __name__ == "__main__":
    main_menu()