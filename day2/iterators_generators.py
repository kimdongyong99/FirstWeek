# iterators_generators.py
# 2일차: 커스텀 이터레이터 & 제너레이터 학습

#커스텀 이터레이터 구현
class CountUpTo:
    def __init__(self, max_value):
        self.max = max_value
        self.current = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current <= self.max:
            val = self.current
            self.current += 1
            return val
        else:
            raise StopIteration


counter = CountUpTo(5)
for num in counter:
    print(num)   # 1 2 3 4 5


#제너레이터 함수 학습

#1.피보나치 수열 제너레이터

def fib_generator(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield b
        a, b = b, a + b
        count += 1


for num in fib_generator(7):
    print(num)   # 1 1 2 3 5 8 13

#2.무한 자연수 제너레이터

def naturals():
    i = 1
    while True:
        yield i
        i += 1

# 사용 (무한이니 주의!)
gen = naturals()
for _ in range(5):
    print(next(gen))   # 1 2 3 4 5

#이터레이터 & 제너레이터 조합 실습

#필터 파이프라인 만들기

# 짝수만 필터
even_gen = (x for x in naturals() if x % 2 == 0)

for _ in range(5):
    print(next(even_gen))  # 2 4 6 8 10
