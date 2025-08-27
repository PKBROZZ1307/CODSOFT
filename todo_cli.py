import sys

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'done': False})
        print(f"Added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
            return
        for idx, t in enumerate(self.tasks, 1):
            status = "✓" if t['done'] else "✗"
            print(f"{idx}. [{status}] {t['task']}")

    def mark_done(self, index):
        if 0 < index <= len(self.tasks):
            self.tasks[index-1]['done'] = True
            print(f"Marked as done: {self.tasks[index-1]['task']}")
        else:
            print("Invalid task number.")

    def remove_task(self, index):
        if 0 < index <= len(self.tasks):
            removed = self.tasks.pop(index-1)
            print(f"Removed: {removed['task']}")
        else:
            print("Invalid task number.")


def main():
    todo = ToDoList()
    while True:
        print("\nTo-Do List CLI")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            task = input("Enter task: ")
            todo.add_task(task)
        elif choice == '2':
            todo.list_tasks()
        elif choice == '3':
            idx = int(input("Enter task number to mark as done: "))
            todo.mark_done(idx)
        elif choice == '4':
            idx = int(input("Enter task number to remove: "))
            todo.remove_task(idx)
        elif choice == '5':
            print("Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
