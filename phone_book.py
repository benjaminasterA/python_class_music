# 클래스를 선언하면 새로운 데이터 타입이 만들어 지는것
class Phone :
    # 객체를 생성하면 자동 호출(초기화)
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        
    
    # 객체를 사용하면 자동 호출 (기본 __str__를 재정의 해서 사용한다)
    def __str__(self):
        # 여러 데이터를 return하면 Tuple 타입으로 반환 됨.
        return f"{self.name}, {self.phone}"
    

p1 = Phone("ppp", "010-555-6666")
# __str__ 함수가 자동 호출 됨
# print(p1 )

phone_book = [
    p1, 
    Phone("aaa", "010-1111-1111"),
    Phone("aaa", "010-1111-1112"), 
    Phone("aaa", "010-1111-3333")
]

# for p in phone_book:
#     if p.phone == "010-1111-1112":
#         print(p)

result = next((c for c in phone_book if c.phone == "010-1111-1112"))
print(result)
