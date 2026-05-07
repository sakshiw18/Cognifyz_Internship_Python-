tasks = []

def show_tasks():
    if not tasks:
        print("No tasks available ✅")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("Task added successfully!")

def delete_task():
    show_tasks()
    try:
        task_no = int(input("Enter task number to delete: "))
        removed = tasks.pop(task_no - 1)
        print(f"Deleted task: {removed}")
    except:
        print("Invalid input!")

def mark_completed():
    show_tasks()
    try:
        task_no = int(input("Enter task number to mark complete: "))
        tasks[task_no - 1] += " ✔"
        print("Task marked as completed!")
    except:
        print("Invalid input!")

def main():
    while True:
        print("\n--- TO-DO LIST MENU ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_tasks()
        elif choice == '2':
            add_task()
        elif choice == '3':
            delete_task()
        elif choice == '4':
            mark_completed()
        elif choice == '5':
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice!")

# Run program
main()