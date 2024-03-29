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

    def add_task(self, description):
        task = {"description": description, "done": False}
        self.tasks.append(task)
        self.save_tasks()
        print(f"Tugas '{description}' ditambahkan.")

    def mark_done(self, index):
        if 1 <= index <= len(self.tasks):
            self.tasks[index - 1]["done"] = True
            self.save_tasks()
            print(f"Tugas '{self.tasks[index - 1]['description']}' ditandai sebagai selesai.")
        else:
            print("Indeks tugas tidak valid.")