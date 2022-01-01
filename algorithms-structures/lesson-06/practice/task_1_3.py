"""
Задание 1.

Вам нужно взять 5 любых скриптов, написанных ВАМИ в рамках работы над ДЗ
курсов Алгоритмы и Основы

На каждый скрипт нужно два решения - исходное и оптимизированное.

Вы берете исходное, пишете что это за задание и с какого оно курса.
Далее выполняете профилирование скрипта средствами memory_profiler

Вы оптимизируете исходное решение.
Далее выполняете профилирование скрипта средствами memory_profiler

Вам нужно написать аналитику, что вы сделали для оптимизации памяти и
чего добились.


ВНИМАНИЕ:
1) скрипты для оптимизации нужно брать только из сделанных вами ДЗ
курсов Алгоритмы и Основы
2) нельзя дублировать, коды, показанные на уроке
3) для каждого из 5 скриптов у вас отдельный файл, в нем должна быть версия до
и версия после оптимизации
4) желательно выбрать те скрипты, где есть что оптимизировать и не брать те,
где с памятью и так все в порядке
5) не нужно писать преподавателю '''я не могу найти что оптимизировать''', это
отговорки. Примеров оптимизации мы перечислили много: переход с массивов на
генераторы, numpy, использование слотов, применение del, сериализация и т.д.

Это файл для третьего скрипта
"""

"""
Через NumPy

    92     25.7 MiB      6.2 MiB      160000           stack.push(j)
    
"""

from memory_profiler import profile
from numpy import array, append, array_equal


class StackNp:

    def __init__(self, capacity):
        self._capacity = capacity
        self._elems = array([])
        self._add_stack()

    def push(self, element):
        if self.is_empty():
            self._add_stack()
        if len(self._current_stack) >= self._capacity:
            self._add_stack()
        self._current_stack = append(self._current_stack, element)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None

        elem = self._current_stack.pop()
        if len(self._current_stack) <= 0:
            self._del_stack()
        return elem

    def is_empty(self):
        return array_equal(self._elems, array([]))

    def _set_current_stack(self):
        if not self.is_empty():
            self._current_stack = self._elems[len(self._elems) - 1]
        else:
            self._current_stack = None

    def _add_stack(self):
        self._elems = append(self._elems, array([]))
        self._set_current_stack()

    def _del_stack(self):
        if not self.is_empty():
            del self._elems[len(self._elems) - 1]
        self._set_current_stack()

    def __str__(self):
        return 'In stack:\n' + '\n'.join(map(str, self._elems))


class Stack:

    def __init__(self, capacity):
        self._capacity = capacity
        self._elems = []
        self._add_stack()

    def push(self, element):
        if self.is_empty():
            self._add_stack()
        if len(self._current_stack) >= self._capacity:
            self._add_stack()
        self._current_stack.append(element)

    def pop(self):
        if self.is_empty():
            print('Stack is empty')
            return None

        elem = self._current_stack.pop()
        if len(self._current_stack) <= 0:
            self._del_stack()
        return elem

    def is_empty(self):
        return self._elems == []

    def _set_current_stack(self):
        if not self.is_empty():
            self._current_stack = self._elems[len(self._elems) - 1]
        else:
            self._current_stack = None

    def _add_stack(self):
        self._elems.append([])
        self._set_current_stack()

    def _del_stack(self):
        if not self.is_empty():
            del self._elems[len(self._elems) - 1]
        self._set_current_stack()

    def __str__(self):
        return 'In stack:\n' + '\n'.join(map(str, self._elems))


# @profile
def stack_ops():
    # stack = Stack(100)
    #
    # for j in range(160000):
    #     stack.push(j)
    #
    # stack.pop()
    # stack.pop()

    # ar = array([])
    # ar = append(ar, [1])
    # ar = append(ar, [2])
    # ar = append(ar, [3])
    # print(ar)
    stack_np = StackNp(6)
    for j in range(16):
        stack_np.push(j)

    print(stack_np)


if __name__ == "__main__":
    stack_ops()
