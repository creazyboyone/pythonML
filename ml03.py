import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# numpy 速成
# 数据创建
my_array = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(my_array)
print(my_array.shape)
# 数据访问(切片)
print(my_array[2, :-1])
# 数据(向量)运算
you_array = np.array([[11, 12, 13], [14, 15, 16], [17, 18, 19]])
print(my_array + you_array)
print(my_array * you_array)  # *乘
print(my_array.dot(you_array))  # ·乘


# matplotlib 速成 (2D绘图库)
# 线条图
plt.plot(my_array)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

# 散点图
plt.scatter(my_array, you_array)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()

# pandas 速成 (提供复杂的数据类型和数据分析运算方法)
# 一维数组 Series
pandas_array = np.array([1, 2, 3])
index = ['a', 'b', 'c']
my_series = pd.Series(pandas_array, index=index)
print(my_series)
print(my_series[0])
print(my_series['c'])

# DataFrame (二维表格型数据结构)
col_index = ['A', 'B', 'C']
my_data_frame = pd.DataFrame(my_array, index=index, columns=col_index)
print(my_data_frame)
print(my_data_frame['C'])
