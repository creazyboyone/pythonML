from pandas import read_csv
from pandas.plotting import scatter_matrix
from matplotlib import pyplot
from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

filename = 'iris.data'
title = ['separ-length', 'separ-width', 'petal-length', 'petal-width', 'class']
dataset = read_csv(filename, names=title)
# print(dataset)
# 数据集前 10 位数据
print(dataset.head(10))

# 数据维度
print('数据维度：行 %s , 列 %s ' % dataset.shape)
# 数据集类型 <class 'pandas.core.frame.DataFrame'>
print(type(dataset))
# 数据集统计数据 行数，中位值，最大值，最小值，均值，四分位值
print(dataset.describe())

# 数据分类分布
print(dataset.groupby('class').size())

# 数据可视化
# 箱线图
dataset.plot(kind='box', subplots=True, layout=(2, 2), sharex=False, sharey=False)
pyplot.show()
# 直方图
dataset.hist()
pyplot.show()
# 散点矩阵图
scatter_matrix(dataset)
pyplot.show()