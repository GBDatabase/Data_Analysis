#워드 클라우드를 이용하여
# https://www.riss.kr/search/Search.do?isDetailSearch=N&searchGubun=true&viewYn=OP&queryText=&strQuery=big+data&exQuery=&exQueryText=&order=%2FDESC&onHanja=false&strSort=RANK&p_year1=&p_year2=&iStartCount=40&orderBy=&mat_type=&mat_subtype=&fulltext_kind=&t_gubun=&learning_type=&ccl_code=&inside_outside=&fric_yn=&db_type=&image_yn=&gubun=&kdc=&ttsUseYn=&l_sub_code=&fsearchMethod=search&sflag=1&isFDetailSearch=N&pageNumber=1&resultKeyword=big+data&fsearchSort=&fsearchOrder=&limiterList=&limiterListText=&facetList=&facetListText=&fsearchDB=&icate=re_a_over&colName=re_a_over&pageScale=10&isTab=Y&regnm=&dorg_storage=&language=&language_code=&clickKeyword=&relationKeyword=&query=big+data#redirect
# 티스토리 : https://highllight.tistory.com/28
import pandas as pd
import glob
import re
from functools import reduce
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import matplotlib.pyplot as plt
from wordcloud import STOPWORDS, WordCloud


all_files = glob.glob('myCabinetExcelData*.xls')
all_files   #출력하여 내용 확인
['myCabinetExcelData.xls',
 'myCabinetExcelData (1).xls',
 'myCabinetExcelData (2).xls',
 'myCabinetExcelData (3).xls',
 'myCabinetExcelData (4).xls']


all_files_data = []     #저장할 리스트
for file in all_files:
    data_frame = pd.read_excel(file)
    all_files_data.append(data_frame)
all_files_data[0]      #작업 내용 확인


all_files_data_concat = pd.concat(all_files_data, axis = 0, ignore_index = True)
all_files_data_concat #1,000개 데이터 출력하여 내용 확인


all_files_data_concat.to_csv('riss_bigdata.csv', encoding='utf-8-sig', index = False)

# 데이터 전처리
# 제목만 가져오기

all_title = all_files_data_concat['제목']
print(all_title)

#모듈 실행시 오류나는 경우 직접 다운로드
#mlfk = download('stopword')
#nltk.download('punkt')
#nltk.download('wordnet')

#nltk.courpus 에서 제공하는 영어 불용어
stopWords = set(stopwords.word('english'))

# 표제어 추출을 위한 객체 생성

lemma = WordNetLemmatizer()

#제목 추출 시작
words= []

#전체 ㅌ이틀을 하나씩 읽으면서 처리
for title in all_title:
    #정규식 규칙을 적용 => 영어단어가 아닌것을 제거
    EnWords = re.sub(r"[^a-zA-Z]+", " ")
    #대소문자 혼합 => 소문자 통일
    #각 단어를 토큰화
    EnWordsToken = word_tokenize(EnWords.lower())

    #불용어 제거를 람다식으로 함
    EnWordsTokenStop = [w for w in EnWordsToken if w not in EnWordsToken]

    #표제어 추출
    EnWordsTokenStopLemma = [lemma.lemmatize(w) for w in EnWordsTokenStop]

    #최종 결과 APPEND
    words.append(EnWordsTokenStopLemma)
#print(words)


#전처리가 끝난 2차원 데이터를 reduce()를 이용하여 1차원으로 변환

words2 = list(reduce(lambda x, y : x+y)) #두개로 되어있는 데이터 셋을 일차원으로 합해서 처리하겠다, 입력은 두개 이차원으로 되어있는 데이터를합해서 1차원으로 만들겠다는 의미
print(words2) #결과는 리스트

#데이터 탐색 - 단어의 빈도수 구하기
count = Counter(words2)
print(count)

#출현 횟수가 많은 상위 50개 단어만 추출
word_count = dict()

for tag, counts in count.most_common(50):
    if len(str(tag))>1: # 1번의 태그에다가 워드 데이터를 넣자 태그하고 카운트를 읽었다면
        word_count[tag] = counts #단어의 길이가 두 알파벳 이상인 것만 저장하겠다는 뜻
        print("%s : %d % (tag, counts")

#[시각화]최종 데이터 시각화
# x축 : 단어 , y축 : 단어의 빈도수
# x 레이블용
#sorted_Keys = sorted(word_count, key = word_count.get, reverse = True) #큰값이 먼저나오므로  reverse = True
# y 레이블용
#sorted_Values = sorted(word_count.values(), reverse = True) #value값만가지고 sorted
#plt.bar(range(len(word_count)), sorted_Values, align = 'center')
#plt.xticks(range(len(word_count)), list(sorted_Keys), rotation = '85')
#plt.show

del word_count['big']
del word_count['data']

#연도별 데이터 추이 시각화
all_files_data_concat['doc_count'] = 0
summary_year = all_files_data_concat.groupby('출판일', as_index = False).count()
print(summary_year)
#출판일을 기준으로 groupby

plt.figure(12,5)
plt.xlabel('year')
plt.ylabel('doc_count')
plt.grid(True)
plt.plot(range(len(summary_year))), summary_year['doc_count']
plt.xticks(range(len(summary_year)), [text for text in summary_year['출판일']])
plt.show()


#워드클라우드로 시각화
#워드클라우드에서 처리할 불용어 처리
stopwords = set(STOPWORDS)
wc = WordCloud(background_color='ivory', stopwords = stopwords , width = 800, height=600 )

#단어 출현 빈도수를 적용
cloud = wc.generate_from_frequencies(word_count) #빈도수를 기반으로 만들겟다
plt.figure(figsize=(8,8))
plt.imshow()
plt.axis('off')
plt.show()