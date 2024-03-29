import json

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open("tugas.json", "r") as file:
                tasks = json.load(file)
        except FileNotFoundError:
            tasks = []
        return tasks

    def save_tasks(self):
        with open("tugas.json", "w") as file:
            json.dump(self.tasks, file)

    def print_tasks(self):
        if not self.tasks:
            print("Tidak ada tugas.")
        else:
            for idx, task in enumerate(self.tasks, 1):
                print(f"{idx}. {task['description']} - {'Selesai' if task['done'] else 'Belum Selesai'}")