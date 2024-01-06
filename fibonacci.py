def fibonacci(nterms):
    n1, n2 = 0, 1
    count = 0

    if nterms <= 0:
        print("Please enter a positive number")
    elif nterms == 1:
        print("Fibonacci sequence:")
        print(n1)
    else:
        print("Fibonacci sequence:")
        while count < nterms:
            print(n1)
            n3 = n1 + n2
            n1 = n2
            n2 = n3
            count += 1


fibonacci(8)