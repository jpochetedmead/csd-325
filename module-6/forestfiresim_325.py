""" 
Forest Fire Simulation - CSD 325 
Julio Pochet Edmead
Date: 02/08/2025
Assignment: Module 6.2 - Forest Fire Simulation
Description: 
    This program simulates the spread of a wildfire in a forest. 
    A new feature, a lake ('~'), has been added. The lake starts 
    from the bottom center and extends to the middle of the grid.
    Fire cannot spread across water, acting as a natural firebreak.
    The simulation updates over time, showing how fire behaves in 
    different conditions. 
"""

import random
import sys
import time

try:
    import bext  # Used for colored text output
except ImportError:
    print('This program requires the bext module.')
    print('Install it using: pip install bext')
    sys.exit()

# Simulation grid dimensions
WIDTH = 79
HEIGHT = 22

# Symbols representing different elements in the simulation
TREE = 'A'
FIRE = '@'
EMPTY = ' '
WATER = '~'  # Lake acts as a fire barrier

# Fire simulation settings
TREE_GROWTH_PROB = 0.01  # Probability of a new tree growing
LIGHTNING_STRIKE_PROB = 0.01  # Probability of a tree catching fire

# Simulation speed
SIM_SPEED = 0.5  # Seconds per step


def main():
    """Runs the simulation loop, updating and displaying the forest at each step."""
    forest = create_forest()  # Generate initial forest grid
    bext.clear()

    while True:
        display_forest(forest)  # Show the current state of the forest

        # Prepare next simulation step
        next_forest = {'width': forest['width'], 'height': forest['height']}

        for x in range(forest['width']):
            for y in range(forest['height']):
                if (x, y) in next_forest:
                    continue  # Skip if already processed

                if forest[(x, y)] == WATER:
                    next_forest[(x, y)] = WATER  # Water remains unchanged

                elif forest[(x, y)] == EMPTY and random.random() <= TREE_GROWTH_PROB:
                    next_forest[(x, y)] = TREE  # Trees grow in empty spaces

                elif forest[(x, y)] == TREE and random.random() <= LIGHTNING_STRIKE_PROB:
                    next_forest[(x, y)] = FIRE  # Lightning strikes, setting tree on fire

                elif forest[(x, y)] == FIRE:
                    # Fire spreads to neighboring trees but does NOT burn water
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            neighbor = (x + dx, y + dy)
                            if forest.get(neighbor) == TREE and forest.get(neighbor) != WATER:
                                next_forest[neighbor] = FIRE
                    next_forest[(x, y)] = EMPTY  # Tree burns down

                else:
                    next_forest[(x, y)] = forest[(x, y)]  # Keep existing elements

        forest = next_forest  # Update the forest state
        time.sleep(SIM_SPEED)  # Pause before next update


def create_forest():
    """
    Generates a new forest grid with trees, empty spaces, and a lake.
    The lake starts at the bottom center and extends upward to the middle.
    
    Returns:
        dict: A dictionary representing the forest grid.
    """
    forest = {'width': WIDTH, 'height': HEIGHT}

    # Define lake position and size
    center_x = WIDTH // 2  # Middle of the width
    lake_width = 10  # Width of the lake
    lake_height = HEIGHT // 2  # Extends from the bottom to the middle

    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Create a lake from bottom center up to the middle
            if (center_x - lake_width // 2 <= x <= center_x + lake_width // 2 and
                    HEIGHT // 2 <= y <= HEIGHT):
                forest[(x, y)] = WATER  # Place water
            elif random.random() < 0.20:  # 20% chance of placing a tree
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY  # Empty ground

    return forest


def display_forest(forest):
    """
    Prints the forest grid to the terminal with color coding.
    Trees (green), Fire (red), and Water (blue) are visually represented.
    
    Args:
        forest (dict): The dictionary representing the forest grid.
    """
    bext.goto(0, 0)  # Reset cursor to top-left before printing
    for y in range(forest['height']):
        for x in range(forest['width']):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == WATER:
                bext.fg('blue')
                print(WATER, end='')
            else:
                print(EMPTY, end='')
        print()  # Move to the next row

    bext.fg('reset')  # Reset text color
    print('Tree Growth: {}%  '.format(TREE_GROWTH_PROB * 100), end='')
    print('Lightning Strike: {}%  '.format(LIGHTNING_STRIKE_PROB * 100), end='')
    print('Press Ctrl-C to exit.')


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()  # Exit when Ctrl-C is pressed
