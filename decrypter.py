
#
##Author: Radhey Ruparel
##Description: This progarm will take two input: the name of a text file and index (key) file, 
##and then it will decrypt the text, as they were encrypted. 
##The program will read in these two files, and using the information stored within them, 
##it will put the contents back in the original order as they were before encryption. 
#

#Required to import all the os functions and progam is able to locate the file
import os
os.chdir(os.path.dirname(__file__))

#Importing all the modules for the program execution  
import random #Importing the random module

#Declaring the main function
def main():
    file_name=input('Enter the name of a mixed text file:\n')
    file_name_index=input('Enter the mix index file:\n')
    decrypting_the_file(file_name,file_name_index)

def decrypting_the_file(file_name,file_name_index):
    '''This function reads the encrypted text file, and decryted in order get them in the original order, 
    with the help of the index file, and also write the orginal order into the decrypted.txt.
    This function has file_name,file_name_index, as it parameter varibale, both of them are strings inputed by 
    the user'''
    
    file_read=open(file_name,'r') #This will open the file with the encrypted text file, to read
    file_index=open(file_name_index,'r') #This will open the file with the indexs to them the orginal order, to read
    
    index_sequence=[] #This list will get each line of the encrypted text file as an item in the list
    line_sequence=[] #This list will get each line of the index text as an item in the list
    
    for line in file_read:
        line_sequence.append(line) #This appends the each line of the encrypted text file as an item in the list

    for index_number in file_index:
        index_number=index_number.rstrip('\n') #This removes the new line in the lines of the index file
        index_sequence.append(int(index_number)) #This appends the each line of the index text file as an item in the list
        
    file_read.close() #This closes the encrypted text file
    file_index.close() #This closes the index text file
    
    line_orginal_sequnece=[] #This list will have the orginal sequence of the encerpyed line  
    numerical_sequnece=1 #This will be help to find the index in the indecreaing numerical 
    while numerical_sequnece<(len(index_sequence)+1):
        orginal_index=index_sequence.index(numerical_sequnece) #This will look for the index which is next line of the orginal order 
        line_orginal_sequnece.append(line_sequence[orginal_index]) #This will look for the line at that numeric sequence, append to the new list to create the orginal sequence
        numerical_sequnece+=1 #This will end when all the lines are over
    
    file_write=open('decrypted.txt','w') #This opens the decrypted.txt text file, to write the orginal sequnce 
    for write_line in line_orginal_sequnece:
        file_write.write(write_line) #This writes the orginal sequnce into the decrypted.txt text file line by line
    
    file_write.close() #This closes the decrypted.txt
    
#Calling the main function
main()