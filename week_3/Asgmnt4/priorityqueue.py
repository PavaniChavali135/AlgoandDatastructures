import time

class Task:
    def __init__(self, task_id, priority, deadline, arrival_time=None):
        self.task_id = task_id
        self.priority = priority
        self.deadline = deadline
        self.arrival_time = arrival_time if arrival_time is not None else time.time()

    def __lt__(self, other):
        if self.priority == other.priority:
            return self.arrival_time < other.arrival_time
        return self.priority < other.priority

    def __repr__(self):
        return (f"Task(id={self.task_id}, prio={self.priority}, "
                f"arr_time={self.arrival_time:.0f})")


class PriorityQueue:
    def __init__(self):
        self.heap = []
        self.task_index_map = {}

    def is_empty(self):
        return len(self.heap) == 0

    def insert(self, task):
        self.heap.append(task)
        n = len(self.heap) - 1
        self.task_index_map[task.task_id] = n
        self.heapify_up(n)

    def extract_min(self):
        if self.is_empty():
            return None
        
        min_task = self.heap[0]
        last_task = self.heap.pop()
        
        del self.task_index_map[min_task.task_id]

        if not self.is_empty():
            self.heap[0] = last_task
            self.task_index_map[last_task.task_id] = 0
            self.heapify_down(0)
            
        return min_task

    def decrease_key(self, task_id, new_priority):
        if task_id not in self.task_index_map:
            raise KeyError(f"Task {task_id} not in queue.")
            
        index = self.task_index_map[task_id]
        task = self.heap[index]
        
        if new_priority >= task.priority:
            return

        task.priority = new_priority
        self.heapify_up(index)

    def increase_key(self, task_id, new_priority):
        if task_id not in self.task_index_map:
            raise KeyError(f"Task {task_id} not in queue.")

        index = self.task_index_map[task_id]
        task = self.heap[index]
        
        if new_priority <= task.priority:
            return

        task.priority = new_priority
        self.heapify_down(index)

    def heapify_up(self, i):
        parent_index = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent_index]:
            self.swap(i, parent_index)
            i = parent_index
            parent_index = (i - 1) // 2

    def heapify_down(self, i):
        n = len(self.heap)
        
        while True:
            smallest = i
            left = 2 * i + 1
            right = 2 * i + 2

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right
            if smallest == i:
                break
                
            self.swap(i, smallest)
            i = smallest

    def swap(self, i, j):
        task_i = self.heap[i]
        task_j = self.heap[j]
        
        self.heap[i], self.heap[j] = task_j, task_i
        
        self.task_index_map[task_i.task_id] = j
        self.task_index_map[task_j.task_id] = i
        
    def peek(self):
        return self.heap[0] if not self.is_empty() else None



    
t1 = Task("task1", 10, "2025-11-22")
t2 = Task("task2", 5, "2025-11-18")
t3 = Task("task3", 7, "2025-11-09")
t4 = Task("task4", 5, "2025-11-12")
    
pq = PriorityQueue()
pq.insert(t1)
pq.insert(t2)
pq.insert(t3)
pq.insert(t4)
    
print(f"Queue state: {pq.heap}")
print(f"Highest priority task: {pq.peek()}")
   


pq.decrease_key("task1", 1)
print(f"Queue state: {pq.heap}")
print(f"New highest priority task: {pq.peek()}")
   


pq.increase_key("task3", 20)
print(f"Queue state: {pq.heap}")
    

print("Extracting all tasks:")
while not pq.is_empty():
    print(f"  Extracted: {pq.extract_min()}")
        
 