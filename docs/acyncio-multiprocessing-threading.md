# Differences between acyncio, multiprocessing and threading

It would be great to learn about the differences between acyncio, 
multiprocessing and threading 


1. **Asyncio**: 

    - `asyncio` is a Python library that provides support for writing 
    asynchronous code using coroutines, event loops, and non-blocking I/O 
    operations. 

    - It allows you to write concurrent code that can handle multiple tasks 
    without blocking the execution. 

    - It is primarily used for building asynchronous network servers, web 
    applications, and other I/O-bound tasks. 

    - `asyncio` utilizes a single thread and an event loop to manage coroutines. 
    It switches between different coroutines when one coroutine awaits for an I/O 
    operation to complete. 

    - It is well-suited for I/O-bound tasks but may not be suitable for CPU-bound 
    tasks due to the Global Interpreter Lock (GIL) limitation in CPython. 

2. **Multiprocessing**: 

    - `multiprocessing` is a Python module that allows the execution of multiple 
    processes in parallel, taking advantage of multiple CPU cores available on a 
    system. 

    - It enables the creation of separate processes, each having its own Python 
    interpreter and memory space, which avoids the GIL limitation. 

    - The `multiprocessing` module provides a Process class for creating and 
    managing processes, as well as various mechanisms for communication and 
    synchronization between processes. 

    - It is useful for CPU-bound tasks that can be parallelized, as each process 
    runs independently and can utilize a different CPU core. 

3. **Threading**: 

    - `threading` is a Python module for creating and managing threads, which are 
    lighter-weight than processes and share the same memory space within a 
    process. 

    - Threads can run concurrently, but due to the GIL in CPython, only one 
    thread can execute Python bytecode at a time. 

    - `threading` is useful for I/O-bound tasks where threads can be used to 
    perform concurrent I/O operations without blocking the execution. 

    - However, due to the GIL, it may not provide significant performance 
    improvements for CPU-bound tasks. 


## In summary, here are the key differences: 

- `asyncio` is suitable for I/O-bound tasks and uses coroutines with an event 
loop to achieve asynchronous execution. 

- `multiprocessing` is suitable for CPU-bound tasks and runs multiple 
processes in parallel, leveraging multiple CPU cores. 

- `threading` is suitable for I/O-bound tasks and allows concurrent execution 
within a single process, but due to the GIL, it may not improve performance 
significantly for CPU-bound tasks. 

Choosing the appropriate concurrency mechanism depends on the nature of your 
task, whether it's I/O-bound or CPU-bound, and whether you require 
parallelism or asynchronous execution. 


## Community Comments

Asyncio and threading are almost identical, but threading is more intuitive. 
They are mainly used for I/O bound tasks. 

Mulltiprocessing is very different. It bypasses the GIL (look it up if you 
don't know what it is). It is mainly used to improve performance with 
parallel programming.

---

Both asyncio and threading are concurrent.Threading is being handled by the 
OS and AsyncIO is being handled within python (the async event loop).
Threads can execute small operations to speeds things up (e.g. adding more 
robots to handle the work, difficult to oversee and manage when program grows 
big. Also race conditions where: comes out weird the outcome) 

`asyncio` is done by using an event loop where task are being awaited (e.g. 
non-blocking! tasks that are fired up and deliver some result while the 
program is doing other things) At the end of the event loop (yes it is a 
loop, all the results are gathered from the loop and it starts over again) 
If tasks are blocking, asyncio isn't the right tool at all. Luckily you can 
also "throw" blocking tasks into a different executor so that they dont slow 
down your async stuff. 

Multiprocessing is using multiple processes to do the grunt work. It kind of 
bypasses the GIL by having more processes with another GIL.Drawback can be 
copied memory and such. 

Basically every technique has an advantage and a drawback. I do like asyncio 
because it is a simple solution to a complex problem.The thing is that when 
using an Executor you can test different scenario's within Python because you 
can swap out multiprocessing, threading and asyncio easily.Test and see what 
does what.

---

Threading and multiprocessing are preemptive, coroutines are not. Coroutines 
and threading are default-share-everything, multiprocessing is default-share-
nothing. Coroutines are easier to debug than threads.


