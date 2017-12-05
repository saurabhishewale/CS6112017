def fun_iteration(n):
    product =1
    for i in n:
        product = product *i
    return product

def fun_recursion(n):
    if not n:
        return 1
    return n[0] * fun_recursion(n[1:])

l = [1,2,4,5]
print("with Iteration : ",fun_iteration(l))
print("With Recursion : ",fun_recursion(l))
