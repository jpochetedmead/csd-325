"""
Module 9.2 - OpenNotify API: Current Astronauts
Julio Pochet
02/23/2025

Purpose:
This script fetches real-time astronaut data from the OpenNotify API
and displays it in both raw and formatted outputs.

Sources:
- API: http://api.open-notify.org/astros.json
- DataQuest API Tutorial (2024) (https://www.dataquest.io/blog/api-in-python/)
"""

import requests
import json

def fetch_data(url):
    """Fetch data from an API and handle errors."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad responses (4xx, 5xx)
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_astronauts():
    """Fetch and display astronaut data in raw and formatted output."""
    url = "http://api.open-notify.org/astros.json"
    data = fetch_data(url)

    if data:
        # 📌 Print raw JSON output
        print("\n🔹 Raw API Response:")
        print(json.dumps(data, indent=4))

        # 📌 Print formatted output
        print("\n🚀 Astronauts Currently in Space:")
        print(f"Total: {data['number']} astronauts\n")

        for astronaut in data["people"]:
            print(f"- {astronaut['name']} aboard {astronaut['craft']}")
    else:
        print("Could not retrieve astronaut data.")

# Run program
if __name__ == "__main__":
    display_astronauts()
