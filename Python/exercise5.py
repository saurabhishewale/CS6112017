i = 1
number = 0
count = 0
print("List of first 20 numbers divisible by 5, 7 and 11")
while(count < 20):
    if(i%5 == 0 and i%7 == 0 and i%11 == 0):
        number = i
        print("{} - {}".format(count+1,number))
        i+=1
        count+=1
    else:
        i+=1