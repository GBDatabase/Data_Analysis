
# 영유아가 가장 많은 동네는 어디일까?
# 영유아의 기준 : 만 3세 이하(0세 ~ 3세까지)
# 영유아가 가장 많은 동네가 어디인지 찾기
# 해당 동의 인구 구조를 그래프로 나타내기
#타이틀(목차? 1번줄은 next로 건너 뛰어야 함)
# 엑셀 파일에서
# 서울특별시 종로구 (1111  000000) ##0이 6개
# 서울특별시 종로구 청운효자동(1111  051500) ##동은 0이 6개 일수가 없다는 사실을 토대로 코드를 짜야함.

import csv
import matplotlib.pyplot as plt

filename = 'age.csv'

# 각 동네의 영유아 인구수 합계를 저장할 딕셔너리 생성
child_populations = {}

# CSV 파일을 열어 데이터를 읽어옴
with open(filename, 'r', encoding='utf-8') as f:
    data = csv.reader(f)
    next(data)  # 헤더 제거
    for row in data:
        town = row[0]  # 동네 이름
        child_population = sum(map(int, row[3:7]))  # 0세부터 3세까지의 인구수 합계
        child_populations[town] = child_population

# 영유아 인구수가 가장 많은 동네 찾기
most_child_town = max(child_populations, key=child_populations.get)
most_child_population = child_populations[most_child_town]

# 그래프 그리기
plt.figure(figsize=(10, 6))
plt.bar(child_populations.keys(), child_populations.values(), color='skyblue')
plt.xlabel('동네')
plt.ylabel('영유아 인구수')
plt.title('각 동네의 영유아 인구수')
plt.xticks(rotation=90)  # x축 라벨 회전
plt.tight_layout()
plt.show()

# 결과 출력
print(f"영유아가 가장 많은 동네는 '{most_child_town}'이며, 해당 동네의 영유아 인구수는 {most_child_population}명입니다.")
