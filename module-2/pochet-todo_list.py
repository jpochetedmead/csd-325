def display_tasks(tasks):
    """
    Displays the current list of tasks.
    If no tasks are available, it informs the user.
    """
    if not tasks:
        print("\nYour to-do list is empty!")
    else:
        print("\nYour To-Do List:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")

def main():
    """
    Main function that runs the to-do list program.
    Users can add, view, and remove tasks.
    """
    tasks = []  # List to store tasks

    while True:
        # Display menu options
        print("\n=== SIMPLE TO-DO LIST ===")
        print("1. Add a Task")
        print("2. View Tasks")
        print("3. Remove a Task")
        print("4. Exit")

        # Get user choice
        choice = input("Choose an option (1-4): ").strip()

        # Check user input and perform action
        if choice == "1":
            task = input("Enter a new task: ").strip()
            if task:  # Ensure task is not empty
                tasks.append(task)
                print(f"✅ Task added: {task}")
            else:
                print("⚠️ Error: Task cannot be empty!")

        elif choice == "2":
            display_tasks(tasks)  # Call function to display tasks

        elif choice == "3":
            display_tasks(tasks)
            if tasks:  # Ensure there are tasks to remove
                try:
                    task_number = int(input("Enter task number to remove: "))
                    if 1 <= task_number <= len(tasks):
                        removed_task = tasks.pop(task_number - 1)
                        print(f" Removed task: {removed_task}")
                    else:
                        print("⚠️ Error: Invalid task number.")
                except ValueError:
                    print("⚠️ Error: Please enter a valid number.")
            else:
                print("⚠️ No tasks to remove!")

        elif choice == "4":
            print("✅ Exiting To-Do List. Goodbye!")
            break  # Exit the loop and end the program

        else:
            print("⚠️ Error: Please choose a valid option (1-4).")

# Run the program
if __name__ == "__main__":
    main()
