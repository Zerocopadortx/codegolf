fibonacci_maximum = 31
fibonacci_sequence = []

y = 0
z = 0

for i in range(fibonacci_maximum):
        if i == 0:
            f = 0
            print(f)
            fibonacci_sequence.append(f)
        elif i == 1:
            f = 1
            print(f)
            fibonacci_sequence.append(f)
        else:
            f = fibonacci_sequence[i-1] + fibonacci_sequence[i-2]
            print(f)
            fibonacci_sequence.append(f)


