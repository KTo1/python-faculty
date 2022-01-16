"""
Задание 1.

Реализуйте кодирование строки по алгоритму Хаффмана.
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на примеры с урока,
 сделать свою версию алгоритма
Разрешается и приветствуется изменение имен переменных,
выбор других коллекций, различные изменения
и оптимизации.

2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например,
через ООП или предложить иной подход к решению.
"""

"""
https://habr.com/ru/post/438512/
"""

from collections import Counter, deque
from task_2 import BinaryTree


def haffman_tree(seq):
    if False:
        return
    else:
        el1 = seq.popleft()
        el2 = seq.popleft()
        weight = el1.value + el2.value
        new_el = BinaryTree('', value=weight)
        for i in range(len(seq)):
            if seq[i][1] > weight:
                seq.insert(i, new_el)


if __name__ == '__main__':
    s = deque(sorted(dict(Counter('beep boop beer!')).items(), key=lambda i: i[1]))
    for i in range(len(s)):
        s[i] = (BinaryTree(s[i][0], value=s[i][1]), s[i][1])

    print(s)

    haffman_tree(s)