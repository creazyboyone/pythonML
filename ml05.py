# 数据理解
from pandas import read_csv
from pandas import set_option
filename = 'pima_data.csv'
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
         'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = read_csv(filename, names=names)
# 显示所有列
set_option('display.max_columns', None)
# 设置精确度(小数点后2位)
set_option('precision', 2)

# 简单查看数据
print(data.head(10))

# 数据的维度
print(data.shape)

# 数据的属性
print(data.dtypes)

# 描述性统计
print(data.describe())

# 数据分组
print(data.groupby('Outcome').size())

# 数据属性的相关性
print(data.corr(method='pearson'))

# 数据的分布分析
print(data.skew())
