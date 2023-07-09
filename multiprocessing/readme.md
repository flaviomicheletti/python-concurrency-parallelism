# multiprocessing

The `multiprocessing` module in Python provides a way to create and manage 
processes, allowing you to achieve true parallelism and take advantage of 
multiple CPU cores. Processes in Python are separate instances of the 
interpreter, each with its own memory space, which makes them suitable for 
CPU-bound tasks that can benefit from parallel execution. 

To work with the `multiprocessing` module, you need to import it:

```python
import multiprocessing
```

Here's an overview of how processes differ from threads:

1. **Memory Space**: Each process has its own memory space, while threads 
within a process share the same memory space. 

2. **Global Interpreter Lock (GIL)**: In Python, the GIL prevents multiple 
threads from executing Python bytecode at the same time. This limitation 
doesn't apply to processes, allowing them to execute Python code concurrently 
on different cores. 

3. **Parallelism**: Processes can achieve true parallelism by utilizing 
multiple CPU cores, whereas threads are limited by the GIL and may not run in 
parallel. 

Remember to use multiprocessing judiciously, as creating and managing 
processes incurs some overhead. It's generally recommended for CPU-bound 
tasks or scenarios where you can efficiently divide the workload across 
processes.