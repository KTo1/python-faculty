from collections import deque

a = 'g2'
b = 'c4f'

la = list(a)
lb = list(b)
print(la, lb)

ia = int(a, 16)
ib = int(b, 16)
print(ia, ib)

isum = hex(ia + ib)
print(isum[2:])

# print(int(, 16))
# print(int(, 16))

# def move_to_end(dct, key):
#     value = dct[key]
#     del dct[key]
#     dct[key] = value
#
#
# dct = dict()
# dct[1] = 1
# print(dct)
# dct[2] = 2
# print(dct)
# dct[3] = 3
# print(dct)
#
# move_to_end(dct, 1)
# print(dct)
#
# # length = 100
# #
# # tmp_list = list(range(100))
# # lst = list(range(length))
# # for k in range(100):
# #     for i in range(length):
# #         for j in range(len(tmp_list)):
# #             lst.insert(0, j)
#
