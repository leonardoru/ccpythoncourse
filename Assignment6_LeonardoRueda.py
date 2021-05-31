# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYTHON-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Assignment 6: Write a Python program that takes file name and content
# Student: Leonardo Rueda
import re

def validateFile(fileName):
    extensionCheck = re.search("(^[A-Za-z0-9\_][A-Za-z0-9\_]+\.[A-Za-z0-9\_]+[A-Za-z0-9\_]$)",fileName)
    charsCheck = re.search("(^[A-Za-z0-9\_][A-Za-z0-9\_\.]+[A-Za-z0-9\_]$)",fileName)
    capsCheck = re.search("(^[A-Z])", fileName)

    # Checking 3 cases of validation usign regular expressions
    if charsCheck is None:
        print('Filename can contain only Alphabets, digits and "_"')
        return False
    if extensionCheck is None:
        print('The file has to have a valid extension')
        return False
    if capsCheck is None:
        print("Filename only can start with Alphabets or '_'.")
        return False
    return True

def main():
    oneMoreFile = True
    while oneMoreFile == True :
        # Declare a few variables we will need along the way
        fileNameOk = False
        oneMoreLine = True
        moreFileCases = {
                'y': 'y',
                'Y':'y',
                'Yes':'y',
                'yes':'y',
                'n':'n',
                'N':'n',
                'No':'n',
                'no':'n'
            }
        
        # Validate file name
        while fileNameOk == False:
            fileName = input('Please enter a filename: ')
            fileNameOk = validateFile(fileName)
            if fileNameOk:
                fileNameOk = True
            else:
                print('Plese enter a proper filename. ')
        
        # Create file and add lines
        file_object = open(fileName, "w+")
        
        while oneMoreLine == True:
            newLine = input('Please enter a sentence: ')
            file_object.write(newLine + '\n')
            moreLines = input('Do you want to add more lines? (Y/N)')
            if (moreLines =='y' or moreLines =='Y' or moreLines =='yes' or moreLines =='Yes'):
                continue 
            else:
                oneMoreLine = False

        file_object.close()
        print("This is what's entered into file " + fileName)
        print("================================")
        file_object = open(fileName, "r")
        print(file_object.read())
        print("================================")
            
        # Confirm if the user wants to add one more file
        oneMoreFileAns = input('Do you want to create another file? (Y/N)')
        oneMoreFileAns = moreFileCases.get(oneMoreFileAns,"I did not understand your answer...")
        if oneMoreFileAns == 'n':
            print('Good bye then')
            break

        if oneMoreFileAns == 'y':
            print('Let\'s do one more file!')
            continue
        
        else:
            print(oneMoreFileAns)
            print('Good bye then')
            break
main()
# By: Leonardo Rueda

