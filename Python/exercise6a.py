def is_prime(n):
        for i in range(2,n):
            if(n%i ==0):
                print(n,": False\n")
                break
        else:
            print(n,": True\n")
is_prime(47)
