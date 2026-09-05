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

import re

def infix_postfix_converter(infix_str):
    """
    支持多位数、任意空格以及嵌套括号的中缀转后缀表达式转换器
    """
    s = Stack()
    # 注意：'(' 在栈内被比对时，视为最低优先级，防止被普通运算符错误弹出
    priority = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    result = []

    # 1. 修改正则表达式：加入 '(' 和 ')' 的匹配
    tokens = re.findall(r'\d+|[a-zA-Z]+|[+\-*/()]', infix_str)

    for token in tokens:
        # 2. 遇到左括号：直接压栈，作为隔离屏障
        if token == '(':
            s.push(token)

        # 3. 遇到右括号：不断弹栈，直到弹出对应的左括号为止
        elif token == ')':
            top_token = s.pop()
            while top_token != '(':
                result.append(top_token)
                top_token = s.pop()

        # 4. 遇到运算符：比对优先级，弹出高/同优先级的运算符
        elif token in priority:
            while not s.is_empty() and priority[token] <= priority[s.peek()]:
                result.append(s.pop())
            s.push(token)

        # 5. 遇到操作数（数字或字母）：直接追加到输出
        else:
            result.append(token)

    # 6. 清空栈中剩余的运算符
    while not s.is_empty():
        result.append(s.pop())

    return ' '.join(result)

print(infix_postfix_converter('10 + 3 * 5 / (16 - 4)'))