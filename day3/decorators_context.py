# decorators_context.py
# 3일차: 데코레이터와 컨텍스트 매니저 심화

# timeit 스타일 데코레이터(실행 시간 측정)
import time
from functools import wraps
from contextlib import contextmanager

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIMER] {func.__name__} 실행 시간: {end - start:.6f}초")
        return result
    return wrapper

@timer
def compute(n):
    total = 0
    for i in range(n):
        total += i * i
    return total

if __name__ == "__main__":
    compute(1000000)

# 호출 로깅 데코레이터 작성
def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"[LOG] 호출: {func.__name__}(), args={args}, kwargs={kwargs}")
        return func(*args, **kwargs)
    return wrapper

@logger
def greet(name, msg="안녕하세요"):
    print(f"{name}, {msg}")

if __name__ == "__main__":
    greet("동용", msg="오늘도 화이팅!")


# 클래스 기반 컨텍스트 매니저 구현

class FileOpener:
    def __init__(self, filepath, mode):
        self.filepath = filepath
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filepath, self.mode, encoding="utf-8")
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
        # False를 반환하면, 발생한 예외를 그대로 밖으로 전달
        return False

if __name__ == "__main__":
    with FileOpener("test.txt", "w") as f:
        f.write("3일차 클래스 기반 컨텍스트 매니저 테스트\n")
    print("test.txt 파일이 생성되었습니다.")

# 함수형 컨텍스트 매니저 구현

@contextmanager
def open_file(path, mode):
    f = open(path, mode, encoding="utf-8")
    try:
        yield f
    finally:
        f.close()

if __name__ == "__main__":
    with open_file("test2.txt", "w") as f:
        f.write("3일차 contextmanager 데코레이터 버전 테스트\n")
    print("test2.txt 파일이 생성되었습니다.")


# 3일차 학습 노트

## 데코레이터
# - @wraps: 메타 정보 보존
# - timer: 함수 실행 시간 측정 패턴
# - logger: 호출 인자 로깅 패턴


## 컨텍스트 매니저
# - 클래스 방식: __enter__/__exit__
# - 함수 방식: @contextmanager + yield
# - 예외 처리 흐름: __exit__ 반환값 / finally 블록
