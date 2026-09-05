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

# 栈的应用 - 进制转换
def base_converter(dec_number: int, base: int) -> str:
    """
    任意进制转换
    :param dec_number: 源数字
    :param base: 进制
    :return: 根据base转换后的结果
    """
    if dec_number == 0:
        return '0'
    s = Stack()
    digits = '0123456789ABCDEF'
    while dec_number > 0:
        rem = dec_number % base
        s.push(rem)
        dec_number //= base
    converted_string = ''
    while not s.is_empty():
        converted_string += digits[s.pop()]
    return converted_string


def infix_postfix_converter(algorithm_str):
    """
    这是一个将中缀表达式转换为后缀表达式的函数 - 仅限简单的四则运算，不支持括号
    :param algorithm_str: 中缀表达式字符串
    :return: 后缀表达式字符串
    """
    s = Stack()
    priority = {'*':3, '/': 3, '+': 1, '-':1}
    result = []
    for char in algorithm_str:
        if char == ' ':
            continue
        if char not in priority:
            result.append(char)
        else:
            while not s.is_empty() and priority[char] <= priority[s.peek()]:
                pop_result = s.pop()
                result.append(pop_result)
            s.push(char)
    while not s.is_empty():
        result.append(s.pop())
    return ''.join(result)
print(infix_postfix_converter('a + b * c'))