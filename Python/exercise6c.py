x = 150
print ("Prime numbers upto (n) 150 are: \n")
for number in range(2,x):
    if all(number%i!=0 for i in range(2,number)):
        print (number)
