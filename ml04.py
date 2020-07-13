# 分别用python标准类库和Numpy和Pandas来导入csv,推荐用Pandas
from csv import reader
from numpy import loadtxt
from pandas import read_csv
import numpy as np
# Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age,Outcome
filename = 'pima_data.csv'

# python标准类库导入csv数据
with open(filename, 'rt') as raw_data:
    readers = reader(raw_data, delimiter=',')
    x = list(readers)
    data = np.array(x).astype('float')
    print(data.shape)

# Numpy导入csv
with open(filename, 'rt') as raw_data2:
    data = loadtxt(raw_data2, delimiter=',')
    print(data.shape)

# Pandas导入csv
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
         'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = read_csv(filename, names=names)
print(data.shape)
