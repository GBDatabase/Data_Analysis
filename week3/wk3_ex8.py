st1 = {'학번':20210646, '이름':'문가빈','학과':'소프트웨어공학과'}

print(st1)

st1['연락처'] = 010-0202-2020
print(st1)

st1['학과'] = '데이터분석과'
print(st1)

del(st1['연락처'])
print(st1)
st1.clear()
print(st1)
st1['학번'] = 230101
print(st1)

st2 ={'학번': 2023001, '이름':'홍길동' ,'학번':2023002}
print(st2)
print(st2['학번'])
print(st2['이름'])
print(st2.get('이름'))