# --------------------------------------------------
# Julio Pochet Edmead
# 02/16/2025
# Assignment: Module 7.2 - Test Cases
# Purpose: This script tests the city_country function on the city_functions file using the unittest framework.
# --------------------------------------------------

import unittest
from city_functions import city_country  # Importing the function from city_functions.py

class TestCityCountry(unittest.TestCase):
    """Unit test for the city_country function."""

    def test_city_country(self):
        """Test if city_country() correctly formats 'City, Country'."""
        formatted_name = city_country("santiago", "chile")
        self.assertEqual(formatted_name, "Santiago, Chile")

if __name__ == '__main__':
    unittest.main()