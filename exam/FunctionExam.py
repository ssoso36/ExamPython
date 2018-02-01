
# def hap(a, b):
#     print(a + b)
#
# def gop(a, b):
#     print(a * b)
#
# def hap_gop(a, b):
#     hap(a, b)
#     gop(a * b)
#
# print(hap_gop(3, 4))

def countdown(n):
    if n == 0:
        print("0인데...")
    else:
        print(n)
        countdown(n-1)

countdown(3)

def functionTmp(x):
    a = 3
    b = 5
    y = ( a + b ) * x
    return y

c = functionTmp(10)
print(c)


def manyFunc(choice, *args):

    if choice == "sum":
        result = 0
        for i in args:
            result = result + i
    elif choice == "multi":
        result = 1
        for i in args:
            result = result * i
    else:
        result = "else....."
    return result, choice, args

print(manyFunc("sum", 1, 2, 3))
# (6, 'sum', (1, 2, 3))
print(manyFunc("multi", 1, 2, 3, 4, 5))
# (120, 'multi', (1, 2, 3, 4, 5))


def say_myself(name, old, man=True):
    result = "이름 : %s, 나이 : %d, 성별 : " %(name, old)

    if man:
        result = result + "남자"
    else:
        result = result + "여자"
    return result

print(say_myself("test", 10))


