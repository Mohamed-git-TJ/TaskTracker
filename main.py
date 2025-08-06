import json
import os
import datetime

# TASK TRACKER CLI


# Append new data to JSON file
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # Load data
        file_data = json.load(file)

        # Append new data to the 'tasks' list
        file_data["tasks"].append(new_data)

        # Move the cursor to the beginning of the file
        file.seek(0)

        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)


# Add a task to JSON file (Option 1)
def option_1(filename='data.json'):
    # Current date
    date = datetime.datetime.now()

    print("ADD A TASK")

    # Getting User Input
    taskDescription = input("What is the task about:" + "\n")

    # Loading data
    with open(filename, 'r+') as file:
        file_data = json.load(file)

    # Task Structure
    task = {
        "id": len(file_data["tasks"]) + 1,
        "description": taskDescription,
        "status": "todo",
        "createdAt": str(date.strftime("%d%b%Y")),
        "updatedAt": "dateUpdatedAt"
    }

    # Calling function to append data
    write_json(task)


# Delete task from JSON file (Option 2)
def option_2(filename='data.json'):
    print("DELETE A TASK")

    # Getting User Input and using it as id of the task
    taskId = int(
        input("Type the ID of the task you would like to delete" + "\n"))

    # Loading data
    with open(filename, 'r+') as file:
        file_data = json.load(file)

        # Removing 'task' from list
        file_data["tasks"].pop(taskId - 1)

        # Write the updated data back to the file
        with open(filename, 'w') as file:
            json.dump(file_data, file, indent=4)

    print("Task deleted succesfully")


def option_3():
    print("You selected Option 3.")


def option_4():
    print("You selected Option 4.")


def main_menu():
    print("What do you want to do!")
    print("1. Add a task")
    print("2. Update a task")
    print("3. Delete a task")
    print("4. Option 4")
    print("0. Exit")

    while True:
        choice = input("Enter your choice (0-4): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if os.path.isfile('data.json'):
    main_menu()
else:
    data = {"tasks": []}
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        print(f"JSON file '{'data.json'}' has been created successfully")
    except FileExistsError:
        print("That file already exists!")
