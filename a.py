# (pip install - 표준 문법이므로 별도 설치 불필요)
# (Python help: 함수 주석(Annotation)은 런타임에 영향을 주지 않지만 정적 분석에 사용됩니다.)

# (English notation: Function Definition) (Korean pronunciation: 펑션 데피니션)
# 30년 경력의 노하우: 입력받는 'a'와 'b'는 정수(int)여야 하며, 결과도 정수(int)임을 선언합니다.
# Parameter(파라미터) 뒤에 콜론(:)을 사용하여 타입을 지정함
# Return(리턴) 타입은 화살표(->)를 사용하여 함수가 끝날 때의 결과 타입을 지정함
def add_numbers(a: int, b: int) -> int:
    # (English notation: Function Body) (Korean pronunciation: 펑션 바디)
    # 전달받은 두 정수를 더하여 결과를 생성함
    result = a + b
    # (English notation: Return Statement) (Korean pronunciation: 리턴 스테이트먼트)
    # 계산된 결과값을 호출한 곳으로 돌려줌
    return result

# (English notation: Function Call) (Korean pronunciation: 펑션 콜)
# 타입 힌트 덕분에 10과 20이 적절한 타입인지 에디터가 미리 검사해 줍니다. ✨
total = add_numbers(10, 20)