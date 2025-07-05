#f=open("Hello.txt","x") # x mode is used to create a new file, if the file already exists it will raise an error
'''
r=open("Hello.txt","r") # r mode is used to read the file
content=r.read() # read the content of the file
r.close() # close the file after reading
print(content) # print the content of the file

f=open("File2.txt","w") # w mode is used to write the file, if the file already exists it will overwrite the file
f.write("Hello, World!") # write the content in the file
f.close() # close the file after writing
r=open("File2.txt","r") # r mode is used to read the file
content=r.read() # read the content of the file
r.close() # close the file after reading
print(content) # print the content of the file

try:
    r=open("File3.txt","r") # r mode is used to read the file
    content=r.read() # read the content of the file
    r.close() # close the file after reading
    print(content) # print the content of the file

except FileNotFoundError:
    print("File is not there, creating a new file")
   
f=open("File3.txt","a") # w mode is used to write the file, if the file already exists it will overwrite the file 
f.write("Hello, World!") # write the content in the file
f.close() # close the file after writing
try:
    r=open("File3.txt","r") # r mode is used to read the file
    content=r.read() # read the content of the file
    r.close() # close the file after reading
    print(content) # print the content of the file

except FileNotFoundError:
    print("File is not there, creating a new file")'''
    
    
'''import os
print(os.path.exists("File4.txt")) # check if the file exists or not Boolean value
#os.remove("File.txt") # remove the file if it exists

#os.rename("calculator.py","calc.py") # rename the file if it exists'''
'''with open("arthur_lewin.jpg","rb") as f: # rb mode is used to read the file in binary mode
    content=f.read() # read the content of the file
print(content) # print the content of the file
    
with open("Arthur_lewin.jpg","wb") as f: # wb mode is used to write the file in binary mode
    f.write(content) # write the content in the file

#os.rename("new_picture.jpg","arthur_lewin.jpg") # rename the file if it exists
with open("filereadandwrite.txt","a+") as f: # w mode is used to write the file
    f.write("Hello, World!") # write the content in the file
    
'''

try:
    with open("missing_file.txt", "r") as f:
        data = f.read()
except FileNotFoundError:
    print("missing_file.txt not found.")
except IOError:
    print("An I/O error occurred.")