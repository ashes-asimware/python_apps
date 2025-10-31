from concurrent.futures import ThreadPoolExecutor
import threading as th
import random as r
import time

def worker(worker_id):
    # Generate a random integer between 1 and 20
    random_int = r.randint(1, 20)
    time.sleep(random_int)
    print(f"{th.current_thread().name} finished.")

# Create a ThreadPoolExecutor with max_workers=20
with ThreadPoolExecutor(max_workers=20) as executor:
    # Submit 20 tasks to the pool
    futures = [executor.submit(worker, i+1) for i in range(20)]   

print("All threads have completed.")
