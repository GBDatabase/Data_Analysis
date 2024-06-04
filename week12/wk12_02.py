from bs4 import BeautifulSoup
import urllib.request
import pandas as pd


#[CODE 1]
def hollys_store(result):
    for page in range(1,54):    # 1~54 페이지까지 검색
            # pageNo만 바뀌는 형태이므로 %d 에 page 값을 넣어줌

        #page=1
        Hollys_url = 'https://www.hollys.co.kr/store/korea/korStore2.do?pageNo=1&sido=&gugun=&store=' %page
        print(Hollys_url)
        #할리스 사이트 매장 정보 페이지 연결

        html = urllib.request.urlopen(Hollys_url)   # url 접근
        soupHollys = BeautifulSoup(html, 'html.parser')  # 해당 html 파싱
        #print(html)
        tag_tbody = soupHollys.find('tbody')    # tbody 태그 찾기


        for store in tag_tbody.find_all('tr'):  # tbody.tr 태그를 찾아 for 문 돌리기
            store_td = store.find_all('td')
            store_sido = store_td[0].string
            store_name = store_td[1].string
            if len(store) <= 3: # 그 수가 3 이하면 종료
                break
            store_td = store.find_all('td') # tbody.tr.td 태그 구하기
            store_sido = store_td[0].string #지역
            store_name = store_td[1].string #매장명
            store_address = store_td[3].string  #주소
            store_tel = store_td[5].string #전화번호

            result.append([store_name]+[store_sido]+[store_address]+[store_tel]) # 리스트에 추가
    print(result)
    hollys_tbl = pd.DataFrame(result, columns=['store', 'sido_gu', 'address', 'phone'])
    hollys_tbl.to_csv('hollys.csv',encoding="cp949", mode="W", index=True)

    return


















