# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:13:20 2023

@author: alexa
"""

import PyPDF2
import sys
import os

# WD
path = r"C:\Users\alexa\Documents\Studium\MSc (WU)\Macroeconometrics\Assignment 4" # r for raw string
path = path.replace("\\", "/")
os.chdir(path)

# Get Files
pdf_ls = []

for file in os.listdir(path):
    if file.endswith(".pdf"):
        print(file)
        pdf_ls.append(file)
        
 

# Merge       
merger = PyPDF2.PdfMerger()

for pdf in pdf_ls:
    merger.append(pdf)
    
file_name = "Merged_Test"
merger.write(file_name + ".pdf")
merger.close()



