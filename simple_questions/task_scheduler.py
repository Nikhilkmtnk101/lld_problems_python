"""
Problem Statement:
    Implement an InMemory Task scheduler Library that supports these functionalities:
        1> Submit a task and a time at which the task should be executed. --> schedule(task, time)
        2> Schedule a task at a fixed interval --> scheduleAtFixedInterval(task, interval) - interval is in seconds
           The first instance will trigger it immediately and the next execution would start after interval seconds
           of completion of the preceding execution.
           If a task has an interval of 10 seconds and submitted at 2:00 pm then, It will be executed at 2:00 pm
           Once the execution is completed + 10 seconds(interval) it will trigger the next execution and so on.
    Expectations
    The number of worker threads should be configurable and manage them effectively.
    Code/Design should be modular and follow design patterns.
    Don’t use any external/internal libs that provide the same functionality and core APIs should be used.
"""
import heapq
import threading
import time
from threading import Lock


class Task:
    def __init__(self, func, *args, **kwargs):
        self.func = func
        self.interval = None
        self.args = args
        self.kwargs = kwargs

    def set_interval(self, interval):
        self.interval = interval

    def execute(self):
        self.func(*self.args, **self.kwargs)

class Worker(threading.Thread):
    def __init__(self, worker_id, task_queue, task_scheduler):
        threading.Thread.__init__(self)
        self.worker_id = worker_id
        self.task_queue = task_queue
        self.task_scheduler = task_scheduler
        self.daemon = True
        self.start()

    def run(self):
        while True:
            if len(self.task_queue) == 0:
                continue
            with self.task_scheduler.lock:
                execution_time, task = heapq.heappop(self.task_queue)
                current_time = time.time()
                if execution_time > current_time:
                    time.sleep(execution_time-current_time)
                print(f'Executing task from worker_id {self.worker_id} at time {time.ctime()}')
                task.execute()

                if task.interval:
                    current_time = time.time()
                    next_scheduled_time = current_time + task.interval
                    heapq.heappush(self.task_queue, (next_scheduled_time, task))

class TaskScheduler:
    def __init__(self, no_of_workers):
        self.tasks = []
        heapq.heapify(self.tasks)
        self.no_of_workers = no_of_workers
        self.workers = []
        self.lock = Lock()

        for i in range(1, no_of_workers+1):
            worker = Worker(f'worker_id_{i}', self.tasks, self)
            self.workers.append(worker)

    def schedule_task(self, task, scheduled_time):
        print(f'Pushing task for execution at time {time.ctime()}')
        self.lock.acquire()
        heapq.heappush(self.tasks, (scheduled_time, task))
        self.lock.release()

    def schedule_task_with_fixed_interval(self, task, interval):
        task.interval = interval
        self.schedule_task(task, time.time())

def sum_func(a, b):
    print(f'{a} + {b} = {a + b}')


def mul_func(a, b):
    print(f'{a} * {b} = {a * b}')

if __name__ == '__main__':
    task1 = Task(sum_func,10, 20)
    task2 = Task(mul_func, 10, 20)
    task_schedular = TaskScheduler(3)
    task_schedular.schedule_task(task1, time.time() + 2)
    task_schedular.schedule_task_with_fixed_interval(task2, 5)
    time.sleep(100)
