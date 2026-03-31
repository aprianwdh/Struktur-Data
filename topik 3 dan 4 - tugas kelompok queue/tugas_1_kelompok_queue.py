import heapq


class EmergencyQueue:
    def __init__(self):
        self.queue = []

    def add_patient(self, name, priority):
        heapq.heappush(self.queue, (priority, name))

    def process_patient(self):
        if not self.is_empty():
            return heapq.heappop(self.queue)[1]
        else:
            return "Antrian Kosong !"

    def display_queue(self):
        sorted_queue = sorted(self.queue)
        print([patient[1] for patient in sorted_queue])

    def is_empty(self):
        return len(self.queue) == 0


if __name__ == "__main__":
    queue = EmergencyQueue()

    # tambah pasien
    queue.add_patient("Andik", 2)  # serius
    queue.add_patient("Budi", 1)  # kritis
    queue.add_patient("Citra", 3)  # ringan
    queue.add_patient("Dewi", 1)  # kritis

    # tampilkan antrian
    print("Antrian saat ini :")
    queue.display_queue()

    # proses antrian
    print(f"Pasien diproses : {queue.process_patient()}")

    # tampilkan antrian setelah pemrosesan
    print("Antrian saat ini :")
    queue.display_queue()
