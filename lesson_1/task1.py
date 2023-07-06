# 1
# if number <= mid
# low(1) mid(128) high(256)
# low(1) mid(64) high(128)
# low(1) mid(32) high(64)
# low(1) mid(16) high(32)
# low(1) mid(8) high(16)
# low(1) mid(4) high(8)
# low(1) mid(2) high(4)
# example low = mid = high = 4
       # in 8 steps

# 2
       # in 9 steps

# 3


# 4
def binary_search():
    list_of_number = []   
    for i in range(1,101):
       list_of_number.append(i)
    low = 0
    high = len(list_of_number) - 1
     
    while low <= high:
       mid = (low + high) // 2  
       guess = list_of_number[mid]
       
       question = input(f"your number (< = >) than {guess} ? ")

       if question == "=":
              return f"Your number = {guess}"
       elif question == "<":
              high = mid - 1
       else:
              low = mid + 1
        
print(binary_search())

# 5
import random
def guess_the_number():
    list_of_number = []   
    for i in range(1,101):
        list_of_number.append(i)
    number = random.choice(list_of_number)
    low = 0
    high = len(list_of_number) - 1
    print("write a number between 1-100 ")

    while low <= high:
        number_of_user = int(input("number "))

        if number_of_user == number:
            return f"yes"

        elif number_of_user > number:
            print(f"number < {number_of_user}")
            high = number_of_user - 1 

        else:
            print(f"number > {number_of_user}")
            low = number_of_user + 1

print(guess_the_number())