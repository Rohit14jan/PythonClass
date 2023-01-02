# 1. prime number
for num in range(2,101):
    is_prime = True
    for divisor in range(2, num):
        if num % divisor == 0:
            is_prime = False
            break
    if is_prime:
        print(num)

# 2. if num1 is divisible by num2
print('-'*50)
def is_divisible(num1,num2):
    if num1 % num2 == 0:
        return True
    else:
        return False
print(is_divisible(10, 5))
print(is_divisible(11, 5))
print('-'*50)
# 3. num1*num2*num3
print('-'*50)
def multiply(num1, num2, num3):
    return num1 * num2 * num3
print(multiply(2, 3, 4))
print(multiply(5, 6, 7))
print('-'*50)
# 4. num1>num2
print('-'*50)
def is_greater(num1, num2):
    if num1 > num2:
        return True
    else:
        return False
print(is_greater(5, 3))
print(is_greater(3, 5))
print('-'*50)

# 5. greater of num1 and num2
print('-'*50)
def greater(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
print(greater(5, 3))
print(greater(3, 5))
print('-'*50)
#%%
