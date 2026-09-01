
def anagram_solution_1(str1, str2):
    """
    求异序词：双循环法，时间复杂度O(N2)
    :param str1: 字符串1
    :param str2: 字符串2
    :return: True or False
    """
    if len(str1) != len(str2):
        return False
    a_list = list(str2)
    pos_1 = 0
    still_ok = True
    while pos_1 < len(str1) and still_ok:
        pos_2 = 0
        found = False
        while pos_2 < len(a_list) and not found:
            if str1[pos_1] == a_list[pos_2]:
                found = True
            else:
                pos_2 += 1
        if found:
            a_list[pos_2] = None
        else:
            still_ok = False
        pos_1 += 1
    return still_ok

def anagram_solution_2(str1, str2):
    """
    求异序词：双循环法，时间复杂度O(N)
    :param str1: 字符串1
    :param str2: 字符串2
    :return: True or False
    """
    if len(str1) != len(str2):
        return False
    c1 = [0] * 26
    c2 = [0] * 26
    for i in range(len(str1)):
        pos = ord(str1[i]) - ord('a')
        c1[pos] += 1
    for i in range(len(str2)):
        pos = ord(str2[i]) - ord('a')
        c2[pos] += 1
    j = 0
    is_ok = True
    while j < 26 and is_ok:
        if c1[j] == c2[j]:
            j += 1
        else:
            is_ok= False
    return is_ok

def anagram_solution_3(str1, str2):
    if len(str1) != len(str2):
        return False
    c1, c2 = [0] * 26, [0] * 26
    for i in range(len(str1)):
        c1[ord(str1[i]) - ord('a')] += 1
        c2[ord(str2[i]) - ord('a')] += 1
    return c1 == c2