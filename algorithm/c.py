# encoding=utf8
a = [5, 10, 15, 20, 25, 30, 35]

b = [2, 4, 6]
a = [2, 4, 5, 6, 7, 9, 10, 11, 12, 14, 15, 16, 17, 19, 20, 21, 22, 24, 25, 26, 27, 29, 30, 31, 32, 34, 35, 36, 37, 39, 41]
b = [1,2 ]
print(sorted(set([i + j for i in a for j in b] + a + b)))
