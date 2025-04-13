# A simple Task Manager application in Python
# Features: Add, view, complete, and delete tasks

# We will store tasks in a list, where each task is a dictionary
tasks = []

# Function to display the menu options
def show_menu():
    print("\n--- Task Manager ---")
    print("1. Add Task")                # Option to add a new task
    print("2. View Tasks")             # Option to display all tasks
    print("3. Mark Task as Completed") # Option to mark a task as completed
    print("4. Delete Task")            # Option to delete a task
    print("5. Exit")                   # Option to exit the program

# Function to add a new task
def add_task():
    task = input("Enter task description: ")  # Get task description from user
    # Add the task to the list with a default status of 'not completed'
    tasks.append({"description": task, "completed": False})
    print("Task added!")

# Function to view all tasks
def view_tasks():
    # If no tasks are present
    if not tasks:
        print("No tasks available.")
        return
    # Loop through each task and display it with a status icon
    for i, task in enumerate(tasks):
        # Use ✅ for completed and ❌ for not completed
        status = "✅" if task["completed"] else "❌"
        print(f"{i + 1}. {task['description']} [{status}]")

# Function to mark a task as completed
def mark_completed():
    view_tasks()  # Show current tasks first
    if tasks:
        try:
            # Ask user to enter the task number
            task_num = int(input("Enter task number to mark as completed: "))
            # Check if the number is within range
            if 1 <= task_num <= len(tasks):
                # Mark the task as completed
                tasks[task_num - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            # Handle non-integer input
            print("Please enter a valid number.")

# Function to delete a task
def delete_task():
    view_tasks()  # Show current tasks
    if tasks:
        try:
            # Ask user for task number to delete
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                # Remove the task from the list
                removed = tasks.pop(task_num - 1)
                print(f"Deleted task: {removed['description']}")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

# Main loop of the program
# This keeps running until the user chooses to exit
while True:
    show_menu()  # Show options to the user
    choice = input("Choose an option (1-5): ")  # Get user choice

    # Call the appropriate function based on user input
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_completed()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        print("Exiting Task Manager. Goodbye!")
        break  # Exit the loop and end the program
    else:
        print("Invalid choice. Try again.")  # Handle wrong input
