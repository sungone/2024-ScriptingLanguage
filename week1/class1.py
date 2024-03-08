friend = 10
type(friend) # int

Friend = 1 # 대소문자 구별
type(Friend) # int

## for = 1 # 안됨 , for 는 예약어이다

t = (a , b) = (1 , 2)
# ( ) 튜플 : 묶음
## t : 튜플
## (a , b) 는 (1 , 2) 로 할당됨

tt = a , b
## 괄호를 안쳐도 , 로 나타내면 튜플 () 로 만들어줌

a , b = b , a
## a b 스왑

l = [c , d] = [3 , 4]
## list 

## tuple 은 그 안에 있는 원소를 읽을수만 있음
## list 는 읽고 쓸 수 있다

year = 2024
month = 3
print(year , month) ## 화면에 출력하는 함수
print(year , month , 3 , 'tuk')

print(0o10) ## 8진수
print(0o100)

print(0x10) ## 16진수

print(0b10) ## 2진수

oct(38) ## 8진수로 변환 , 문자열로 만들어줌
hex(38) ## 10진수로 변환 , 문자열로 만들어줌
bin(38) ## 2진수로 변환 , 문자열로 만들어줌

type(2**128) ## ** 는 승이다 2의 128승 , 아주 긴 정수도 잘 표현해 준다

f = 3.14
type(f) ## float 

type(314e-2) ## float

x = 3-4j
type(x) ## 복소수 complex

x.real ## 실수부
x.imag ## 허수부

x.conjugate() ## (3+4j) 

y = 1 + 1j
type(y)

x + y ## (4 - 3j)
x * y ## (7 - 1j)

r = 10
circle_area = 3.14*(r**2)
print(circle_area)

x = 3
y = 4
triangle_area = x * y / 2
print(triangle_area)

2 / 3 ## 실수가 나옴 정수 / 정수 -> 실수
2 // 3 ## 정수가 나옴 , 소수점 아래를 버림

s = 'string'
ss = "KOREA"
type(s) ## string 
type(ss) ## string
## 파이썬은 문자 타입 존재 x 다 string type
## string 은 문자열을 조작할수 있는 많은 기능을 제공

sss = '''영원에 살고 순간에 살아라
-리히텐 베르크
'''
### ''' 은 여러줄 쓸 수 있는 문자열
print(sss) ## string

print("hi \nbye \t good") 
### 이스케이프 문자
## \n : 다음줄
## \t : 탭

print(r"\t탭\n다음줄") ## r 은 이스케이프 문자 신경쓰지 말고 그대로 출력해라

'py' + 'thon' ## 'python'
'py' 'thon' ## 'python'
'py' * 3 ## "pypypy"

a = 'python'
type(a) ## a 는 string
a[0] ## 'p' ('p' 는 문자가 아니라 문자열 , 한글자여도 문자열)
a[0:2] ## 'py' , slicing
a[:2] ## a[0:2]
a[2:] ## a[2:끝까지]
a[-1] ## 'n' 제일 뒤에있는 문자를 추출
a[-2:] ## 'on' 문자열의 길이를 몰라도 맨 뒤의 2번째 부터 끝까지 추출 가능
## 맨뒤부터 반대로 -1 -2 -3 의 인덱스가 부여되어 있음

a[:] ## 'python'

str(3.14)
int('49')
## int('korea') ## (X) 문자열 안에 정수가 들어있어야 함 (실수도 안됨)
int('3')
float(23)

a.find('p') ## p가 몇번 인덱스에 있니?
a.find('t')

a.count('p') ## p 가 몇개니?

a.index('p') ## 몇번 인덱스에 있니?

a.find('y') ## 없으면 -1 반환
## a.index("x") index 는 찾는게 없으면 에러
## find 는 string 에만 있는 멤버함수

ord('A') ## 문자를 아스키 코드 수로 변환
ord('a') 
ord('Z') - ord('A') ## 25

chr(65) ## 'A' , 아스키 코드를 주면 문자를 반환

colors = ['red' , 'green' , 'golf']
type(colors) ## list

colors.append("blue") ## 뒤에 덧붙이는 함수
colors.insert(1 , 'black') ## 특정 인덱스 자리에 원소 추가 가능
colors.extend(['white' , 'gray']) ## 리스트를 확장 , 기존 리스트 뒤에 리스트를 붙임

colors += ['red'] ## colors 리스트 뒤에 'red' 가 추가됨
colors += 'red' ## colors 리스트 뒤에 'r' , 'e' , 'd' 가 추가됨

colors.index('red')
colors.index('red' , 1) ## 몇번 인덱스를 기준으로 셀 건지 정할수 있음
## colors.index('red' , 1 , 5) ## 없으면 에러
## colors.find('red') ## (x)

colors.count('red') 

colors.pop() ## 제일 뒤에 있는 원소 제거 , 값 반환
colors.pop(1) ## 특정 인덱스의 원소 제거 , 값 반환
colors.remove('golf') ## 원소의 값을 넣어주면 찾아서 제거 , 원소가 존재하지 않으면 에러

## pop 은 인덱스 , remove 는 값

colors.sort() ## 사전순 정렬
colors.reverse() ## 원래 순서를 반대로 뒤집음

def mysort(x) :
    return x[-1] ## 문자열의 끝
## index 연산을 할 수 있는 것만 전달 가능

colors.sort(key=mysort)
## 각 원소의 문자열의 맨 마지막 문자를 기준으로 사전순으로 정렬
## 이렇게 내맘대로 sort 의 기준을 정할 수 잇음

colors.sort(key=mysort , reverse=True) ## 내림차순으로 정렬 가능

temp = colors
colors.pop(0) # colors 의 0번원소 제거
## temp 의 0번 원소도 같이 없어짐

## why? colors 의 레퍼런스를 temp 에 전달하는 것이기 때문에
## 주소가 같아 실제 사용하는 list 가 같음

temp = colors[:] ## 이건 주소 복사가 아닌 실제 값을 복사 , 둘의 id 가 다름

## 주소만 복사 할건지 값 전체를 복사해서 다른 리스트를 만들지 생각해보자

colors.append(100) ## 같은 타입이 아니어도 추가 가능
colors.append(3.14)
colors.insert(1,["orange"])

