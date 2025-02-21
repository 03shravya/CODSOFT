import json
import os
import time
import random


class ToDoList:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r") as file:
                    return json.load(file)
            except json.JSONDecodeError:
                return []
        return []

    def save_tasks(self):
        with open(self.filename, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def add_task(self, task):
        self.tasks.append({"task": task, "done": False})
        self.save_tasks()
        print(f"🚀 Task added: '{task}'")
        self.motivate_user()

    def view_tasks(self):
        if not self.tasks:
            print("🎉 No tasks yet! Time to add some and conquer the world!")
        else:
            print("\n📝 Your Legendary To-Do List:")
            for i, task in enumerate(self.tasks, start=1):
                status = "✅" if task["done"] else "❌"
                print(f"{i}. {status} {task['task']}")

    def update_task(self, task_number, new_task):
        if 0 < task_number <= len(self.tasks):
            old_task = self.tasks[task_number - 1]["task"]
            self.tasks[task_number - 1]["task"] = new_task
            self.save_tasks()
            print(f"🔄 Task updated: '{old_task}' → '{new_task}'")
        else:
            print("⚠️ Oops! Invalid task number.")

    def mark_task_done(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["done"] = True
            self.save_tasks()
            print("🎯 Task accomplished! You're on fire! 🔥")
            self.motivate_user()
        else:
            print("⚠️ That task number doesn't exist!")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"🗑️ Task deleted forever: '{removed_task['task']}'")
        else:
            print("⚠️ No such task found!")

    def motivate_user(self):
        quotes = [
            "Keep going! The best is yet to come! 💪",
            "One step at a time, you're making progress! 🏆",
            "Believe in yourself! You got this! 🚀",
            "Small progress is still progress. Keep moving! 🌟",
            "Success is built on small consistent actions. Keep it up! 🔥"
        ]
        print(random.choice(quotes))


if __name__ == "__main__":
    todo = ToDoList()
    while True:
        print("\n✨ Ultimate Productivity Hub ✨")
        print("1️⃣ Add a Task")
        print("2️⃣ View Your Tasks")
        print("3️⃣ Update a Task")
        print("4️⃣ Mark a Task as Completed")
        print("5️⃣ Remove a Task")
        print("6️⃣ Exit")
        choice = input("🎯 What's your move? (Enter number): ")

        if choice == "1":
            task = input("📝 Type your task: ")
            todo.add_task(task)
        elif choice == "2":
            todo.view_tasks()
        elif choice == "3":
            todo.view_tasks()
            num = int(input("✏️ Choose task number to update: "))
            new_task = input("🔄 Type new task description: ")
            todo.update_task(num, new_task)
        elif choice == "4":
            todo.view_tasks()
            num = int(input("✅ Enter task number to mark as done: "))
            todo.mark_task_done(num)
        elif choice == "5":
            todo.view_tasks()
            num = int(input("🗑️ Enter task number to delete: "))
            todo.delete_task(num)
        elif choice == "6":
            print("👋 Exiting... Stay awesome and keep crushing your goals! 🚀")
            break
        else:
            print("⚠️ Invalid choice. Try again!")

