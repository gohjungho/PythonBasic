def add(a,b):
    return a + b

def sub(a,b):
    return a - b

print(add(1,4))
print(sub(4,2))


# 'from mod1 import *'이 손쉽고 쉬운 방법이지만 쓸데없는 것까지 전부 긁어와서 속도가 매우 떨어진다.
# 가져와 써야하는 메소드가 수백 개 될 경우엔 *을 쓰자