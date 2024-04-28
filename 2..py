import random

import numpy as np
import matplotlib.pyplot as plt
import random


# with open('data.csv', 'w') as f:
#     f.write('')
# for i in range(200):
#     with open('data.csv', 'a+') as f:

#         x = random.random()*50
#         y = random.random()*50
#         f.write(f'{x},{y}\n')

# points = np.genfromtxt('data.csv', delimiter=',')
# # print(points[0,0])
# # 提取points中的两列数据分别作为x，y
# x = points[:, 0]
# y = points[:, 1]
# plt.scatter(x, y)
# plt.show()


# 定义损失函数,另外还要有数据x，y
def compute_cost(w, b, points):
    total_cost = 0
    M = len(points)

    for i in range(M):
        x = points[i, 0]
        y = points[i, 1]
        total_cost += (y - w * x - b) ** 2
    return total_cost / M


# 定义核心算法拟合函数
def average(data):
    return sum(data) / len(data)


