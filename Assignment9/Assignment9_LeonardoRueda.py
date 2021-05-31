# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYTHON-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Assignment 9: Create a Python program which merges two files together in the right order of pages
# Student: Leonardo Rueda

# First we import PyPDF2 and related
import PyPDF2
from PyPDF2 import PdfFileReader,PdfFileMerger
from pathlib import Path
 
 # Open the files that have to be merged
file1 = open('pythonlearn_ch8MissingPages.pdf', 'rb')
file2 = open('From_pythonlearn_ch8.pdf', 'rb')

 
# Here we create 2 objects that are reading the files so we can access the pageNum and other properties
readerFile1 = PyPDF2.PdfFileReader(file1)
readerFile2 = PyPDF2.PdfFileReader(file2)

# Create a new PdfFileMergerobject which represents a blank PDF document
newDocument = PyPDF2.PdfFileMerger()

# I initially thought of this approach which does not use pdfMerger Object 
# # Loop through the page numbers 1 to 4 as our document is 12 pages
# for pageNumber in range(4):
#     pageObj = readerFile1.getPage(pageNumber)
#     newDocument.addPage(pageObj)
 
# # Loop through all the page numbers for the second document
# for pageNumber in range(readerFile2.numPages):
#     pageObj = readerFile2.getPage(pageNumber)
#     newDocument.addPage(pageObj)

# # Loop through remaining all page
# for pageNumber in range(4,readerFile1.numPages):
#     pageObj = readerFile1.getPage(pageNumber)
#     newDocument.addPage(pageObj)

# But, the following code is a better way of doing it, shorter and more beautifull
# - Used PDF Merger to append docs based on the pages that need to be included
# 1 - First the pages 0 to 4 from document #1
newDocument.append(file1, pages=(0,4))
# 2 - Then the full document #2 with the missing pages
newDocument.append(file2 )
# 3 - Finally the rest of the fisrt document #1
newDocument.append(file1, pages=(4,readerFile1.numPages))
 
# Now we have merged the pages properly let's write this in a new file
outFileObj = open('mergedDocument.pdf', 'wb')
newDocument.write(outFileObj)
 
# Close all the files 
outFileObj.close()
file1.close()
file2.close()

# By: Leonardo Rueda