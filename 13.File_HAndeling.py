#f=open("Hello.txt","x") # x mode is used to create a new file, if the file already exists it will raise an error
r=open("Hello.txt","r") # r mode is used to read the file
content=r.read() # read the content of the file
r.close() # close the file after reading
print(content) # print the content of the file