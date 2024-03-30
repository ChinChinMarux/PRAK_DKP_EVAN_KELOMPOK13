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
            
    def delete_task(self, index):
        if 1 <= index <= len(self.tasks):
            deleted_task = self.tasks.pop(index - 1)
            self.save_tasks()
            print(f"Tugas '{deleted_task['description']}' dihapus.")
        else:
            print("Indeks tugas tidak valid.")

    def run(self):
        while True:
            print("\n===== To-Do List Manager =====")
            print("1. Tampilkan Daftar Tugas")
            print("2. Tambahkan Tugas Baru")
            print("3. Tandai Tugas Selesai")
            print("4. Hapus Tugas")
            print("5. Keluar")

            pilih = input("Pilih opsi (1/2/3/4/5): ")

            if pilih == "1":
                self.print_tasks()
            elif pilih == "2":
                description = input("Masukkan deskripsi tugas baru: ")
                self.add_task(description)
            elif pilih == "3":
                self.print_tasks()
                index = int(input("Masukkan nomor tugas yang selesai: "))
                self.mark_done(index)
            elif pilih == "4":
                self.print_tasks()
                index = int(input("Masukkan nomor tugas yang akan dihapus: "))
                self.delete_task(index)
            elif pilih == "5":
                print("Terima kasih! Program selesai.")
                break
            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

def main():
    task_manager = TaskManager()
    task_manager.run()

if __name__ == "__main__":
    main()