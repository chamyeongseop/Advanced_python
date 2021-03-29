# Chapter07-01
# Asyncio is a library to write concurrent code using the async/await syntax
# Asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
# Async I/O: 코루틴에서 네트워크나 파일 처리를 따로 할 수 있도록 만듦
# 비동기 I/O Coroutine 작업
# Generator -> 반복적인 객체 Return 사용
# non-blocking 비동기 처리

## 용어 숙지
### Blocking I/O : 호출 된 함수가 자신의 작업이 완료 될 때까지 제어권을 가지고 있음. 타 함수는 대기해야 함
### NonBlocking I/O : 호출 된 함수(서브 루틴)가 reture(yield) 후, 호출한 함수(메인 루틴)에 제어권을 전달 -> 타 함수는 일을 지속할 수 있음


# 쓰레드 단점 : 디버깅, 자원 접근 시 Race Condition(경쟁 상태), 데드락(Dead Lock) 들을 고려한 후에 코딩해야 함.
# 코루틴 장점 : 하나의 루틴만 실행 -> 락 관리 필요가 없고, 제어권을 통해 실행함.
# 코루틴 단점 : 사용 함수가 비동기로 구현되어 있어야 하거나, 직접 비동기로 구현해야 함


# Asyncio 웹 스크랩핑 실습
# aiohttp 권장
import asyncio
import timeit
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import threading

# 실행 시작 시간
start = timeit.default_timer()

# 서비스 방향이 비슷한 사이트로 실습 권장(예 : 게시판성 커뮤니티)
urls = ['http://daum.net', 'https://naver.com', 'http://mlbpark.donga.com/', 'https://tistory.com', 'https://wemakeprice.com/']


async def fetch(url, executor):
    # 쓰레드명 출력
    print('Thread Name :', threading.current_thread().getName(), 'Start', url)
    # 실행
    # 다른 함수가 요청할 때까지 기다려 줌
    # urlopen은 Block 함수이므로, Non-block 함수로 만들어준다.
    res = await loop.run_in_executor(executor, urlopen, url)
    print('Thread Name :', threading.current_thread().getName(), 'Done', url)
    # 결과 반환
    return res.read()[0:5]

# 비동기 함수 선언
async def main():
    # 쓰레드 풀 생성
    executor = ThreadPoolExecutor(max_workers=10)

    # future 객체 모아서 gather에서 실행 " list comprehension
    # 중요 부분
    futures = [
        asyncio.ensure_future(fetch(url, executor)) for url in urls
    ]

    # 결과 취합
    # futures는 list형태이므로 Unpacking을 수행한 후, Instance로 넣어준다.
    rst = await asyncio.gather(*futures)

    print()
    print('Result : ', rst)

if __name__ == '__main__':
    # 루프 초기화
    loop = asyncio.get_event_loop()
    # 작업 완료 까지 대기
    loop.run_until_complete(main())
    # 수행 시간 계산
    duration = timeit.default_timer() - start
    # 총 실행 시간
    print('Total Running Time : ', duration)
