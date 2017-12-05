def is_prime(x, l):
    n = 0
    for k in range(2, x):
        prime = True
        for i in range(2, k):
            if (k % i == 0):
                prime = False
        if prime:
            if (n < l):
                print("Prime no.{} : {} ".format(n + 1, k))
                n += 1
is_prime(100, 15)