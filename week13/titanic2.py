import pandas as pd
import matplotlib.pyplot as plt

titanic = pd.read_csv('titanic.csv')

# 결측값이 있는 속성 확인
# print(titanic.isnull().sum())

#결측치를 어떻게 할것인지 에 대해서
#age 결측치 : 중앙값으로 치환

titanic['age'] = titanic['age'].fillna(titanic['age'].median())
# ■ 비어있는 감에 대해서 함
#bprint(titanic.isnull().sum())

# embarked
print(titanic['embarked'].value_counts())
titanic['embarked'] = titanic['embarked'].fillna('S')
# print(titanic.isnull().sum())



print(titanic['embark_town'].value_counts())
titanic['embark_town'] = titanic['embarked'].fillna('T')
#print(titanic.isnull().sum())

print(titanic['embark_town'].value_counts())
titanic['embark_town'] = titanic['embark_town'].fillna('southampton')
#print(titanic.isnull().sum())

print(titanic['deck'].value_counts())
titanic['deck'] = titanic['deck'].fillna('C')

print('------')
print((titanic.info()))
#print(titanic.isnull().sum())


#파이 차트로 시각화(성별, 생존, 비율)
#f, ax = plt.subplots(1,2,figsize=(10,5)) #가로 10인치, 세로 5인치
#titanic['survived'][titanic['sex']=='male'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%',ax=ax[0],shadow=True) #몇명이나 survived 했는지 가져옴
#titanic['survived'][titanic['sex']=='female'].value_counts().plot.pie(explode=[0,0.1], autopct='%1.1f%%',ax=ax[1],shadow=True) #여자에 대해서 female로 바꾸고 ax도 1번값으로 바꿈
#ax[0].set_title('survived (Male)')
#ax[1].set_title('survived (Femaile)')


#등급별 생존자수를 파이차트로 시각화
#sns.count(x = 'pclass', hue='survived', data=titanic)
#plt.title('Pclass vs Survived')


#plt.show()

#상관분석
titanic2 = titanic[titanic.columns.difference(['sex','age', 'embarked', 'embark_town', 'class', 'who','deck','alive'])]
titanic_corr = titanic.corr(method='pearson')
print(titanic_corr)