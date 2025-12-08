import threading
import time

shared_counter = 0
lock = threading.Lock()

def slow_way():
    global shared_counter
    for _ in range(1000000):
        with lock:              #locking 1 million times (for every iteration 1 lock)
            shared_counter += 1

def fast_way():
    global shared_counter
    my_private_pile = 0         #local variable (no lock needed)
    
    for _ in range(1000000):
        my_private_pile += 1    #Counting locally
        
    with lock:                  #locking only one time after the whole incremental thing
        shared_counter += my_private_pile


start = time.time()
t1 = threading.Thread(target=slow_way)
t1.start()
t1.join()
print(f"Slow Way took: {time.time() - start:.4f} seconds")

start = time.time()
t2 = threading.Thread(target=fast_way)
t2.start()
t2.join()
print(f"Fast Way took: {time.time() - start:.4f} seconds")