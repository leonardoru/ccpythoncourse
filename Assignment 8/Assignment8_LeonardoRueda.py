# Class: CIS 112 #37791 ADVANCED PROGRAMMING USING PYTHON-Online
# Pasadena City College
# Instructor: Mr. Jason Y. Huh
# Assignment 8: Write a Python program which concatenates three PDF files together and name merged file as "MergedFile.pdf".
# Student: Leonardo Rueda

# First we import PyPDF2
import PyPDF2
from PyPDF2 import PdfFileReader,PdfFileMerger
from pathlib import Path
 
# Create PdfFileMerger object from PyPDF2
MergerObject = PdfFileMerger( strict=False )

# Get Current Working Directory using pathlib
PDF_paths = Path.cwd()

# Count var
filesCount = 0

# Iterate trough files ending in .pdf
for path in PDF_paths.glob("*.pdf"):
    # print(path.name)
    MergerObject.append(PdfFileReader(path.name, 'rb'))
    filesCount += 1

# If there is less than 2 pdf files in this folder...
if filesCount <= 1:
    print(" At least 2 pdf files need to be in the same folder this python file exists in order to conactenate them. ")

# Else merge the files  
else:
    # Here we are writing the Merged files to a pdf named as MergedFile.pdf
    MergerObject.write("MergedFile.pdf")

    # Here we let the user know that the PDF's were merged succesfully
    print(str(filesCount) + " PDF's were merged successfully!, please check the MergedFile.pdf file.")

# By Leonardo Rueda CIS 112