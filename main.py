# This is my task-tracker project
import json
import os
import datetime


# Function to append new data to JSON file
def write_json(new_data, filename='data.json'):
    with open(filename, 'r+') as file:
        # Load existing data into a dictionary
        file_data = json.load(file)

        # Append new data to the 'emp_details' list
        file_data["emp_details"].append(new_data)

        # Move the cursor to the beginning of the file
        file.seek(0)

        # Write the updated data back to the file
        json.dump(file_data, file, indent=4)


# SIMPLE MENU
def option_1(filename='data.json'):
    print("ADD A TASK")
    taskDescription = input("What is the task about:" + "\n")

    with open(filename, 'r+') as file:
        file_data = json.load(file)

    date = datetime.datetime.now()

    employee = {
        "id": len(file_data["emp_details"]) + 1,
        "description": taskDescription,
        "status": "todo",
        "createdAt": str(date.strftime("%d%b%Y")),
        "updatedAt": "dateUpdatedAt"
    }

    write_json(employee)


def option_2(filename='data.json'):
    print("DELETE A TASK")

    taskId = int(
        input("Type the ID of the task you would like to delete" + "\n"))

    with open(filename, 'r+') as file:
        file_data = json.load(file)

        file_data["emp_details"].pop(taskId - 1)
        with open(filename, 'w') as file:
            json.dump(file_data, file, indent=4)


def option_3():
    print("You selected Option 3.")
    # Add your command logic here for Option 3


def option_4():
    print("You selected Option 4.")
    # Add your command logic here for Option 4


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


# Call the function to append data
if os.path.isfile('data.json'):
    main_menu()
else:
    data = {"emp_details": []}
    try:
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)

        print(f"JSON file '{'data.json'}' has been created successfully")
    except FileExistsError:
        print("That file already exists!")
