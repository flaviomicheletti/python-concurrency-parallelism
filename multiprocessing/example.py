import multiprocessing
import threading
import time

# Example CPU-bound task


def square(n):
    return n ** 2


if __name__ == '__main__':
    # Using multiprocessing
    start_time = time.time()
    processes = []
    for i in range(100):
        p = multiprocessing.Process(target=square, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print(f"Multiprocessing time: {time.time() - start_time} seconds")

    # Using threading
    start_time = time.time()
    threads = []
    for i in range(100):
        t = threading.Thread(target=square, args=(i,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print(f"Threading time: {time.time() - start_time} seconds")

"""
In this example, we define a square function that represents a CPU-bound 
task. We then compare the performance of multiprocessing and threading for 
executing this task on multiple inputs. 

By using multiprocessing, we create separate processes for each input, 
allowing them to execute in parallel. We measure the execution time using the 
time module. 

Similarly, we create threads for each input using threading, but due to the 
GIL limitation, they may not run in parallel. However, threading can still be 
useful for tasks that involve I/O operations or waiting for external 
resources, as threads can release the GIL during such operations. 

After executing the code, you should observe that multiprocessing completes 
the task faster than threading, indicating the benefits of true parallelism 
achieved by processes. 

Remember to use multiprocessing judiciously, as creating and managing 
processes incurs some overhead. It's generally recommended for CPU-bound 
tasks or scenarios where you can efficiently divide the workload across 
processes.
"""