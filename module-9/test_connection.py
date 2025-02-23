"""
Module 9.2 - API Connection Test
Julio Pochet
02/23/2025

Purpose:
This script tests API connectivity by making a simple GET request to Google.
"""

import requests

# Test connection to Google
response = requests.get("http://www.google.com")
print(f"Google API Response Code: {response.status_code}")