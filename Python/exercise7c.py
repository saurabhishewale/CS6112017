def list_count(n):
    count =0
    for i in n:
        count+=1
    return count

l = [1,2,23,10,57,4,41,8]
print("The length of the list : ",list_count(l))