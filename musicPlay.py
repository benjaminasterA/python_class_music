# (pip install typing) - 리스트(List) 타입 힌트(Type Hint) 활용을 위해 임포트함
from typing import List

# (Python help: 클래스(class)는 데이터와 기능을 하나로 묶는 객체의 설계도입니다)
class Music:
    # (English notation: Constructor) (Korean pronunciation: 컨스트럭터)
    # 인스턴스화 시 속성(Attribute)을 초기화하여 객체의 상태(State)를 설정함
    def __init__(self, singer: str, song: str):
        # (English notation: Instance Variable) (Korean pronunciation: 인스턴스 베리어블)
        # 가수(singer) 정보를 현재 인스턴스(self)의 메모리 공간에 바인딩함
        self.singer = singer
        # 노래(song) 정보를 현재 인스턴스(self)의 메모리 공간에 바인딩함
        self.song = song
        
    # (Python help: 인스턴스 메서드는 첫 번째 인자로 self를 받아 객체 내부 데이터에 접근함)
    # 객체의 고유한 행위(Behavior)를 정의하며 캡슐화된 속성을 활용해 메시지를 출력함
    def play(self):
        # (English notation: f-string) (Korean pronunciation: 에프스트링)
        # 문자열 포맷팅을 통해 런타임에 가수와 곡명을 동적으로 보간하여 출력함
        print(f"{self.singer}의 {self.song}를 실행중 ...")

    # (Python help: __str__ 메서드는 객체의 가독성 있는 문자열 표현을 정의할 때 사용함)
    # print() 호출 시 내부적으로 호출되는 던더(Dunder) 메서드로 객체 정보를 반환함
    def __str__(self) -> str:
        # 객체의 현재 상태를 문자열 형태로 직렬화하여 반환함으로써 디버깅 편의성을 높임
        return f"{self.singer}의 {self.song}를 실행중 ..."


# (Python help: MusicPlayer는 Music 인스턴스들을 관리하는 오케스트레이터 역할을 수행함)
class MusicPlayer:
    # (English notation: Initialization) (Korean pronunciation: 이니셜라이제이션)
    # 플레이어 생성 시 빈 음악 목록을 초기화하며 타입 안정성을 위해 List[Music]을 명시함
    def __init__(self, music_list: List[Music] = []):
        # (English notation: Member Field) (Korean pronunciation: 멤버 필드)
        # 플레이어가 제어할 대상인 음악 객체들의 집합을 내부 변수에 할당함
        print(music_list,"ggg")
        self.music_list: List[Music] = music_list
        print(self.music_list,"fff")

    # (English notation: Setter Method) (Korean pronunciation: 세터 메서드)
    # 외부에서 완성된 의존성(Dependency)인 리스트를 주입받는 통로 역할을 수행함
    def setList(self, music_list: List[Music]):
        # 외부에서 전달받은 참조(Reference)를 내부 멤버 변수에 연결함
        self.music_list = music_list
        
    # (Python help: iterable 객체를 순회하기 위해 for 반복문(loop)을 사용함)
    # 리스트 내의 각 객체에게 메시지를 전송하여 다형성(Polymorphism)을 실현함
    def play(self):
        # (English notation: Iteration) (Korean pronunciation: 이터레이션)
        # 관리 중인 음악 리스트를 순회하며 각 요소인 Music 인스턴스를 하나씩 꺼냄
        for music in self.music_list:
            # (English notation: Method Delegation) (Korean pronunciation: 메서드 델리게이션)
            # 재생의 실제 책임은 Music 객체에게 위임하여 각 객체가 스스로 동작하게 함
            music.play()
        

# (English notation: Data List) (Korean pronunciation: 데이터 리스트)
# 리터럴(Literal)을 사용하여 Music 클래스의 인스턴스들로 구성된 배열을 생성함
music_list: List[Music] = [
    Music("조용필", "창밖의 여자"),
    Music("이선희", "아~ 옛날이여"),
    Music("악동뮤지션", "바람의 노래")
]

# (English notation: Instantiation) (Korean pronunciation: 인스턴스화)
# MusicPlayer 타입(Type)의 객체를 메모리에 생성하고 참조 변수 player에 할당함
player: MusicPlayer = MusicPlayer()
# 생성된 플레이어 객체에 준비된 음악 목록(Dependency)을 주입(Injection)함
player.setList(music_list)
# 플레이어의 play 메서드를 호출하여 전체 음악 재생 로직을 실행함
player.play()

# 콜론(:) 뒤에 타입 지정 가능
# 클래스는 새로운 타입이다.
print(player, "ddd")
player: MusicPlayer = MusicPlayer()
print(player, "aaa")
player.setList(music_list)
print(player.setList,"bbb")
player.play()
print(player.play(),"ccc")

# 클래스의 디자인 패턴
# Gof의 디자인 패턴
# 템플릿메서드 패턴, 전략 패턴
# 의존성 주입, 제어의 역전(IoC 패턴)
# 일반적인 프레임워크의 핵심 패턴