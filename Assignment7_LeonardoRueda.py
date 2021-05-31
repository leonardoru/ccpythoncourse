# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYTHON-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Assignment 7: Write a Python program which asks PDF filename and pages to extract into a new PDF
# Student: Leonardo Rueda
from PyPDF2 import PdfFileReader, PdfFileWriter

# First we get the users input and initiallize Pdf-File reader...
userInputFile = input('Please enter a file name: ')
pdfFileName = PdfFileReader(userInputFile)

# Initialize while loop for cases were page ranges are erroneous and we need to ask page numbers again
while True:      
    startPage = int(input('Please enter the beginning page number to extract: '))
    endPage = int(input('Please enter the ending page number to extract: '))
    
    # Get totatl pages using PyPDF2
    total_pages = pdfFileName.getNumPages()

    # Validate pages prvided by user are in range of the Pdf file total pages
    if endPage < startPage or endPage > total_pages or startPage > total_pages:
       # If not message and restart loop
        print('Your beginning and ending page numbers are not correct.')
        continue
    
    # If page ranges are ok iterate trough the page range provided by user
    for page_num in range(startPage, endPage+1):
        # Add pages one by one to File Writer Object
        PdfFileWriter().addPage(pdfFileName.getPage(page_num))

    # Get Users input for output file name
    outputFileName = input('Please enter output file name:')
    
    # Use with statement to handle file easier, won't need file.close()
    with open(outputFileName, 'wb') as file:
        PdfFileWriter().write(file)
    
    # Break main loop, program finished
    break
# By: Leonardo Rueda

