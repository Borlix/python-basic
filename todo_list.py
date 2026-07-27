# 7th python program - simple to-do list!

tasks = []  # empty list to store tasks

while True:
    # show the menu every time
    print("\n=== TO-DO LIST ===")
    print("1. Add task")
    print("2. List tasks")
    print("3. Complete task")
    print("4. Delete task")
    print("5. Quit")

    choice = input("Choose (1-5): ")

    if choice == "1":
        # add a new task to the list
        task = input("Enter task: ").strip()
        if task:
            tasks.append(task)
            print("Task added!")
        else:
            print("Task cannot be empty.")

    elif choice == "2":
        # show all tasks with numbers
        if not tasks:
            print("No tasks yet. Add one with option 1.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

    elif choice == "3":
        # mark a task as done
        if not tasks:
            print("No tasks yet. Add one with option 1.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            task_number = input("Enter task number to complete: ")

            if not task_number.isdigit():
                print("Please enter a valid number.")
            else:
                index = int(task_number) - 1

                if index < 0 or index >= len(tasks):
                    print("That task number does not exist.")
                elif " [DONE]" in tasks[index]:
                    print("That task is already done.")
                else:
                    tasks[index] += " [DONE]"
                    print("Task marked as done!")

    elif choice == "4":
        # remove a task from the list
        if not tasks:
            print("No tasks yet. Add one with option 1.")
        else:
            for number, task in enumerate(tasks, start=1):
                print(f"{number}. {task}")

            task_number = input("Enter task number to delete: ")

            if not task_number.isdigit():
                print("Please enter a valid number.")
            else:
                index = int(task_number) - 1

                if index < 0 or index >= len(tasks):
                    print("That task number does not exist.")
                else:
                    removed = tasks.pop(index)
                    print(f"Deleted: {removed}")

    elif choice == "5":
        print("Goodbye!")
        break

    else:
        print("Invalid choice. Try again.")
