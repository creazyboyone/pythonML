from pandas import read_csv
from numpy import set_printoptions
from sklearn.feature_selection import RFE
from sklearn.feature_selection import chi2
from sklearn.feature_selection import SelectKBest
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.decomposition import PCA

filename = 'pima_data.csv'
names = ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI',
         'DiabetesPedigreeFunction', 'Age', 'Outcome']
data = read_csv(filename, names=names)
array = data.values
X = array[:, 0:8]
Y = array[:, 8]

# 单变量特征选定
test = SelectKBest(score_func=chi2, k=4)
fit = test.fit(X, Y)
set_printoptions(precision=3)
print(fit.scores_)
features = fit.transform(X)
print(features)

# 递归特征消除
model = LogisticRegression()
rfe = RFE(model, 3)
fit = rfe.fit(X, Y)
print('特征个数: {},   被选定的特征: {},    特征排名: {}'.format(fit.n_features_, fit.support_, fit.ranking_))

# 主要成分分析
pca = PCA(n_components=3)
fit = pca.fit(X)
print("解释方差：%s" % fit.explained_variance_ratio_)
print(fit.components_)

# 特征重要性
model = ExtraTreesClassifier()
fit = model.fit(X, Y)
print(fit.feature_importances_)