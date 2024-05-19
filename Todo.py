class Task:
    def __init__(self, description):
        self.description = description

    def __str__(self):
        return self.description


class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        self.tasks.append(Task(description))

    def update_task(self, index, description):
        self.tasks[index].description = description

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)

    def display_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")


def main():
    todo_list = ToDoList()
    while True:
        print("\nTo-Do List Application")
        print("1. Add task")
        print("2. Update task")
        print("3. Delete task")
        print("4. Display tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            todo_list.add_task(description)
            print("TASK ADDED SUCCESSFULLY")
        elif choice == '2':
            index = int(input("Enter task number to update: ")) - 1
            try:
                if todo_list.tasks[index]:
                    description = input("Enter new description: ")
                    todo_list.update_task(index, description)
                    print("TASK UPDATED SUCCESSFULLY")
            except IndexError:
                print("Task not found.")
        elif choice == '3':
            index = int(input("Enter task number to delete: ")) - 1
            try:
                if todo_list.tasks[index]:
                    todo_list.delete_task(index)
                    print("TASK DELETED SUCCESSFULLY")
            except IndexError:
                print("Task not found.")
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Thank you for using the To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")


main()
