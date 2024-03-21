def Times(a = 10 , b = 20) :
    return a * b
Times()
# 200
Times(5)
# 100

def connectURI(server , port) :
    str = 'http://' + server + ':' + port
    return str

connectURI('test.com' , '8080')
# 'http://test.com:8080'
connectURI(port = '8080' , server = 'test.com')
# 'http://test.com:8080'

def test(*args) :
    print(type(args))

test(1 , 2 , 3, 4 , 5)
# * 이 앞에 붙으면 가변인자

## 인자의 개수가 정해지지않고 여러개가 정해질수 있게
## * 앞에 붙이면 가변인자 -> 튜플로 동작
def union2(*ar) :
    res = []
    for item in ar :
        for x in item :
            if not x in res :
                res.append(x)
    return res

print(union2('HAM' , 'EGG' , 'SPAM'))

# **인자값 도 가변인자 -> 사전 형식으로 받음

def userURIBuilder(server , port , **user) :
    str = 'http://' + server + ':' + port + '/?'
    for key in user.keys() :
        str += key + '=' + user[key] + '&'
    return str

print(userURIBuilder('test.com' , '8080' , id='userid' , password='1234' , name = 'mike' , age='20'))

g = lambda x , y : x * y
g(2 , 3) ## 6

(lambda x : x * x)(3) ## 9

def testLambda(g) :
    g(1 ,2 , 3)

testLambda(lambda a , b , c : print(a , b , c)) 

print(list(zip('abc' , [1 , 2 , 3] , ('가' , '나' , '다'))))

l = ['apple' , 'banana' , 'orange' , 'kiwi']
l.sort()
print(l)
l.sort(key=lambda x : x[-1])
print(l)

### 하노이의 탑

def hanoi(ndisks , startPeg = 1 , endPeg = 3) :
    if ndisks :
        hanoi(ndisks - 1 , startPeg , 6 - startPeg - endPeg)
        print(startPeg , '번 기둥의' , ndisks , '번 원반을' , endPeg , '번 기둥에 옮깁니다.')
        hanoi(ndisks - 1 , 6 - startPeg - endPeg , endPeg)

hanoi(5)