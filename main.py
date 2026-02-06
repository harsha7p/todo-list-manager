tasks = []

def show_menu():
    print("\n--- TO-DO LIST MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added successfully!")

    elif choice == '2':
        if not tasks:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == '3':
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
