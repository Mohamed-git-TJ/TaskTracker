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
    status = "todo"
    
    # Task Structure
    task = {
        "id": taskId,
        "description": taskDescription,
        "status": status,
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
        "status": i.get("status"),
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
    
    print("-"*114)
    
    for colum in header:
        print(fixed_length(colum, 20), end = " | ")
    print()
    print("-"*114)
    
    task = []
    for row in file_data["tasks"]:
                  
        task.append(row.get("id"))
        task.append(row.get("description"))
        task.append(row.get("status"))
        task.append(row.get("createdAt"))
        task.append(row.get("updatedAt"))
        
    
        for colum in task:
            
            print(fixed_length(colum, 20), end = " | ")
        print()
        print("-"*114)
        task.clear()
   
    
        
        
def option_5(filename='data.json'):
    with open(filename, 'r+') as file:
        file_data = json.load(file)
        
    
    taskId = input("Type the ID of the task you would like to mark down" + "\n")
    
    # Removing 'task' from list
    for i in file_data["tasks"]:
        if taskId == i.get("id"):
            file_data["tasks"].remove(i)
            # Write the updated data back to the file
            with open(filename, 'w') as file:
                json.dump(file_data, file, indent=4)
            
    status = ""
    while True:
        statusChoice = input("Would you like to mark the task as 'in-progress' or 'done' \n Type 1 or 2: ")
        
        if statusChoice == "1":
            status = "in-progress"
            break
        elif statusChoice == "2":
            status = "done"    
            break
        else:
            print("Invalid choice. Please try again.")

    # Task Structure
    task = {
        "id": taskId,
        "description": i.get("description"),
        "status": status,
        "createdAt": i.get("createdAt"),
        "updatedAt": i.get("updatedAt")
    } 
    # Calling function to append data
    write_json(task)
     
    



def main_menu():
    print("What do you want to do!")
    

    while True:
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Update a task")
        print("4. Tasks List")
        print("5. Tasks status")
        print("0. Exit")
        choice = input("Enter your choice (0-5): ")

        if choice == "1":
            option_1()
        elif choice == "2":
            option_2()
        elif choice == "3":
            option_3()
        elif choice == "4":
            option_4()
        elif choice == "5":
            option_5()
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
