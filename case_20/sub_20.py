'''
一球从100米高度自由落下，每次落地后反跳回原高度的一半；
再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
'''

h = 100  # 自由落体高度
n = 10  # 落地次数

s = []  # 每次下落高度

for i in range(n):
    s.append(h)
    h /= 2

print('总高度：', 2 * sum(s) - s[0])
print('反弹高度：', s[-1] / 2)

# 等比数列求解法
q = 1 / 2
a1 = 100

a11 = a1 * (q ** (11 - 1))
s10 = a1 * ((1 - q ** 10) / (1 - q))

print('总高度：', 2 * s10 - a1)
print('反弹高度：', a11)