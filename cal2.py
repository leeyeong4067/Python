#더하기 함수 정의
def add(a, b):
    c = a + b
    return c

#빼기 함수 정의
def minus(a, b):
    c = a - b
    return c

#곱하기 함수 정의
def multiply(a, b):
    c = a * b
    return c

#나누기 함수 정의
def divide(a, b):
    c = a / b
    return c


while True :
    a = input("first value : ")

    if a == '0000' :
        break

    a = int(a)
    b = int(input("second value : "))
    
    result = add(a, b)
    print(a, "+", b, "=", result)
    result = minus(a, b)
    print(a, "-", b, "=", result)
    result = multiply(a, b)
    print(a, "*", b, "=", result)
    result = divide(a, b)
    print(a, "/", b, "=", result)

print("exit")
