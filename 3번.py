#pandas 라는 라이브러리를 불러와서 pd라는 변수로 호출함
import pandas as pd
#랜덤수를 뽑기위해 random 라이브러리를 불러옴
import random

from numpy.ma.extras import average

#pandas 라이브러리를 사용해 엑셀에 있는 데이터 프레임을 불러옴
pd_Dataset = pd.read_csv('D:\Python\Sample_CSV\Pandas_Sample.csv')
DF = pd.DataFrame(pd_Dataset)

pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)


# 랜덤수를 만들어서 변수에 지정
A = random.randint(1,100)
B = random.randint(1,100)
C = random.randint(1,100)
D = random.randint(1,100)
E = random.randint(1,100)
F = random.randint(1,100)

#칼럼에 있는 내용을 변수에 지정

X1 = DF['X1']
X2 = DF['X2']
X3 = DF['X3']
X4 = DF['X4']
X5 = DF['X5']
Y1 = DF['Y1']

#시작지점과 끝지점을 구분해서 범위 출력(다른 범위도 반복)
ST1 = min(A,B)
EN1 = max(A,B)
Range_X1 = X1[ST1:EN1]
ave_X1 = round(average(Range_X1))

print(f"X1범위 {ST1}~{EN1}의 평균:{ave_X1}\n")

ST2 =min(A,B)
EN2 =max(A,B)
Range_X2 =X2[ST2:EN2]
ave_X2 =round(average(Range_X2))

print(f"X2범위 {ST2}~{EN2}의 평균:{ave_X2}\n")

ST3 =min(A,B)
EN3 =max(A,B)
Range_X3 =X2[ST3:EN3]
ave_X3 =round(average(Range_X3))

print(f"X3의 범위 {ST3}~{EN3}의 평균:{ave_X3}\n")

ST4 =min(A,B)
EN4 =max(A,B)
Range_X4 =X4[ST4:EN4]
ave_X4 =round(average(Range_X4))

print(f"X4의 범위 {ST4}~{EN4}의 평균:{ave_X4}\n")

ST5 =min(A,B)
EN5 =max(A,B)
Range_X5 =X5[ST5:EN5]
ave_X5 =round(average(Range_X5))

print(f"X5의 범위 {ST5}~{EN5}의 평균:{ave_X5}\n")

ST6 =min(A,B)
EN6 =max(A,B)
Range_Y1 =Y1[ST6:EN6]
ave_Y1 =round(average(Range_Y1))

print(f"X6의 범위 {ST6}~{EN6}의 평균:{ave_Y1}\n")