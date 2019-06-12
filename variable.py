# 변수 이름은 문자, 숫자, _로 구성된다.
import  keyword
from builtins import print

friend = 1
a = 10
my_name = '홍길동'
myName = '홍길동'
_yourname = '둘리'
member1 = '도우넛'

# error
# friend$ = 1
# a! = 1
# 1abc = 10
# def = 10

print(keyword.kwlist)

# 한글이름의 변수도 사용이 가능하다.
가격1 = 10000
print(가격1-5000)
