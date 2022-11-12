import sys



def optimal_sequence(n):
    sequence = []
    while n >= 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        elif n % 3 == 0:
            n = n // 3
        else:
            n = n - 1
    return reversed(sequence)

if __name__ == '__main__':
    
    #input = sys.stdin.read()
    n = 96234 #int(input)

    sequence = list(optimal_sequence(n))
    print(len(sequence) - 1)
    for x in sequence:
        print(x, end=' ')

