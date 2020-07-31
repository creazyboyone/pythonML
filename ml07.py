# 数据预处理
from pandas import read_csv
from numpy import set_printoptions
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import Binarizer

filename = 'pima_data.csv'
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
         'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = read_csv(filename, names=names)

array = data.values
# array[:, 0:8]  是取[0,8) , 即[0,7]
X = array[:, 0:8]
Y = array[:, 8]

# 调整数据尺度
transformer = MinMaxScaler(feature_range=(0, 1))
newX = transformer.fit_transform(X)
set_printoptions(precision=3)
print(newX)

# 正态化数据
transformer = StandardScaler().fit(X)
newX = transformer.fit_transform(X)
set_printoptions(precision=3)
print(newX)

# 标准化数据
transformer = Normalizer().fit(X)
newX = transformer.fit_transform(X)
set_printoptions(precision=3)
print(newX)

# 二值化数据
transformer = Binarizer(threshold=0.0).fit(X)
newX = transformer.fit_transform(X)
set_printoptions(precision=3)
print(newX)
