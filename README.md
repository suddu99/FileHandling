# FileHandling
#read the first file
f=open("qn.txt","r")

#read the second file
f1=open("qn1.txt","r")

#Create a thrid file
f2=open("que.txt","w")

#copy contents of first and second into third file
for i in f:
    f2.write(i)
for j in f1:
    f2.write(j)

#read the 4th file
f3=open("qn2.txt","r")
n=f3.read()

#append the contents of f3 to f2
f2=open("que.txt","a")
f2.write(n)

f.close()
f1.close()
f2.close()
f3.close()
