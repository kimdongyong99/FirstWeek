# 정수 리스트를 입력받아 각 원소의 제곱값 리스트를 반환하는 람다 작성

square = lambda nums: list(map(lambda x: x*x,nums))
print(square([1,2,3,4]))

# 두 문자열을 비교해 길이가 긴 쪽을 반환하는 람다 작성

longest = lambda a, b: a if len(a) > len(b) else b
print(longest("Python", "Java"))

# 1~20 사이 숫자 중 짝수만 뽑아 [2,4,6,…] 형태로 만들기

evens = [i for i in range(1,21) if i % 2 == 0]
print(evens)


# 단어 리스트 ["apple","banana","cherry"] → 길이 dict { "apple":5, ... } 만들기

fruits = ["apple", "banana", "cherry"]
length_map = { fruit: len(fruit) for fruit in fruits }
print(length_map)

# 컴프리헨션 콤보: 1~10 제곱수 중 “홀수 제곱”만 뽑기

odd_squares = [x*x for x in range(1,11) if (x*x) % 2 == 1]
print(odd_squares)
