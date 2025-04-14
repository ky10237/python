import random as rd
import pandas as pd

ListA=[rd.randint(1,100) for _ in range(10)]
ListB=[rd.randint(1,100) for _ in range(10)]
ListC=[rd.randint(1,100) for _ in range(10)]
ListD=[rd.randint(1,100) for _ in range(10)]
ListE=[rd.randint(1,100) for _ in range(10)]
ListF=[rd.randint(1,100) for _ in range(10)]
ListG=[rd.randint(1,100) for _ in range(10)]
ListH=[rd.randint(1,100) for _ in range(10)]
ListI=[rd.randint(1,100) for _ in range(10)]
ListJ=[rd.randint(1,100) for _ in range(10)]

SerA=pd.Series(ListA)
SerB=pd.Series(ListB)
SerC=pd.Series(ListC)
SerD=pd.Series(ListD)
SerE=pd.Series(ListE)
SerF=pd.Series(ListF)
SerG=pd.Series(ListG)
SerH=pd.Series(ListH)
SerI=pd.Series(ListI)
SerJ=pd.Series(ListJ)


#시리즈를 1차원 배열에 넣음
List_Ser=[SerA,SerB,SerC,SerD,SerE,SerF,SerG,SerH,SerI,SerJ]

#0 ~ 9까지
for i in range(len(List_Ser)):
    #i+1 ~ 9까지
    for j in range(i+1,len(List_Ser)):
        #요소의 합이 뒤에 있는 요소보다 크면
        if(List_Ser[i].sum() > List_Ser[j].sum()):
            #자리바꿈
            List_Ser[i], List_Ser[j] = List_Ser[j], List_Ser[i]

#출력
for i in List_Ser:
    print(i.sum(), end=" ")

