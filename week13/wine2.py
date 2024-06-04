import pandas as pd
red_df = pd.read_csv('wine_red.csv')
white_df = pd.read_csv('wine_red.csv')
print(red_df.head())

# ■ 합치기
red_df.insert(0,column='type',value='red')
print(red_df.head())

# ▶ 컬럼은 이름이 같아야함
white_df.insert(0,column='type',value='white')
print(white_df.head())

print(red_df.shape)
print(white_df.shape)

# ■ 두 데이터 병합 => pd.concat()
# 병합할 데이터를 리스트 안에 넣어줍니다.
wine = pd.concat([red_df,white_df])
print('whine.shape')

#csv 파일로 저장
wine.to_csv('wine.csv', index=False)