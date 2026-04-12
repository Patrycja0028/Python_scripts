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


print(find_pdf_size("."))
