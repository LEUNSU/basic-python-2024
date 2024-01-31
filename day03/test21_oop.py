# file : test21_oop.py
# desc : 객체지향 클래스 만들기

# 클래스(사람이라는 객체를 만들기위한 청사진) 만들기
class Person:  # 사람 클래스 선언
    name = '' # 멤버변수
    age = 0
    gender = ''

    # 생성자 함수(스페셜 함수) 클래스의 객체를 생성할 때 동작
    # init == initialization(초기화)
    def __init__(self) -> None:
        self.name = '홍길순'
        self.age = 29
        self.gender = '남자'
    
    # 클래스를 호출할 때 원하는 형태로 변환해서 보여줄 때
    def __str__(self) -> str:
        strs = f'커스텀 출력, 이름: {self.name} 객체 생성!'
        return strs

    def walk(self): # 멤버함수 매개변수 self 필수!
        print(f'{self.name}이(가) 걷습니다.')

    def stop(self): 
        print(f'{self.name}이(가) 멈춥니다.')

# 사람 객체 생성, Instance(사례, 예제)
gd = Person()
es = Person()
# print(type(mg))
# print(id(mg)) # 다른 객체인지 확인
# print(id(es))
gd.name = '홍길동' # 객체명.멤버변수 = ...
gd.age = 47
gd.gender = '남자'

es.name = '이은수'
es.age = 26
es.gender = '여자'

print(f'gd => 이름:{gd.name} / 나이:{gd.age} / 성별:{gd.gender}')
print(f'es => 이름:{es.name} / 나이:{es.age} / 성별:{es.gender}')

gd.walk()
print('1분동안 걷습니다')
gd.stop()

es.walk()
print('걷는 것을 싫어합니다')
es.stop()
print('생성자 함수 추가 --------------> ')
gs = Person()
print(f'gs => 이름:{gs.name} / 나이:{gs.age} / 성별:{gs.gender}')
print(gs)