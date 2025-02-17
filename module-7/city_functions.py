# --------------------------------------------------
# Julio Pochet Edmead
# 02/16/2025
# Assignment: Module 7.2 - City Functions
# Purpose: Defines a function that formats city, country, population, 
# and language. Calls the function with different cases.
# --------------------------------------------------

def city_country(city, country, population=None, language=None):
    """
    Returns a formatted string in the form 'City, Country'.
    Optionally includes population and language if provided.
    """
    result = f"{city.title()}, {country.title()}"
    
    if population:
        result += f" - Population: {population}"
    
    if language:
        result += f", {language.title()}"
    
    return result


# Calling the function with different test cases
if __name__ == "__main__":
    # City, Country
    print(city_country("Santiago", "Chile"))

    # City, Country, Population
    print(city_country("New York", "USA", 8419600))

    # City, Country, Population, Language
    print(city_country("Tokyo", "Japan", 13929286, "Japanese"))
