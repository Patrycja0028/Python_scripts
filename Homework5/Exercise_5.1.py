# For a given directory (top) find the number of bytes taken by PDF files in the directory tree (".pdf" extensions).
#The code should be in the function find_pdf_size(top). In order to test the current directory we run find_pdf_size("."). 

import os

def find_pdf_size(top):
    total_size = 0
    
    for root, dirs, files in os.walk(top):
        for file in files:
            if file.lower().endswith(".pdf"):
                file_path = os.path.join(root, file)
                try:
                    total_size += os.path.getsize(file_path)
                except OSError:
                    pass 
    
    return total_size

# test
top = "D:\\Desktop"

print(find_pdf_size(top))
