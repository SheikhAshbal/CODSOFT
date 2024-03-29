import json

def add_task(tasks, status="Incomplete"):
    title = input("Enter task title: ").capitalize()
    description = input("Enter task description: ").capitalize()
    task = {"title": title, "description": description, "status": status}
    tasks.append(task)
    print("Task added successfully.")

def display_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.\n")
    else:
        print("\n-------- Your Tasks -------\n")
        for idx, task in enumerate(tasks, start=1):
            print(f"{idx}. {task['title']} - {task['description']} - {task['status']}\n")

def update_task_status(tasks):
    display_tasks(tasks)
    if not tasks:
        print("No tasks available to update.")
        return
    title = input("Enter the title of the task to mark as complete:").capitalize()
    task_found = False

    for task in tasks:
        if task["title"] == title:
            task["status"] = "Complete"
            print(f"Task '{title}' marked as complete.")
            task_found = True
            break
    if not task_found:
        print(f"Task '{title}' not found.")
    
def Update_tasks(tasks):
    display_tasks(tasks)
    if not tasks:
        print("No tasks to update.")
        return
    while True:
        try:
            index = int(input("Enter the index of the task to update: ")) - 1
            if 0 <= index < len(tasks):
                task = tasks[index]
                task["title"] = input(f"New Title ({task['title']}): ").capitalize()
                task["description"] = input(f"New Description ({task['description']}): ").capitalize()
                print("Task updated successfully!")
                break
            else:
                print("Invalid index. Please enter a valid index.")
        except ValueError:
            print("Invalid input. Please enter a valid index.")
        


def remove_completed_tasks(tasks):
    completed_tasks = []
    for task in tasks:
        if task["status"] == "Complete":
            completed_tasks.append(task)
    if not completed_tasks:
        print("\nNo completed tasks found.")
        return
    for completed_task in completed_tasks:
        tasks.remove(completed_task)
    save_to_file(tasks, filename)
    print("Completed tasks removed successfully.")

def save_to_file(tasks, filename):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def load_from_file(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            loaded_tasks = json.load(file)
            tasks.extend(loaded_tasks)
    except FileNotFoundError:
        pass  
    except json.JSONDecodeError:
        print("Error decoding JSON. File might be corrupted.")

    return tasks

def main():
    global filename,username
    username = input("Enter Your Name:").capitalize()
    filename= "tasks_Task_1 .json"
    tasks = load_from_file(filename)

    while True:
        print("""\n-----> Task Manager <-----\n
        1. Add Task
        2. Display Tasks
        3. Mark Task as Complete
        4. Remove Completed Tasks
        5. Update tasks
        6. Save and Quit""")

        while True:
            try:
                choice = int(input(f"\n{username} Please Choose one option given above!! Press(1-6) : "))
                if choice < 1 or choice > 6:
                    print("\nPlease enter a number between 1 and 6.")
                elif 1<=choice<=6:
                    break
            except:
                print("\nPlease enter a valid integer.")


        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            display_tasks(tasks)
        elif choice == 3:
            update_task_status(tasks)
        elif choice == 4:
            remove_completed_tasks(tasks)  
        elif choice==5:
            Update_tasks(tasks)
        elif choice == 6:
            save_to_file(tasks, filename)
            print("Tasks saved Successfully.\nExiting ......")
            break
        input("Press any key to continue..")

if __name__ == "__main__":
    print("\n-------------> To-Do List <----------------")
    main()
