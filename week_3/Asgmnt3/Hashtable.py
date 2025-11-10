import random

class MapNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __repr__(self):
        return f"({self.key}: {self.value})"

class HashMapChain:
    
    def __init__(self, capacity=10):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self.capacity = capacity
        self._buckets = [None] * self.capacity
        
        self._prime_p = 2**89 - 1
        self._mult_a = random.randint(1, self._prime_p - 1)
        self._add_b = random.randint(0, self._prime_p - 1)

    def get_index(self, key):
        k = hash(key)
        hash_val = ((self._mult_a * k + self._add_b) % self._prime_p) % self.capacity
        return hash_val if hash_val >= 0 else hash_val + self.capacity

    def put(self, key, value):
        index = self.get_index(key)
        
        if self._buckets[index] is None:
            self._buckets[index] = []
        
        bucket = self._buckets[index]
        
        for node in bucket:
            if node.key == key:
                node.value = value
                return
        
        bucket.append(MapNode(key, value))

    def get(self, key):
        index = self.get_index(key)
        bucket = self._buckets[index]
        
        if bucket is None:
            raise KeyError(f"Key not found: {key}")
            
        for node in bucket:
            if node.key == key:
                return node.value
                
        raise KeyError(f"Key not found: {key}")

    def remove(self, key):
        index = self.get_index(key)
        bucket = self._buckets[index]
        
        if bucket is None:
            raise KeyError(f"Key not found: {key}")
        
        for i in range(len(bucket)):
            if bucket[i].key == key:
                bucket.pop(i)
                return
                
        raise KeyError(f"Key not found: {key}")

    def print_table(self):
        print("Hash Map State")
        for i, bucket in enumerate(self._buckets):
            if bucket:
                print(f"Bucket {i}: {bucket}")
        



hm = HashMapChain(capacity=5)

hm.put("Mazda", 1)
hm.put("BMW", 2)
hm.put("Honda", 3)
hm.put("Tesla", 4)
hm.put("Hyundai", 5)
    
hm.print_table()

print("searching")
print(f"Fetch 'BMW': {hm.get('BMW')}")
print(f"Fetch 'Tesla': {hm.get('Tesla')}")

print("adding to table")
hm.put("Nissan", 100)
print(f"Fetch 'Nissan' (updated): {hm.get('Nissan')}")
print("\nMap after update:")
hm.print_table()

print("Deleting from table")
hm.remove("Hyundai")
print("Map after deleting 'Hyundai':")
hm.print_table()

   
        
