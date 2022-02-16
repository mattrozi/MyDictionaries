#Write a program that reads the contents of a text file (you can use this file - AI.txt).
#  The program should create a dictionary in which the keys are the individual words found in the file and the values are the number of times each word appears.
#  For example, if the word “the” appears 128 times, the dictionary would contain an element with 'the' as the key and 128 as the value. 
# The program should display the frequency of each word.


def main(): 
   outfile=open('AI.txt','r')

   file_contents=outfile.read().split()

   word_list={}


   for i in range(len(file_contents)):
     word_list[file_contents[i]]=0

   for i in range(len(file_contents)):
     word_list[file_contents[i]]+=1

   print(word_list)

   outfile.close()


main()