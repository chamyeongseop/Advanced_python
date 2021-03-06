# Chapter06-03
# 흐름제어, 병행성(Concurrency)
# 코루틴(Coroutine)

# yield : 메인 루틴 <-> 서브 루틴
# 코루틴 제어, 상태, 양방향 전송
# yield from

# 서브루틴 : 메인루틴에서 호출 -> 서브루틴에서 수행(흐름제어)
# 코루틴 : 루틴 실행 중 중지(Stop Point를 저장하고 있음) ->  동시성 프로그래밍
# 코루틴 : 단일(싱글) 쓰레드 : 스택을 기반으로 동작하는 비동기 작업을 수행 -> 쓰레드에 비해 오버헤드 감소

# 쓰레드 : OS 관리, CPU 코어에서 실시간, 시분할 비동기 작업 -> 멀티 쓰레드
# 쓰레드 : 싱글쓰레드 -> 멀티쓰레드 -> 복잡 -> 공유되는 자원 -> 교착 상태 발생 가능성, 컨텍스트 스위칭 비용 발생, 자원 소비 가능성 증가
# 파이썬 3.5 이상에서는 def -> async, yield -> await로 사용할 수 있음


# 코루틴 Ex1
## 해당 영역은 서브 루틴 영역
def coroutine1():
    print('>>> coroutine started.')
    # yield가 들어간다면 Generator라고 볼 수 있음.
    i = yield
    print('>>> coroutine received : {}'.format(i))

## 아래 영역은 메인 루틴 영역
# 제네레이터 선언
cr1 = coroutine1()

print(cr1, type(cr1))

# yield 지점 까지 서브루틴 수행
# next(cr1)

# 기본 전달 값 None
# next(cr1)

# 값 전송
# Send 명령어를 통해, 메인 루틴과 서브 루틴이 서로 데이터를 교환할 수 있음
# cr1.send(100)

# 잘못된 사용
cr2 = coroutine1()

# next없이 send를 바로 보낸 경우.
# 즉 Next 명령어를 통해, Yield 안에서 멈춘 다음에, Send를 사용할 수 있다. -> 지점을 먼저 간 후에, 데이터를 송신 및 수신이 가능함(Send 사용 조건)
# cr2.send(100) # 예외 발생

# 코루틴 Ex2
# GEN_CREATED : 처음 대기 상태
# GEN_RUNNING : 실행 상태
# GEN_SUSPENDED : yield 대기 상태 (중요!): 이 때 Send를 보낼 수 있음
# GEN_CLOSED : 실행 완료 상태

def coroutine2(x):
    print('>>> coroutine started : {}'.format(x))
    # 왼쪽 변수의 위치는 Receiver, 오른쪽 변수의 위치는 Sender
    # 오른쪽에 있으면 나한테 주는 것이고, 왼쪽에 있으면 입력 값
    y = yield x
    print('>>> coroutine received : {}'.format(y))
    z = yield x + y
    print('>>> coroutine received : {}'.format(z))


cr3 = coroutine2(10)

from inspect import getgeneratorstate

print(getgeneratorstate(cr3))

print(next(cr3))

print(getgeneratorstate(cr3))

print(cr3.send(15))

# print(c3.send(20)) # 예외

print()
print()

# 코루틴 Ex3
# StopIteration 자동 처리(3.5 -> await)
# 중첩 코루틴 처리
def generator1():
    for x in 'AB':
        yield x
    for y in range(1,4):
        yield y

t1 = generator1()

print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
print(next(t1))
# print(next(t1))

t2 = generator1()

print(list(t2))

print()
print()

def generator2():
    # yield from : 순차적인 Iterator를 끝날 때까지 출력함
    yield from 'AB'
    yield from range(1,4)


t3 = generator2()

print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
print(next(t3))
# print(next(t3))

print()
print()