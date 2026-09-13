class Node:
    """一个链表节点"""

    def __init__(self, node_data):
        self._data = node_data
        self._next = None

    def get_data(self):
        """获取节点数据"""
        return self._data

    def set_data(self, node_data):
        """设置节点数据"""
        self._data = node_data

    data = property(get_data, set_data)

    def get_next(self):
        """获取下一个节点"""
        return self._next

    def set_next(self, node_next):
        """设置下一个节点"""
        self._next = node_next

    next = property(get_next, set_next)

    def __str__(self):
        return str(self._data)

temp = Node(10)
print(temp.data)

class UnorderedList:
    def __init__(self):
        self._head = None

    def add(self, item):
        # 1. 节点的创建是在这里完成的：外部传入数据 item，我们实例化一个全新的 Node
        new_node = Node(item)

        # 2. 让新节点的 _next 指向原先的头节点
        new_node.set_next(self._head)

        # 3. 关键点：列表更新自己的 head 引用，让它指向这个刚创建的新节点
        self._head = new_node

    def is_empty(self):
        return self._head is None

    def size(self):
        count = 0
        current = self._head

        while current is not None:
            count += 1
            current = current._next
        return count

    def search(self, item):
        current = self._head
        while current is not None:
            if current._data == item:
                return True
            current = current._next
        return False

    def remove(self, item):
        if self.is_empty():
            return False

        current = self._head
        previous = None

        while current is not None:
            if current.data == item:
                # 分情况处理删除逻辑
                if previous is None:
                    # 情况 1：要删的是头节点，直接让 self._head 指向下一个节点
                    self._head = current.next
                else:
                    # 情况 2：要删的是中间或尾部节点，让前驱节点绕过当前节点
                    previous.next = current.next

                return True  # 成功删除，退出函数

            # 指针同步后移：previous 抢先接管 current 的位置，current 再往后走
            previous = current
            current = current.next

        return False  # 遍历结束仍未找到目标元素

    def add_rear(self,item):
        new_node = Node(item)
        current = self._head

        # 如果头节点为空，则直接添加
        if current is None:
            self._head = new_node
        else:
            while current._next is not None:
                current = current._next
            current._next = new_node


