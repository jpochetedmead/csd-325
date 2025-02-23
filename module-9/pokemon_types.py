"""
Module 9.2 - Listing Pokémon Types, Strengths, and Weaknesses
Julio Pochet
02/23/2025

Purpose:
This script fetches all Pokémon types from the PokéAPI, including their
strengths (double damage to) and weaknesses (double damage from).

Sources:
- API: https://pokeapi.co/api/v2/type/
"""

import requests
import json

def fetch_pokemon_types():
    """Fetch and display all Pokémon types along with their strengths and weaknesses."""
    url = "https://pokeapi.co/api/v2/type/"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        print("\n🔹 Fetching Pokémon Types...")

        for type_info in data["results"]:
            type_name = type_info["name"]
            type_url = type_info["url"]
            display_type_details(type_name, type_url)

    else:
        print(f"Failed to retrieve Pokémon types. Status Code: {response.status_code}")

def display_type_details(type_name, type_url):
    """Fetch and display strengths and weaknesses of a specific Pokémon type."""
    response = requests.get(type_url)
    if response.status_code == 200:
        type_data = response.json()

        strengths = [t["name"] for t in type_data["damage_relations"]["double_damage_to"]]
        weaknesses = [t["name"] for t in type_data["damage_relations"]["double_damage_from"]]

        print(f"\n✨ Type: {type_name.capitalize()}")
        print(f"   🟢 Strong Against: {', '.join(strengths) if strengths else 'None'}")
        print(f"   🔴 Weak Against: {', '.join(weaknesses) if weaknesses else 'None'}")
    else:
        print(f"Could not fetch details for type: {type_name}")

# Run the program
if __name__ == "__main__":
    fetch_pokemon_types()