import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols, glm

wine = pd.read_csv('wine.csv')
wine.columns = wine.columns.str.replace(' ', '_')
# ■ 퀄리티값
red_wine_quality = wine.loc[wine['type']=='red', 'quality']
print(red_wine_quality)#콘솔창에 띄우기

white_wine_quality = wine.loc[wine['type']=='white', 'quality']
print(white_wine_quality)#콘솔창에 띄우기


# 그룹간의 차이를 확인 t test  라는 변수에 넣음. t=

ttest = stats.ttest_ind(red_wine_quality, white_wine_quality, equal_var = False)
print(ttest)

# ■ 선형 회귀 분석: 독립변수 = 연속된값을 가진 변수만 사용 가능
# 종속변수는 quality
Rformula ='quality ~ fixed_acidity+volatile_acidity+citric_acid+residual_sugar+chlorides+free_sulfur_dioxide + total_sulfur_dioxide+density+ pH+sulphates+alcohol'
regression_result = ols(Rformula, data=wine).fit()

# ■ 회귀분석모델로 샘플의 등급 예측하기
sample1 = wine[wine.columns.difference(['quality','type'])]
sample1 = sample1[0:5][:] # ▶ 4번 인덱스 까지
print(sample1.head())

sample1_predict = regression_result.predict(sample1)
print(sample1_predict)
print(wine[0:5]['quality'])

# 새로운 데이터 적용
data = {'fixed_acidity' : [8.5,8.1],
        'volatile_acidity' : [0.8 , 0.5],
        'citric_acid' : [0.3,0.4],
        'residual_sugar' : [6.1,5.8],
        'chlorides' : [0.055,0.04],
        'free_sulfur_dioxide': [30.0, 31.0],
        'total_sulfur_dioxid': [98.0,99],
        'densit': [0.996,0.91],
        'pH': [3.25,3.01],
        'sulphates': [0.4,0.35],
        'alcoho': [9.0, 0.88]
        } #▶각 속성에 해당되는 값을 다 줘야하니까

sample2=pd.DataFrame(data, columns=sample1.columns)
sample2_predict = regression_result.predict(sample2)
print(sample2_predict)