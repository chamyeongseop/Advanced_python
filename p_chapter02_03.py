# Chapter02-03
# 파이썬 심화
# 클래스 메소드, 인스턴스 메소드, 스테이틱 메소드

# 기본 인스턴스 메소드

# 클래스 선언
class Car(object):
    '''
    Car Class
    Author : Me
    Date : 2019.11.08
    Description : Class, Static, Instance Method
    '''

    # Class Variable
    price_per_raise = 1.0

    def __init__(self, company, details):
        self._company = company
        self._details = details
        
    def __str__(self):
        return 'str : {} - {}'.format(self._company, self._details)

    def __repr__(self):
        return 'repr : {} - {}'.format(self._company, self._details)

    # Instance Method
    # Self 인자를 받는 것을 Instance Method라고 함.
    # self : 객체의 고유한 속성 값 사용

    def detail_info(self):
        print('Current Id : {}'.format(id(self)))
        print('Car Detail Info : {} {}'.format(self._company, self._details.get('price')))
        
    # Instance Method
    def get_price(self):
        return 'Before Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price'))

    # Instance Method
    # Class 변수 price_per_raise는 모두 공유하는 변수
    def get_price_culc(self):
        return 'After Car Price -> company : {}, price : {}'.format(self._company, self._details.get('price') * Car.price_per_raise)

    # Class Method
    # cls: Instance Method를 통해, 매개변수를 보내는 일을 하지 않고, 클래스 자기 자신을 첫번째 매개변수로 받는 차이가 있음 -> cls 매개변수를 사용하여 Class Method 사용 (가독성 좋음)
    @classmethod
    def raise_price(cls, per):
        if per <= 1:
            print('Please Enter 1 or More')
            return
        cls.price_per_raise = per
        return 'Succeed! price increased.'

    # Static Method
    # Static Method는 특별한 파라미터를 받지 않는다.
    @staticmethod
    def is_bmw(inst):
        if inst._company == 'Bmw':
            return 'OK! This car is {}.'.format(inst._company)
        return 'Sorry. This car is not Bmw.'
    
    
# 자동차 인스턴스
# 인스턴스 변수 : 보통은 캡슐화로 설정하여, Private로 설정함. 보통은 메소드를 만들어서, 필요한 정보를 반환하는 방식으로 만듦.
car1 = Car('Bmw', {'color' : 'Black', 'horsepower': 270, 'price': 5000})
car2 = Car('Audi', {'color' : 'Silver', 'horsepower': 300, 'price': 6000})

# 기본 정보
print(car1)
print(car2)
print()

# 전체 정보
car1.detail_info()
car2.detail_info()
print()

# 가격 정보(직접 접근) -> 추천하지 않는 방법
print(car1._details.get('price'))
print(car2._details.get('price'))

# 가격 정보(인상 전)
print(car1.get_price())
print(car2.get_price())
print()

# 가격 인상(클래스 메소드 미사용) -> 직접 접근법으로 추천하지 않음
Car.price_per_raise = 1.2

# 가격 정보(인상 후)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# 가격 인상(클래스 메소드 사용)
Car.raise_price(1.6)
print()

# 가격 정보(인상 후 : 클래스메소드)
print(car1.get_price_culc())
print(car2.get_price_culc())
print()

# Bmw 여부(스테이틱 메소드 미사용)
def is_bmw(inst):
    if inst._company == 'Bmw':
        return 'OK! This car is {}.'.format(inst._company)
    return 'Sorry. This car is not Bmw.'

# 별도의 메소드 작성 후 호출
print(is_bmw(car1))
print(is_bmw(car2))
print()

# Bmw 여부(스테이틱 메소드 사용)
# 클래스 또는 인스턴스로 호출해도 동일한 결과가 나타남
print('Static : ', Car.is_bmw(car1))
print('Static : ', Car.is_bmw(car2))
print()

print('Static : ', car1.is_bmw(car1))
print('Static : ', car2.is_bmw(car2))
