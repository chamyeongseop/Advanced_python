# Chapter06-02
# 병행성(Concurrency) : 한 컴퓨터가 여어 일을 동시에 수행함. -> 코루틴으로 해결 가능 -> 단일 프로그램 안에서 여러가지 일을 쉽게 해결함.
## Thread는 하나지만, 여러가지 일을 동시에 하는 것처럼 효율을 높일 수 있음(파이썬의 장점)
# 병렬성(Parallelism) : 여러 컴퓨터가 여러 작업을 동시에 수행함 -> 속도

# 이터레이터, 제네레이터
# Iterator, Generator

# 파이썬 반복 가능한 타입
# for, collections, text file, List, Dict, Set, Tuple, unpacking, *args

# Generator Ex1
def generator_ex1():
    print('Start')
    yield 'A Point.'
    print('continue')
    yield 'B Point.'
    print('End')

temp = iter(generator_ex1())

# print(next(temp))
# print(next(temp))
# print(next(temp))

for v in generator_ex1():
    pass
    # print(v)

print()

# Generator Ex2
temp2 = [x * 3 for x in generator_ex1()] # Yield가 return 역할을 함.
temp3 = (x * 3 for x in generator_ex1()) # Generator

print(temp2)
print(temp3)

for i in temp2:
    print(i)

print()
print()

for i in temp3:
    print(i)

print()
print()


# Generator Ex3(중요 함수) : itertools를 통해 사용할 수 있는 메소드
# count, takewhile, filterfalse, accumulate, chain, product, product, groupby
import itertools

gen1 = itertools.count(1, 2.5)

print(next(gen1))
print(next(gen1))
print(next(gen1))
print(next(gen1))
# ... 무한

print()

# 조건
## 1000 미만일 때까지 계속해서 증가함.
gen2 = itertools.takewhile(lambda n : n < 1000, itertools.count(1, 2.5))

for v in gen2:
    print(v)


print()

# 필터 반대 -> 조건식의 반대의 경우를 취함
gen3 = itertools.filterfalse(lambda n : n < 3, [1,2,3,4,5])

for v in gen3:
    print(v)


print()

# 누적 합계
gen4 = itertools.accumulate([x for x in range(1, 101)])

for v in gen4:
    print(v)

print()

# 연결1
gen5 = itertools.chain('ABCDE', range(1,11,2))

print(list(gen5))

# 연결2

gen6 = itertools.chain(enumerate('ABCDE'))

print(list(gen6))

# 개별
gen7 = itertools.product('ABCDE')

print(list(gen7))

# 연산(경우의 수)
gen8 = itertools.product('ABCDE', repeat=2)

print(list(gen8))

# 그룹화
gen9 = itertools.groupby('AAABBCCCCDDEEE')

# print(list(gen9))

for chr, group in gen9:
    print(chr, ' : ', list(group))

print()