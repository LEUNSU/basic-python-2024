# file : test19_starprint.py
# desc : 별 찍기 또는 피라미드 만들기
# *
# **
# ***
# ****
# *****

for i in range(1, 5+1):
    # 첫번째 i가 1이면, range(1,2) 1번 반복
    # i가 2이면, range(1,3) 2번 반복
    for j in range(1, 5-i+1): # range() 값 바꿔서 디버깅
        print(' ', end='') # 엔터 대신 empty로 변환
    
    for j in range(1, i+1):
        print('*', end='')
    print() # 안 쪽 for문이 끝나면 엔터