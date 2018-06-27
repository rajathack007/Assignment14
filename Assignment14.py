#Q.1.Write A python program for print  a last n line..........
f=open("test.txt")
content=f.readlines()
print(content)
f.close()
n=int(input("enter the lines"))
while n>0:
    print(content[-n])
    n=n-1

#Q.2 Write a Python program to count the frequency of words in a file.
words=open("test.txt","r").read().split()
print(words)
uniqwords=sorted(set(words))
print(uniqwords)
print(type(uniqwords))
for word in uniqwords:
    print(words.count(word),word)

#Q.3- Write a Python program to copy the contents of a file to another file.
with open('test.txt','r') as f1:
    with open('test1.txt','w') as f2:
        for line in f1:
            f2.write(line)

#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file..........
with open('test.txt','r') as f1:
    with open('test1.txt','r') as f2:
        for line1,line2 in zip(f1,f2):
            print(line1+line2)

#Q.5-Write a python program to write 10 random numbers in to a file.Read The file  and then  sort the numbers and then store it to another file.
import random
with open ('abc.txt','w') as f:
    for x in range(10):
        n=random.randint(1,9)
        f.write(str(n))
        f.write("\n")
with open ('abc.txt','r') as f:
    numbers=f.readlines()
numbers.sort()
with open('test2.txt','w') as f:
    for n in numbers:
        f.write(n)
        f.write("\n")




