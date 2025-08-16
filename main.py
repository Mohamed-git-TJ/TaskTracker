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
    
    # Loading data
    with open(filename, 'r+') as file:
        file_data = json.load(file)

    print("ADD A TASK")

    # Getting User Input
    loop = True
    ids = []
    while loop:
        taskId = input("What ID do you want to give to this task:" + "\n")
        for i in file_data["tasks"]:
            ids.append(i.get("id"))
        if taskId in ids:
            print("That already exists")
        else:
            loop = False
                
                
    taskDescription = input("What is the task about:" + "\n")

    # Task Structure
    task = {
        "id": taskId,
        "description": taskDescription,
        "status": "todo",
        "createdAt": str(date.strftime("%d/%b/%Y %H:%M")),
        "updatedAt": "dateUpdatedAt"
    }
    
    # Calling function to append data
    write_json(task)
    


# Delete task from JSON file (Option 2)
def option_2(filename='data.json'):
    print("DELETE A TASK")
    
    # Getting User Input and using it as id of the task
    taskId = input("Type the ID of the task you would like to delete" + "\n")

    # Loading data
    with open(filename, 'r+') as file:
        file_data = json.load(file)

        # Removing 'task' from list
        for i in file_data["tasks"]:
            if taskId == i.get("id"):
                file_data["tasks"].remove(i)

            

        # Write the updated data back to the file
        with open(filename, 'w') as file:
            json.dump(file_data, file, indent=4)

    print("Task deleted succesfully")


def option_3(filename='data.json'):
    print("UPDATE TASK")
    date = datetime.datetime.now()
    # Loading data
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        
    taskId = input("Type the ID of the task you would like to edit/update" + "\n")

    # Removing 'task' from list
    for i in file_data["tasks"]:
        if taskId == i.get("id"):
            file_data["tasks"].remove(i)
            # Write the updated data back to the file
            with open(filename, 'w') as file:
                json.dump(file_data, file, indent=4)
            taskDescription = input("Set the new description:" + "\n")
    
    # Task Structure
    task = {
        "id": taskId,
        "description": taskDescription,
        "status": "todo",
        "createdAt": i.get("createdAt"),
        "updatedAt": str(date.strftime("%d/%b/%Y %H:%M"))
    }
    # Calling function to append data
    write_json(task)
            
            
            
    
            
           
            

def option_4(filename='data.json'):
    
    with open(filename, 'r+') as file:
        file_data = json.load(file)
    
    header = ["ID", "DESCRIPTION", "STATUS", "DATE OF CREATION", "DATE OF UPDATE"]

    def fixed_length(text, length):
        if len(text) > length:
            text = text[:length]
        elif len(text) < length:
            text = (text + " " * length)[:length]
        return text
    
    print("-"*117)
    print("| ", end=" ")
    for colum in header:
        print(fixed_length(colum, 20), end = " | ")
    print()
    print("-"*117)
    
    task = []
    for row in file_data["tasks"]:
        print("| ", end=" ")            
        task.append(row.get("id"))
        task.append(row.get("description"))
        task.append(row.get("status"))
        task.append(row.get("createdAt"))
        task.append(row.get("updatedAt"))
        
        for colum in task:
            print(fixed_length(colum, 20), end = " | ")
        print()
        print("-"*117)
        task.clear()
        
        




def main_menu():
    print("What do you want to do!")
    print("1. Add a task")
    print("2. Delete a task")
    print("3. Update a task")
    print("4. Tasks List")
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
