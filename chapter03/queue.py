"""
队列的概念及应用
"""
class Queue:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.insert(0, item)

    def dequeue(self):
        return self._items.pop()

    def is_empty(self):
        return self._items == []

    def size(self):
        return len(self._items)

def hot_potato(name_list,num):
    sim_queue = Queue()
    for name in name_list:
        sim_queue.enqueue(name)
    while sim_queue.size() > 1:
        for _ in range(num):
            sim_queue.enqueue(sim_queue.dequeue())
        sim_queue.dequeue()

    return sim_queue.dequeue()

print(hot_potato(['Bill', 'David', 'Susan', 'Jane', 'Ken', 'Brad'], 7))

class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm # 打印速度
        self.current_task = None # 打印任务
        self.time_remaining = 0 # 任务倒计时

    def tick(self): # 打印一秒
        if self.current_task is not None:
            self.time_remaining -= 1
            if self.time_remaining <= 0:
                self.current_task = None

    def busy(self):
        return self.current_task is not None

    def start_next(self, new_task):
        self.current_task = new_task
        # 根据任务的页数计算完成打印所需的时间（单位：秒）
        self.time_remaining = new_task.get_pages() * 60 / self.page_rate

import random

class Task:
    def __init__(self, time):
        self.time_stamp = time
        self.pages = random.randrange(1, 21) # 随机产生打印的页数（1 - 20 页）

    def get_pages(self):
        return self.pages

    def get_stamp(self):
        return self.time_stamp

    def wait_time(self, current_time):
        return current_time - self.time_stamp

def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []

    for current_second in range(num_seconds):
        if new_print_task():
            task = Task(current_second)
            print_queue.enqueue(task)

        if (not lab_printer.busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)

        lab_printer.tick()

    # 避免出现除 0 的情况
    if waiting_times:
        average_waiting_time = sum(waiting_times) / len(waiting_times)
        print(f"Average waiting time: {average_waiting_time:6.2f} seconds" + f"{print_queue.size():3d} tasks remaining.")
    else:
        print(
            "No tasks were completed during the simulation. "
            f"{print_queue.size():3d} tasks remaining."
        )

def new_print_task():
    # 概率同样是 1/180，但避免了产生完整的整数区间，执行效率更高
    return random.random() < (1 / 180)

# 执行模拟
for _ in range(10):
    simulation(3600, 5)