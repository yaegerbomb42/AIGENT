from queue import Queue
import threading

class TaskQueue:
    def __init__(self):
        self.queue = Queue()

    def add_task(self, task_func, *args, **kwargs):
        self.queue.put((task_func, args, kwargs))

    def run(self):
        while not self.queue.empty():
            func, args, kwargs = self.queue.get()
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(f"❌ Task failed: {e}")
