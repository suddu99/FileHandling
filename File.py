import sys
import os
import fileinput

# read the first file
file1 = open("usermanual.txt", "r")
# read the second file
file2 = open("usermanual1.txt", "r+")
#open third file
file3 = open("usermanual2.txt", "w")
# copy contents of first in second
op = input("Which feature to execute?")
if op == "copy":
    for data in file1:
        file2.write(data)
#replace a particular word in the file
elif op == "replaceWord":
    file2 = open("usermanual1.txt", "rt")
    word1 = str(input("Enter word to be replaced"))
    word2 = str(input("Enter the new word"))
    for line in file2:
        file3.write(line.replace(word1, word2))
    file2.close()
#length of the string
elif op == "len":
    file2 = open("usermanual1.txt","rt")
    n=file2.read()
    l=len(n)
    print("Length of file ",l)
    file2.close()
#convert to upper case
elif op == "upper":
    file2 = open("usermanual1.txt","rt")
    for letter in file2:
        file3.write(letter.upper())
    file2.close()
#conver to lower case
elif op == "lower":
    file2 = open("usermanual1.txt","rt")
    for letter in file2:
        file3.write(letter.lower())
    file2.close()
else:
    print("No operation")
file1.close()
file2.close()
file3.close()







