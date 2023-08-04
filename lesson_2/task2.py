# 2
def gcd(a, b):
    if a == 0 :
        return b
     
    return gcd(b%a, a)

print(gcd(10,15))

# 3
def binaryToDecimal(n):
    num = n
    dec_value = 0 
    base = 1

    temp = num
    while(temp):
        last_digit = temp % 10
        temp = int(temp // 10)
        dec_value += last_digit * base
        base = base * 2
    return dec_value

num = 11001
print(binaryToDecimal(num))