#tourist.py
import os
import sys
import urllib.request
import datetime
import time
import json
import pandas as pd

ServiceKey = "kCi6%2Fv%2BPShbuY0bTvM2q%2Ff9V0RunKTIp0OhOHtNckMcMpOJZ1yzhz4UgT28Xq663%2Fv95XvgzekR2eyz1sWe6PA%3D%3D"

#입국자국가,국가코드,입국년월,입국자수
# 1. url 접속을 요청하고 응답을 받아서 반환
def getRequestUrl(url):
    req = urllib.request.Request(url)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# 2. openApi를 사용하여, 데이터 요청 url을 구성해서 요청
def getTourismStatsItem(yyyymm, national_code, ed_cd):
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=json&serviceKey=" + ServiceKey  # 인증키
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + national_code
    parameters += "&ED_CD=" + ed_cd

    url = service_url + parameters
    print(url)

    responseDecode = getRequestUrl(url)  #제대로 받았는지 확인
    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode) #서버에서 받은 json 형태의 응답객체를
                                          #파이썬에서 처리할 수 있는 객체로 로드해서 반환


# 3. 데이터 수집기간동안 월 단위로 데이터 요청
def getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear): #입력받은 년도로 월 단위 데이터 요청
    jsonResult = []
    result = [] #result 데이터도 리스트 형태로 저장

    natName = ''    # 국가코드
    dataEND = "{0}{1:0>2}".format(str(nEndYear), str(12)) #마지막 데이터 엔드는 str값으로 endyear해주고 최종적으로 str값으로 12를 주자
    isDataEnd = 0  #끝 연도

    for year in range(nStartYear, nEndYear + 1):
        for month in range(1, 13):
            if (isDataEnd == 1): break
            yyyymm = "{0}{1:0>2}".format(str(year), str(month)) #{} 포맷으로 만들어 주는법, 0번 인덱스, 1번 인덱스, YEAR을 스트링으로 바꿔 넣어줘야함. 두자리로 포맷 정해주기:두자리의 헤딩을 주는데 0으로 채울거고 1월부터 9월까지 오른쪽 2자리 정렬 201701 이렇게

            jsonData = getTourismStatsItem(yyyymm, nat_cd, ed_cd)  # [CODE 2]
            print((jsonData['response'],['header'],['resltMsg']))
            print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False))


            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                if jsonData['response']['body']['items'] == '':
                    isDataEnd = 1
                    dataEND = "{0}{1:0>2}".format(str(year), str(month - 1))
                    # print("데이터 없음.... \n 제공되는 통계 데이터는 %s년 %s월까지입니다." % (str(year), str(month - 1)))
                    # break

                print(json.dumps(jsonData, indent=4, sort_keys=True, ensure_ascii=False))

                natName = jsonData['response']['body']['items']['item']['natKorNm']
                natName = natName.replace(' ', '') #netname.replace(' ', '') #한칸 띄워진것, 빈공간 없애기
                num = jsonData['response']['body']['items']['item']['num']
                ed = jsonData['response']['body']['items']['item']['ed']

                print('[%s_%s:%s ]' % (natName, yyyymm, num)) # json
                print('---------------------------------------------')
                jsonResult.append({'nat_name': natName,
                                    'nat_cd': nat_cd,
                                    'yyyymm': yyyymm,
                                    'visit_cnt': num})

                result.append([natName, nat_cd, yyyymm, num]) #csv

    return (jsonResult, result, natName, ed, dataEND)


# [CODE 0]
def main():
    jsonResult = [] #값을 받기위해서 선언해주고
    result = []

    print("<<국내 입국한 외국인의 통계 데이터를 수집합니다>>")
    nat_cd = input('국가 코드를 입력하세요 (중국:112 / 일본:130 / 미국:275) >> ')
    nStartYear = int(input('데이터를 몇 년부터 수집할까요?:'))
    nEndYear = int(input('데이터를 몇 년까지 수집할까요?>> '))
    ed_cd = "E"     # E : 방한외래관광객, D : 해외 출국

    #getTourismStatsService(nat_cd,ed_cd,nStartYear,nEndYear)
    jsonResult, result, natName, ed, dateEnd = getTourismStatsService(nat_cd, ed_cd, nStartYear, nEndYear)


    # 파일 저장 1 :json 파일
    with open('./%s_%s_%d_%s.json' % (natName, ed, nStartYear, dataEND), 'w',
               encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)
        outfile.write(jsonFile)
    # 파일 저장 2 : csv 파일
    columns = ["입국자국가", "국가코드", "입국연월", "입국자 수"]
    result_df = pd.DataFrame(result, columns=columns) # pandas 이용해서 위에있는 컬럼
    result_df.to_csv('./%s_%s_%d_%s.csv' % (natName, ed, nStartYear, dataEND), #나라이름 나라연도 월 일
                     index=False, encoding='cp949')


if __name__ == '__main__':
    main()
