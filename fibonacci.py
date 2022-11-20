def fibonacci_number(n):
    if n <= 1:
        return n

    return fibonacci_number(n - 1) + fibonacci_number(n - 2)

def fibonnacci_number_fast(n):
    f1=0
    f2=1
    if (n < 2):
        return n  
 
    for i in range(n-1):
        tmp_f1 = f1
        f1 = f2
        f2 = tmp_f1 + f2
    return f2

if __name__ == '__main__':
    input_n = int(input("Enter a number:"))
    print(fibonnacci_number_fast(input_n))