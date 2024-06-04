import pandas as pd
wine = pd.read_csv('wine.csv')
print(wine.info())

# ■ 칼럼명 빈공간을 언더바로 리플레이스
wine.columns = wine.columns.str.replace(' ', '_')
# ■ 확인겸 출력
print(wine.head())

# ■ 통계기법
print(wine.describe())

print(sorted(wine.quality.unique()))
print(wine.quality.value_counts())


print(wine.groupby('type')['quality'].describe())

print(wine.groupby('type')['quality'].agg(['mean','std']))




