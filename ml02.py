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
# filename = 'bezdekIris.data'

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

# 评估算法
# 分离数据集
array = dataset.values
X = array[:, 0:4]
Y = array[:, 4]
validation_size = 0.2
seed = 7
X_train, X_validation, Y_train, Y_validation = \
    train_test_split(X, Y, test_size=validation_size, random_state=seed)

# 算法审查
models = {'LR': LogisticRegression(), 'LDA': LinearDiscriminantAnalysis(),
          'KNN': KNeighborsClassifier(), 'CART': DecisionTreeClassifier(),
          'NB': GaussianNB(), 'SVM': SVC()}
results = []
for key in models:
    key_fold = KFold(n_splits=10, random_state=seed, shuffle=True)
    cv_results = cross_val_score(models[key], X_train, Y_train, cv=key_fold, scoring='accuracy')
    results.append(cv_results)
    print('%s: %f (%f)' % (key, cv_results.mean(), cv_results.std()))

# 箱型图比较算法
fig = pyplot.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
pyplot.boxplot(results)
ax.set_xticklabels(models.keys())
pyplot.show()

# 使用评估数据集评估算法
svm = SVC()
svm.fit(X=X_train, y=Y_train)
predictions = svm.predict(X_validation)
print(accuracy_score(Y_validation, predictions))
print(confusion_matrix(Y_validation, predictions))
print(classification_report(Y_validation, predictions))

# 获取数据，整理数据，切片，统计，可视化，分数据集(训练+验证)，评估算法，比较算法，生成评估报告
