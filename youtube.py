from googleapiclient.discovery import build
import pandas as pd
from collections import Counter
import re
import matplotlib.pyplot as plt

# 한글 글꼴 설정
plt.rcParams['font.family'] = 'Malgun Gothic'  # '맑은 고딕' 글꼴 사용
plt.rcParams['axes.unicode_minus'] = False  # 마이너스 기호 깨짐 방지

# [STEP 1] YouTube API를 사용하여 데이터 수집
API_KEY = '나의 API키'  # 자신의 유효한 API 키를 입력
CHANNEL_ID = 'UCUj6rrhMTR9pipbAWBAMvUQ'  # 분석할 채널의 ID를 입력

# YouTube API 클라이언트 빌드
youtube = build('youtube', 'v3', developerKey=API_KEY)

# 활동 데이터 수집 함수 정의
def get_all_activities(api_key, channel_id):
    youtube = build('youtube', 'v3', developerKey=api_key)
    activities = []
    next_page_token = None

    while True:
        request = youtube.activities().list(
            part='snippet,contentDetails',
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page_token
        )
        response = request.execute()
        activities.extend(response['items'])

        next_page_token = response.get('nextPageToken')
        if not next_page_token:
            break

    return activities

# 데이터 수집
all_activities = get_all_activities(API_KEY, CHANNEL_ID)

# [STEP 2] 수집한 데이터를 데이터프레임으로 정리
activities = all_activities  # 수집한 활동 데이터
activity_data = []

for activity in activities:
    snippet = activity['snippet']  # 활동의 기본 정보
    content_details = activity['contentDetails']  # 활동의 콘텐츠 세부 정보

    activity_info = {
        'publishedAt': snippet['publishedAt'],  # 활동이 발생한 시간
        'title': snippet['title'],  # 활동과 관련된 제목
        'description': snippet['description'],  # 활동과 관련된 설명
        'type': snippet['type'],  # 활동의 유형
        'videoId': content_details.get('upload', {}).get('videoId', ''),  # 업로드된 동영상 ID
        'likeVideoId': content_details.get('like', {}).get('resourceId', {}).get('videoId', ''),  # 좋아요를 받은 동영상 ID
        'commentVideoId': content_details.get('comment', {}).get('resourceId', {}).get('videoId', '')  # 댓글이 달린 동영상 ID
    }
    activity_data.append(activity_info)  # 활동 정보를 리스트에 추가

df = pd.DataFrame(activity_data)  # 리스트를 데이터프레임으로 변환

# 댓글 데이터 확인
print(df[['commentVideoId', 'title']].drop_duplicates())

# 결측치 확인
print("결측치 확인:")
print(df.isnull().sum())

# 이상치 확인을 위한 통계 요약
print("통계 요약:")
print(df.describe())

# 상자 그림을 통한 이상치 시각화
for column in ['videoId', 'likeVideoId', 'commentVideoId']:  # 이상치를 확인할 수치형 컬럼 리스트
    plt.figure(figsize=(10, 6))
    df[column].value_counts().plot(kind='box')
    plt.title(f'Box plot for {column}')
    plt.show()

# [STEP 3] 트렌드 분석
# 동영상 업로드, 좋아요, 댓글이 달린 동영상의 빈도 계산
video_trend = df[['videoId', 'title']].drop_duplicates().set_index('videoId')
video_trend['upload_count'] = df['videoId'].value_counts()
video_trend['like_count'] = df['likeVideoId'].value_counts()
video_trend['comment_count'] = df['commentVideoId'].value_counts()

# 상위 10개 데이터 선택
top_uploads = video_trend.sort_values('upload_count', ascending=False).head(10)
top_likes = video_trend.sort_values('like_count', ascending=False).head(10)
top_comments = video_trend.sort_values('comment_count', ascending=False).head(10)

print("최다 업로드는 :")
print(top_uploads)

print("최다 좋아요는 :")
print(top_likes)

print("최다 댓글은? :")
print(top_comments)

# 트렌드 데이터를 개별적으로 시각화
fig, ax = plt.subplots(3, 1, figsize=(14, 15))

# 업로드 트렌드
top_uploads['upload_count'].plot(kind='bar', ax=ax[0], color='blue')
ax[0].set_title('다시보기 top 10 ')
ax[0].set_xlabel('비디오 이름')
ax[0].set_ylabel('갯수')
ax[0].set_xticklabels(top_uploads['title'], rotation=45, ha='right')

# 좋아요 트렌드
top_likes['like_count'].plot(kind='bar', ax=ax[1], color='orange')
ax[1].set_title('좋아요를 많이 받은 top10')
ax[1].set_xlabel('동영상 이름')
ax[1].set_ylabel('갯수')
ax[1].set_xticklabels(top_likes['title'], rotation=45, ha='right')

# 댓글 트렌드
top_comments['comment_count'].plot(kind='bar', ax=ax[2], color='green')
ax[2].set_title('댓글이 가장 많이 달린 동영상 top 10 ')
ax[2].set_xlabel('동영상 이름')
ax[2].set_ylabel('갯수')
ax[2].set_xticklabels(top_comments['title'], rotation=45, ha='right')

plt.tight_layout(pad=2.0)
plt.show()

