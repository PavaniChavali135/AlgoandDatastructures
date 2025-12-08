import threading
import queue
import time

shared_queue = queue.Queue()
# A manual lock used twice for Queue, but added by mistake
manual_lock = threading.Lock()

def inefficient_producer(item_count):
    for i in range(item_count):
        # This forces extra context switching and overhead.
        with manual_lock: 
            shared_queue.put(i)

def optimized_producer(item_count):
    for i in range(item_count):
        #No extra lock overhead.
        shared_queue.put(i)


def test(producer_func, n_threads=10, items_per_thread=10000):
    threads = []
    start_time = time.time()
    
    for _ in range(n_threads):
        t = threading.Thread(target=producer_func, args=(items_per_thread,))
        t.start()
        threads.append(t)
        
    for t in threads:
        t.join()
        
    return time.time() - start_time

print("Running test with 10 threads")
t_inefficient = test(inefficient_producer)
print(f"Inefficient (Double Locking): {t_inefficient:.4f} seconds")

# Clearing queue for next run
shared_queue = queue.Queue()

t_optimized = test(optimized_producer)
print(f"Optimized (No Extra Lock):    {t_optimized:.4f} seconds")