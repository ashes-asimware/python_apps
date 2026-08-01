import threading as th
import random as r
import time

def worker():
    # Generate a random integer between 1 and 100
    random_int = r.randint(1, 20)
    time.sleep(random_int)
    print(f"{th.current_thread().name} finished.")

threads = []
for i in range(20):
    t = th.Thread(target=worker, name=f"Worker-{i+1}")
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have completed.")