# [STEP 4] 시청자가 많이 보는 시간대 분석
# 데이터 프레임의 'publishedAt' 컬럼을 datetime 형식으로 변환
df['publishedAt'] = pd.to_datetime(df['publishedAt'])  # 문자열 형식을 datetime 형식으로 변환
df['hour'] = df['publishedAt'].dt.hour  # 활동이 발생한 시간대 추출

# 시간대별 조회수 분석
hourly_views = df['hour'].value_counts().sort_index()  # 시간대별 활동 빈도 계산

# 시각화
hourly_views.plot(kind='bar', figsize=(14, 7))  # 막대 그래프로 시각화
plt.title('시간 당 업로드')  # 그래프 제목
plt.xlabel('하루의 시간 ')  # x축 라벨
plt.ylabel('업로드 갯수')  # y축 라벨
plt.xticks(range(0, 24))  # x축 눈금 설정
plt.show()  # 그래프 표시

# [STEP 5] 시청자가 많이 댓글을 다는 동영상 유형 및 시간대 분석
# 시간대별 댓글 수 분석
comment_hourly = df[df['commentVideoId'] != ''].groupby('hour').size()  # 댓글이 달린 동영상의 시간대별 빈도 계산

# 데이터가 비어 있지 않은 경우에만 시각화
if not comment_hourly.empty:
    plt.figure(figsize=(14, 7))  # 그래프 크기 설정
    bars = plt.bar(comment_hourly.index, comment_hourly.values, color='#1f77b4')  # 막대 그래프로 시각화

    # 그래프 제목과 라벨 설정
    plt.title('시간당 코멘트', fontsize=16, fontweight='bold')
    plt.xlabel('시간', fontsize=14)
    plt.ylabel('코멘트 갯수', fontsize=14)

    # y축 눈금 설정
    plt.yticks(fontsize=12)

    # x축 눈금 설정
    plt.xticks(range(0, 24), fontsize=12)

    # 막대 위에 값 표시
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom', fontsize=10,
                 fontweight='bold')

    # 그리드 추가
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # 레이아웃 조정
    plt.tight_layout()

    # 그래프 표시
    plt.show()
else:
    print("No comments data available for plotting.")

# [STEP 6] 시청자가 자주 공유하는 동영상 및 공유된 플랫폼 분석
# 예시로 가상의 소셜 미디어 공유 데이터를 포함
video_shares = [
    {'videoId': 'VIDEO_ID_1', 'platform': 'Facebook', 'shares': 120},
    {'videoId': 'VIDEO_ID_2', 'platform': 'Twitter', 'shares': 75},
    {'videoId': 'VIDEO_ID_3', 'platform': 'Facebook', 'shares': 60},
    {'videoId': 'VIDEO_ID_4', 'platform': 'Twitter', 'shares': 95}
]

df_shares = pd.DataFrame(video_shares)

# 플랫폼별 공유 횟수 분석
platform_shares = df_shares.groupby('platform')['shares'].sum().reset_index()

# 시각화
plt.figure(figsize=(10, 6))  # 그래프 크기 설정
colors = ['#1f77b4', '#ff7f0e']  # 색상 지정
bars = plt.bar(platform_shares['platform'], platform_shares['shares'], color=colors)

# 그래프 제목과 라벨 설정
plt.title('플랫폼별 공유 수', fontsize=16, fontweight='bold')
plt.xlabel('플랫폼', fontsize=14)
plt.ylabel('공유 수', fontsize=14)

# y축 눈금 설정
plt.yticks(fontsize=12)

# 막대 위에 값 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom', fontsize=12, fontweight='bold')

# 그리드 추가
plt.grid(axis='y', linestyle='--', alpha=0.7)

# 레이아웃 조정
plt.tight_layout()

# 그래프 표시
plt.show()

# [STEP 7] 분석 결과 시각화
# 제목과 설명의 상위 단어 시각화
title_words = Counter()
description_words = Counter()

for _, row in df.iterrows():
    title_words.update(re.findall(r'\w+', row['title'].lower()))
    description_words.update(re.findall(r'\w+', row['description'].lower()))

# 가장 많이 언급된 단어 10개 추출
top_title_words = title_words.most_common(10)
top_description_words = description_words.most_common(10)

# 제목의 상위 단어 시각화
words, counts = zip(*top_title_words)  # 단어와 빈도 추출
plt.figure(figsize=(14, 7))  # 그래프 크기 설정
bars = plt.bar(words, counts, color='#1f77b4')  # 막대 그래프로 시각화
plt.title('제목 단어 Top 10', fontsize=16, fontweight='bold')  # 그래프 제목
plt.xlabel('단어들', fontsize=14)  # x축 라벨
plt.ylabel('빈도수', fontsize=14)  # y축 라벨

# 막대 위에 값 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.show()

# 설명의 상위 단어 시각화
words, counts = zip(*top_description_words)  # 단어와 빈도 추출
plt.figure(figsize=(14, 7))  # 그래프 크기 설정
bars = plt.bar(words, counts, color='#ff7f0e')  # 막대 그래프로 시각화
plt.title('Top 10 설명 단어', fontsize=16, fontweight='bold')  # 그래프 제목
plt.xlabel('단어들', fontsize=14)  # x축 라벨
plt.ylabel('빈도수', fontsize=14)  # y축 라벨

# 막대 위에 값 표시
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width() / 2.0, height, '%d' % int(height), ha='center', va='bottom', fontsize=12, fontweight='bold')

plt.show()

