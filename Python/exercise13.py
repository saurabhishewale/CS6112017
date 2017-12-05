import re
a = open("C:\\Users\\Saurabhi Shewale\\Desktop\\Pace University\\Fall 2017\\CS 611 - Prin of Programming Lang\\Python\\emails.txt", "r")
f1 = a.read()
x = re.findall(r'(\w(?:[-.+]?\w+)+\@(?:[a-zA-Z0-9](?:[-+]?\w+)*\.)+[a-zA-Z]{2,})', f1)
for n in x:
    print(n)