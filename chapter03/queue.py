"""
队伍的概念及应用
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