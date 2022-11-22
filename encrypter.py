#
##Author: Radhey Ruparel
##Description: This program will be to encrypt (“mix” or “shuffle”) the lines from a text file, 
##but do it in such a way that it can be un-done later, if the person has the key to decrypt it.
#

#Required to import all the os functions and progam is able to locate the file
import os
os.chdir(os.path.dirname(__file__))

#Importing all the modules for the program execution  
import random #Importing the random module

#Delcaring main function
def main():
    random.seed(125) #To generate a pattern of random number for a particular type of encryption 
    encrypting_the_file() #Calling the fuction will run the encryption
    

def reading_indexing_file():
    '''This function reads the user selected file, each line in the selected file in a form an item in a list
    The parameter varibles for this function is file_name, it is a string.'''
    file_name=input('Enter a name of a text file to mix:\n') #Asking the user to choose the which need to be encrypted
    file_read=open(file_name,'r') #This will open the selected file to read and further process it
    #This list will have all each line in the selected file in a form an item in the list
    lines_orginal_sequence=[]
    #This is will be the sequcnce of the index which is encryted. 
    line_index_sequence=[]
    #This variable helps to create a asecending order of numbers in the line_index_sequence list 
    line_indexing=0
    
    for line in file_read:
        lines_orginal_sequence.append(line) #This will add the lines as the items on the list
        line_indexing+=1 
        line_index_sequence.append(line_indexing) #This will a create a numeric sequence 
    file_read.close() #Clossing the user selected file
    return line_index_sequence,lines_orginal_sequence #retuns the list which has the lines of file into a list, and list of with its associative indexs

def encrypting_the_file():
    '''This function encrypted the lines and writes the new encrypted text into a text file called encrypted.txt'''
    
    line_index,lines_sequence=reading_indexing_file() #This reading function is called 
    sequence_index=len(lines_sequence)*5 #This is required to swap the index and lines in the list for the required amount of time to produce a certian encepytion pattern
    while sequence_index>0:
        frist_choosen_index=random.randint(0,(len(line_index)-1)) #frist random line and index selected which will be swaped with the second which is randomly selected
        second_choosen_index=random.randint(0,(len(line_index)-1))#second random line and index selected which will be swaped with the frist which is randomly selected
        
        copy_line=lines_sequence[frist_choosen_index] #This copies the frist random line into a dummy varaible for easy swaping
        copy_line_index=line_index[frist_choosen_index] #This copies the frist random index of the frist random line into another dummy varaible for easy swaping
        
        lines_sequence[frist_choosen_index]=lines_sequence[second_choosen_index] #This replaces the frist random line to the second random line
        line_index[frist_choosen_index]=line_index[second_choosen_index] #This replaces the frist random line index to the second random line index
        
        lines_sequence[second_choosen_index]=copy_line  #This replaces the second random line to the dummy varaible, hence frist random line
        line_index[second_choosen_index]=copy_line_index #This replaces the second random line index to the dummy varaible for index, hence frist random line index
        sequence_index-=1
    
    file_write=open('encrypted.txt','w') #This opens the encrypted.txt text file for writing the encrypt text
    file_write_indexs=open('index.txt','w') #This opens the index.txt text file for writing the encrypt text
    index_print=0 #This varaible helps to the write index on the index.txt
    for line in lines_sequence:
        file_write.write(line) #This writes the encryted lines line by line on the encrypted.txt 
        file_write_indexs.write((str(line_index[index_print])+'\n')) #This writes the indexs line by line on the index.txt 
        index_print+=1
    file_write.close() #This closes the encrypted.txt file 
    file_write_indexs.close() #This closes the index.txt file 

#Calling the main function
main()