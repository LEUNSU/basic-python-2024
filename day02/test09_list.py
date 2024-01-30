# date : 20240130
# desc : 복합자료형 list
# s1 = 80
# s1 = 90
# s1 = 100
# s1 = 50
# s1 = 60 # 학생 수만큼 변수를 생성
# 총 갯수 10(n)면 인덱스의 마지막 값은 9(n-1)
# index= 0, 1,  2 , 3 , 4 , 5 , 6 , 7 , 8 ,  9 
#     -10, -9,  -8, -7, -6, -5, -4, -3, -2,  -1
std = [80, 90, 100, 50, 60, 55, 77, 88, 99, 100]
print(std[8]) # 리스트 요소 접근

list_1 = [265, 3.5, '문자열', True, [1,2,3,4], (3,4), std]
print(list_1)
print(list_1[5])

list_1[6] = "바꾼 값" # 원래 리스트가 문자열로 변경
print(list_1)

## 리스트 연산
print(list_1[2:3+1]) # 뒤의 수는 출력하고 싶은 인덱스+1이 필수
## 마이너스 인덱스
print(list_1[-7:-5])
##이중 리스트
print(list_1[4][2]) # [1,2,3,4] 중에서 두번째 인덱스만 가져오기

list_2 = [[1,2,3],[4,5,6],[7,8,9]]
print(list_2[1][2]) # 6

list_4 = [1,2,3]
list_5 = [7,8,9]
# list_3 = list_4 + list_5
## 리스트 연산 +, * 만 사용가능
print(list_4 + list_5) # + 는 리스트를 연결
print(list_5 * 2) # * 는 리스트를 반복

## 리스트 길이함수 len()
print(len(list_4))

## append() 리스트 마지막에 하나 추가
## insert(index, val) 리스트의 index 이후에 val 추가
print(list_1)
list_1.append('Hello!')
print(list_1)

list_1.insert(2,100) # 2번째 인덱스에 값을 추가(원래값은 뒤로 밀림)
print(list_1)

## extend() 기존 리스트 확장 : + 와 거의 유사
list_4.extend(list_5)
print(list_4) # [1,2,3,7,8,9]
print(list_5) # [7,8,9]

## 리스트 삭제
del list_4[3]
print(list_4)
del list_4  # 리스트 자체를 삭제
# print(list_4)

val = list_5.pop() # 마지막 값을 꺼내오기
print(val)
print(list_5) # [7,8]

print(std)
val = std.pop(2)
print(val)
print(std)

# clear()
list_5.clear() # del()은 완전삭제 print도 안됨, clear()는 내용만 삭제
print(list_5)

# sort()
print(list_1) 
# list_1.sort() # 문자열, 숫자, 불 섞여있는 리스트는 정렬 안됨
std.sort() # 오름차순 정렬
print(std)
std.sort(reverse=True) # 내림차순 정렬
print(std)

# in, not in
print(99 in std) # True
print(98 in std) # False

# reverse(), copy(), count()...
# * 리스트 : 전개연산자 - 몰라도 됨
list_a = [1,3,5]
list_b = [2,4,8]
list_c = [*list_a, *list_b]
print(list_c)

list_d = [list_a, list_b]
print(list_d)