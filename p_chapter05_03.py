# Chapter05-03
# 파이썬 심화
# 클로저 심화
# 클로저 : 외부에서 호출 된 함수의 변수값, 상태(레퍼런스) 복사 후 저장 -> 후에 접근(엑세스) 가능
# 클로저(Closure) 사용

# ex1에서 사용 된 series(리스트)는 가변 자료구조이고,
# ex2에서 사용 된 Local Variable은 Immutable 성격을 가지고 있어, 에러가 발생한다.

def closure_ex1():
    # Free variable
    series = []

    # Closure Area (클로저 영역)
    def averager(v):
        sereis.append(v)
        print('inner >>> {} / {}'.format(series, len(series)))
        return sum(series) / len(series)
    return averager
    # 함수 안에 함수를 호출함 -> Closure


avg_closure1 = closure_ex1()

print(avg_closure1(15))
print(avg_closure1(35))
print(avg_closure1(40))

print()
print()

# function inspection

print(dir(avg_closure1))
print()
print(dir(avg_closure1.__code__))
print()
print(avg_closure1.__code__.co_freevars)
print()
print(dir(avg_closure1.__closure__[0]))
print()
print(avg_closure1.__closure__[0].cell_contents)

print()
print()


# 잘못된 클로저 사용
## Free variable을 사용할 때, 유의하기 -> nonlocal로 선언하기.
def closure_ex2():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        cnt += 1 # cnt = cnt + 1
        total += v
        return total / cnt

    return averager

avg_closure2 = closure_ex2()

# print(avg_closure2(15)) # 예외


# Nonlocal -> Free variable
def closure_ex3():
    # Free variable
    cnt = 0
    total = 0

    def averager(v):
        nonlocal cnt, total
        cnt += 1
        total += v
        return total / cnt

    return averager

avg_closure3 = closure_ex3()

print(avg_closure3(15))
print(avg_closure3(35))
print(avg_closure3(40))

print()
print()
