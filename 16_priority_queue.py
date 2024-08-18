class Process:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority

    def __repr__(self):
        return f"{self.data}({self.priority})"

class PriorityQueue:
    def __init__(self):
        self.pq = []

    def insert(self, data, priority):
        self.pq.append(Process(data, priority))
        self.pq.sort(key=lambda x:x.priority)

    def display(self):
        print(f"Current queue: {self.pq}")

    def peek(self):
        if len(self.pq) != 0:
            print(f"Highest priority process: {self.pq[0].data}")
        else:
            print("Current queue is empty.")

    def remove(self):
        if len(self.pq) != 0:
            remElem = self.pq.pop(0)
            print(f"Removed process: {remElem.data}")
        else:
            print("Current queue is empty.")

    def isEmpty(self):
        print(f"Is empty: {len(self.pq) == 0}")

pq = PriorityQueue()
while True:
    command = input()
    if command.startswith("INSERT"):
        _, name, priority = command.split()
        pq.insert(name, int(priority))
    elif command == "DISPLAY":
        pq.display()
    elif command == "PEEK":
        pq.peek()
    elif command == "REMOVE":
        pq.remove()
    elif command == "IS_EMPTY":
        pq.isEmpty()
    else:
        print("Unknown command")