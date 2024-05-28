class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added.")

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' deleted.")
        else:
            print(f"Task '{task}' not found.")

    def mark_completed(self, task):
        if task in self.tasks:
            print(f"Task '{task}' marked as completed.")
        else:
            print(f"Task '{task}' not found.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task}")
        else:
            print("No tasks to display.")

def main():
    todo_list = TodoList()

    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Completed")
        print("4. Display Tasks")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)
        elif choice == '2':
            task = input("Enter task to delete: ")
            todo_list.delete_task(task)
        elif choice == '3':
            task = input("Enter task to mark as completed: ")
            todo_list.mark_completed(task)
        elif choice == '4':
            todo_list.display_tasks()
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 5.")

if __name__ == "__main__":
    main()
