import random as rd

List_Rnd = [rd.randint(1,100) for _ in range(100)]

#print(List_Rnd)

#파일 경로
File_Fath = (r"C:\data\os1.txt")

#'w' 모드로 파일을 열어서
with open(File_Fath, "w") as f: #write
    #f.write(str(List_Rnd))

    #List_Rnd의 요소의 개수만큼 반복하면서
    for i in range(len(List_Rnd)):
        #i번째 요소를 작성
        f.write(f" {List_Rnd[i]}")
        #10 번째 요소를 작성하면 줄바꿈
        if i % 10 == 9 : f.write('\n')

#List_Rnd.sort()

#선택정렬
for i in range(len(List_Rnd)):
    for j in range(i+1, len(List_Rnd)):
        if List_Rnd[i] > List_Rnd[j]: List_Rnd[i], List_Rnd[j] = List_Rnd[j], List_Rnd[i]

#print(List_Rnd)

with open(File_Fath, "a") as f:
    f.write("결과\n")
    f.write("--------------------------------------------\n")
    f.write(f"최소값 : {List_Rnd[0]}\n")
    f.write(f"최대값 : {List_Rnd[99]}")

    f.write("\n")

    #List_Rnd의 요소의 개수만큼 반복하면서
    for i in range(len(List_Rnd)):
        #i번째 요소를 작성
        f.write(f" {List_Rnd[i]}")
        #10 번째 요소를 작성하면 줄바꿈
        if i % 10 == 9 : f.write('\n')