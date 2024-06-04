

kor = [49 ,79 ,20 ,100, 80]
math =[43 ,59 ,85 ,30, 90]
eng =[49 ,79 ,68, 60, 100]

#2차원 리스트를 만드시오
midterm_score = [kor,math,eng]
print(midterm_score)

total = midterm_score[0][1]+midterm_score[1][0]+midterm_score[2][0]
ave = total / 3


#sum = kor[0]+math[0]+eng[0]
print(f'A 학생의 총점은 {total} 이고,평균은 {ave:.2f} 입니다.')

