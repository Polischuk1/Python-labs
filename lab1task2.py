#Створити рекурсивну функцію fib(k), яка повертає список n чисел Фібоначчі.
# Написати програму яка виводить k чисел Фібоначчі, використовуючи функцію fib(k).


def fib (k):
    sequence = []
    if k < 0:
        print('Incorrect input')
        return sequence
    elif k == 0:
        return sequence.append(0)
    elif k == 1:
        return sequence.extend([0,1]) 
    else:
        sequence.extend([0, 1])  
        for i in range(2,k + 1):
          sequence.append( sequence [-1] + sequence[-2]) # Add the sum of the last two elements
    return sequence
    
k = 9
print(f"Fibonacci sequence up to {k} is {fib(k)}" )


