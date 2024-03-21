def Times(a , b) :
    return a * b

Times(10 , 10)
Times(3.5 , 4.5)
Times('Korea' , 3)
Times([0] , 10)

## Times('Korea' , 'TUK')

### 함수의 이름은 함수가 있는 곳의 주소를 가지고있음 (레퍼런스다)
MyTimes = Times

MyTimes(10 , 10)

def setValue(newValue) :
    x = newValue

retVal = setValue(10)
print(retVal)

def swap(x , y) :
    return y , x ## 튜플로 반환

swap(1 , 2) ## 2 , 1

t = swap(1 , 2)
type(t) ## tuple

def intersect(prelist , postlist) : ## 교집합 함수
    retList = []
    for x in prelist :
        if x in postlist and x not in retList :
            retList.append(x)

    return retList

list1 = "SPAM"
list2 = "EGG"
print(intersect(list1 , list2))
print(intersect(list1 , ['H' , 'A' , 'M']))
tup1 = ('B' , 'E' , 'E' , 'F')
print(intersect(list2 , tup1))

x = 10
def sum2(x , y) :
    x = 1 ## 로컬 변수
    return x + y

b = 20
print(sum2(x , b))
print(x)

def change(x) :
    x[0] = 'H'

w = ['J' , 'A' , 'M']
t = ('J' , 'A' , 'M') ## 튜플은 읽을수 잇지만 쓸 수 없음
s = 'JAM'

# change(s) 
# change(t)
change(w)
print(w)
def change(x) :
    x = x[:]
    x[0] = 'H'

w = ['J' , 'A' , 'M']
change(w)
print(w)

g = 1
def testScope(a) :
    global g
    g = 2
    return g + a

testScope(1)
print(g)
