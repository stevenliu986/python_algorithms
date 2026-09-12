"""
双端队列实现及示例
"""

class Deque:
    """假设双端队列的后端是位置0处"""
    def __init__(self):
        """创建双端队列"""
        self._items = []

    def is_empty(self):
        """检查双端队列是否为空"""
        return not bool(self._items)

    def add_front(self, item):
        self._items.append(item)

    def add_rear(self, item):
        self._items.insert(0, item)

    def remove_front(self):
        return self._items.pop()

    def remove_rear(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

def pal_check(a_str):
    q = Deque()

    for char in a_str:
        q.add_front(char)

    while q.size() > 1:
        first_char = q.remove_front()
        last_char = q.remove_rear()
        if first_char != last_char:
            return False
    return True
print(pal_check('radar'))