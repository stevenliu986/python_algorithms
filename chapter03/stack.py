"""
栈的概念及应用
"""
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return self.items == []

# 栈的应用 - 圆括号匹配
def pair_symbol(symbol_string):
    s= Stack()
    for symbol in symbol_string:
        if symbol == '(':
            s.push(symbol)
        else:
            if s.is_empty():
                return False
            s.pop()
    return s.is_empty()

def matches(left_symbol, right_symbol):
    opens = '({['
    closes = ')}]'
    return opens.index(left_symbol) == closes.index(right_symbol)

# 栈的应用 - 所有类型括号匹配
def pair_symbol2(symbol_string):
    s = Stack()
    mapping = {")": "(", "]": "[", "}": "{"}

    for char in symbol_string:
        if char in mapping.values():
            s.push(char)
        elif char in mapping: # 检查 char 是不是 mapping 的 key
            # s.peek() 获取栈顶元素但不弹出
            if s.is_empty() or s.peek() != mapping[char]:
                return False
            s.pop()

    return s.is_empty()