# date : 20240130
# desc : 여러조건 if문

date = input('날짜 입력(예: 12-31) >') # '12-31'문자열 01-01, 12-01

month = date.split('-')[0] # '12' 
day = date.split('-')[1] # '31'

if month == '12' and day == '25': # 12월 25일
    print('Merry Christmas!')
elif month == '1' and day == '1': # 1월 1일
    print('Happy New Year!')
elif month == '04' and day == '14': # 4월 14일
    print('짜장면 먹어!')
else:
    print('보통날입니다')