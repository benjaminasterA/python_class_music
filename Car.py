"""    
# Car 클래스 선언
# 클래스 이름은 주로 대문자로 사용
class Car:
    pass

# 힙에 생성된 Car객체를 스택의 my_car 변수가 참조
my_car = Car()
"""

# 생성자: 객체가 만들어질때 자동으로 실행되는 메서드
# 사용자가 선언하지 않아도 기본 생성자는 자동 추가 됨.
class Car :
    # 생성자 이름은 정해져 있다.
    # 클래스 내부의 멤버함수는 반드시 self를 선한다.
    # self 클래스로 생성한 객체 자신이다.
    # 멤버 메서드끼리 멤버 필드를 공유한다. 
    def __init__(self, name, price):
        self.name = name
        self.price = price
    

    # self가 없다면 어떤 객체가 이 메서드를 호출 했는지 알수 없다.
    def audio(self):
        print(self.name, "에서 음악을 듣는다.")
    
    
my_car = Car("Sonata", 3000)
my_car.audio()

your_car = Car("K7", 3500)
your_car.audio()