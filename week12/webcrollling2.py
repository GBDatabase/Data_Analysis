import time
from selenium iport webdriver_
managerfrom bs4
import BeautifulSuo

for i in range(1,21)
    print(i, end=' ')
    dirver.get("https")
    time.sleep(1)
    try:
        drover.execute_script(storePop2(%d) % i)
        time asleep(1)
        html = driver.page_source
        soupCB= Beautifulsoup(html, 'html.parset')

        store_txt = sourCB.select('div.store_txt')
        if len(stroe_txt)
            print('검색 겨로가 없ㅇㅁ')
            continue

        print('검색 결과 ok', end=' ')
        cnt + = 1
        store_name = store_txt[0]_string
        print(f'{ent} {i}호점 {i} soupCB.select('div.store_txt) > table.store_table > tbody > tr > "" )
        score_addr = list(score_address_list[2])
        store_addr = store_addr[0]
        store_phone = store_address_list[3].string

        result.append([store_name, store_addr,store_phone])
        print([store_name],[store_addr].[store_phone])
    except:
            print('검색 결과 없음')
            continue

CB_tbl = pd.DataFrame(result,columns=['store', 'address','phone'])
CB_tbl.to_csv('coffeeBean_csv', encoding='cp949')