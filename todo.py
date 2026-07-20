
tasks = []


while True:

    print("\n===== TO DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":

        task = input("Enter Task: ")
        tasks.append(task)
        print("Task Added Successfully!")

    elif choice == "2":

        if len(tasks) == 0:
            print("No Tasks Available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":

        if len(tasks) == 0:
            print("No Tasks Available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = int(input("Enter task number to update: "))

            if 1 <= num <= len(tasks):
                new_task = input("Enter New Task: ")
                tasks[num - 1] = new_task
                print("Task Updated Successfully!")
            else:
                print("Invalid Task Number")

    elif choice == "4":

        if len(tasks) == 0:
            print("No Tasks Available")
        else:
            print("\nYour Tasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            num = int(input("Enter task number to delete: "))

            if 1 <= num <= len(tasks):
                tasks.pop(num - 1)
                print("Task Deleted Successfully!")
            else:
                print("Invalid Task Number")

    elif choice == "5":

        print("Thank You!")
        break

    else:

        print("Invalid Choice")