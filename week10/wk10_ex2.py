import os
import sys
import urllib.request
import datetime
import time
import json

client_id = '1zZpXmo_m7aeI_L2vflT'
client_secret = 'qln_1XvMJe'

def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


def getNaverSearch(node, srcText, start, display):
    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % node
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(srcText), start, display)

    url = base + node + parameters
    responseDecode = getRequestUrl(url)  # [CODE 1]

    if (responseDecode == None):
        return None
    else:
        return json.loads(responseDecode)



def getPostData(post, jsonResult, cnt):
    title = post['title']
    description = post['description']
    bloggerlink = post['bloggerlink']
    link = post['link']
    bloggername = post ['bloggername']

    # pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900') #9시간 차이나니까...
    # pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'cnt': cnt, 'title': title, 'description': description,
                        'blogger_link': bloggerlink, 'bloggername': bloggername})
    return




# [CODE 0]
def main():
    node = 'blog'  # 크롤링 할 대상
    srcText = input('검색어를 입력하세요: ') #source text
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)  # [CODE 2]
    total = jsonResponse['total']

    while ((jsonResponse != None) and (jsonResponse['display'] != 0)):
        for post in jsonResponse['items']:
            cnt += 1
            getPostData(post, jsonResult, cnt)  # [CODE 3]

        start = jsonResponse['start'] + jsonResponse['display']
        jsonResponse = getNaverSearch(node, srcText, start, 100)  # [CODE 2]

    print('전체 검색 : %d 건' % total)

    with open('%s_naver_%s.json' % (srcText, node), 'w', encoding='utf8') as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(jsonFile)

    print("가져온 데이터 : %d 건" % (cnt))
    print('%s_naver_%s.json SAVED' % (srcText, node))


if __name__ == '__main__':
    main()
