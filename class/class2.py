a = {1 , 2 , 3}
b = {3 , 4 , 5}
type(a) # set
# set 은 집합이므로 인덱스 연산자가 없음

a = {1 , 1 , 1 , 2 , 3}
b = {3 , 4 , 5}
a.union(b) # 합집합
a.intersection(b) # 교집합

t = (1 , 2 , 3) ## 튜플
type(t) # class tuple 
## tuple 은 읽을 수만 있다

## list , set , tuple 형변환 가능
a = set((1 , 2 , 3))
b = list(a)
c = tuple(b)
d = set(c)

## in 연산자 제공 , 원소를 갖고 있느냐 검사 가능 , True False 반환

if 1 in c :
    print("YES")

## dict : 사전 (단어 : 뜻)
d = dict(a = 1 , b = 3 , c = 5)
## index 연산자 쓸수 없음 , 순서가 없음
## d[key] 을 주면 밸류를 줌
d['a']

color = {'apple' : 'red' , 'banana' : 'yellow'}
color['apple'] ## red
##color['cherry'] ## 없는 키값을 읽으려 하면 에러
color['cherry'] = 'red'
## 기존에 없는 키값에 밸류를 만들어주면 dict 에 삽입됨
color['apple'] = 'green' ## 키의 밸류를 변경함
print(color)

for c in color.items() : ## key , value 쌍을 튜플로 묶어서 반환시켜줌
    print(c)

for k , v in color.items() :
    print(k , v)

for k in color.keys() :
    print(k)

for v in color.values() :
    print(v)

del color['cherry'] ## cherry 의 키 밸류 쌍이 제거됨
color.clear() ## 다 지우고 싶으면 clear

ll = [1 , 2 , 3 , 4.5 , 'korea' , (1 , 2) , {'apple' : 'red'}]
ss = (0 , 2 , 3 , 4.5 , 'korea' , (1 , 2) , {'apple' : 'red'})
sss = {1 , 2 , 3 , 4.5 , 'korea' , (1 , 2) , {'apple' : 'red'}}
ddd = {'age' : 40 , 'job' : [1 , 2 , 3] , 'name' : {'kim' : 2 , 'cho' : 1}}

isRight = False
type(isRight) ## False
isRight = not isRight
type(isRight) ## True

a = [1 , 2 , 3]
b = a ## 리스트의 변수는 레퍼런스이다 , 주소가 변수 b 에 복사되므로 a 값이 변하면 b 값도 변한다

id(a)
id(b)

b = a[:] ## a 의 값만이 복사되어 새로운 리스트 b 가 만들어진다

## 2차원일때
import copy
a = [1 , 2 , 3]
b = copy.deepcopy(a)

import random
random.random() ## 0 이상 1 미만의 실수를 랜덤하게 생성 (1은 미포함)
random.randint(1 , 10) ## 1 이상 10 미만의 정수중 랜덤하게 생성
random.choice(['red' , 'blue' , 'orange'])
l = ['red' , 'blue' , 'orange']
random.shuffle(l)

