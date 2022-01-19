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


class BinaryTree:
    def __init__(self, left=None, right=None, value=0):
        self.left = left
        self.right = right
        self.value = value


class HaffmanTree:
    def encode(self, string):
        # строим дерево
        tree = self.build(string)

        # расставляем 0, 1
        self._walk(tree)

        # собираем коды

    def build(self, string):
        return self._haffman_tree(self._initial(string))

    def _walk(self, node):
        if isinstance(node, str):
            print(node)
            return
        if node.left is not None:
            print(0)
            self._walk(node.left)
        if node.right is not None:
            print(1)
            self._walk(node.right)

    def _initial(self, string):
        sequence = deque(sorted(dict(Counter(string)).items(), key=lambda i: i[1]))
        for i in range(len(sequence)):
            sequence[i] = (BinaryTree(sequence[i][0], value=sequence[i][1]), sequence[i][1])

        return sequence

    def _haffman_tree(self, seq):
        if len(seq) == 1:
            return seq[0]

        el1, el2 = seq.popleft(), seq.popleft()
        weight = el1[1] + el2[1]
        new_el = BinaryTree(left=el1[0], right=el2[0], value=weight)
        if len(seq) <= 0:
            seq.insert(0, new_el)
            return seq[0]
        else:
            for i in range(len(seq)):
                if seq[i][1] >= weight:
                    seq.insert(i, (new_el, weight))
                    break
                if i == len(seq)-1:
                    seq.append((new_el, weight))
            self._haffman_tree(seq)
        return seq[0]


if __name__ == '__main__':
    s = 'beep boop beer!'
    ht = HaffmanTree()
    tree = ht.build(s)
    ht._walk(tree)
    print(tree)