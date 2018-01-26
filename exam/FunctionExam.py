
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




