from collections import deque


class TaskManager:
    def __init__(self):
        self.task = deque()

    def add_task(self, task):
        self.task.append(task)

    def remove_task(self):
        if not self.is_empty():
            return self.task.popleft()  # menhgapus tugas dari depan
        else:
            return "tidak ada tugas dalam antrian"

    def add_urgent_task(self, task):
        self.task.appendleft(task)

    def display_task(self):
        print(list(self.task))  # konversi deque ke list

    def is_empty(self):
        return len(self.task) == 0


if __name__ == "__main__":
    tasks = TaskManager()
    # Tambah tugas
    tasks.add_task("Kerjakan laporan")
    tasks.add_task("Meeting dengan tim")
    tasks.add_urgent_task("Bug fix urgent")  # Tugas ini masuk ke depan antrian
    # Tampilkan antrian tugas
    print("Daftar Tugas:")
    tasks.display_task()  # Output: ['Bug fix urgent', 'Kerjakan laporan', 'Meeting dengan tim']
    # Proses tugas
    print("Tugas dikerjakan:", tasks.remove_task())  # Output: Bug fix urgent
    # Tampilkan antrian setelah pemrosesan
    print("Daftar Tugas setelah pemrosesan:")
    tasks.display_task()  # Output: ['Kerjakan laporan', 'Meeting dengan tim']
