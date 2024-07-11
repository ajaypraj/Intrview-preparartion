#WAP to learn difference of a+, r+ and w+
# what are various ways to open the file
# what are various mode to open the file
# how to move cursor position
# How to read binary files
"""
Mode	File Exists	               File Doesn't Exist	    Pointer Position	    Truncate Existing Content	       Read	Write
r+	    Open file	               Error	                Beginning	            No	                             Yes	Yes
a+	    Open file	               Create new file	      End	                  No	                             Yes	Yes
w+	    Open file and truncate	 Create new file	      Beginning	            Yes	                             Yes	Yes
""" 

# r mode --> open existing file for read operation

f=open('abc.txt','r')

print(f.readlines())  # it will print the all lines in  list
# ['oslmfwsnknwdnknqniqndqdqjmqadw'] it will print entire content in list
f.seek(0)  # It will move the cursor to the line 0
print(f.readline())   # It will read the one line 
f.seek(0)
print("below line will print output of f.read()")
print(f.read())
# it will print line by line
['oslmfwsnknwdnknqniqndqdqjmqadw\n', 'wjfowejo\n', 'woifjwoj\n', '\n', 'iwjhwj']

print("It will print the readline")
f.seek(0)
print(f.readline())  #only one line is printed oslmfwsnknwdnknqniqndqdqjmqadw
f.close()

# write operation 
# Lets try to write a file which does not exits

# 'w' mode will create the file if it does not exists 
f=open("write_file.txt",'w')
f.write("This is first line written to the file")
f.close()
# Lets try to again write to the same file and it will overwrite the content
# There is no method as writeline
f=open('write_file.txt','w')
f.write('This is second line written to the file \n') 
f.writelines(['AJay \n','Fortune \n','500 \n','list company \n'])
f.write("Third lines added \n")
f.close()
#Writing code to understand the append operation
f=open('append_file','a')  # if file does not existing it will create the file
f.write("HI I am append file operation")
f.close()

# let again open the same file and see the content 
f=open('append_file','a')
f.write("Appending the file to the content \n")
f.writelines(['This is list \n','data added at the second lines \n'])
f.close()

# r+ mode 
# if file must exists else FileNotFound Error
# it will be used to read and write file
# File pointer is placed at beginning of file and allow you to read and write from beginning of the file

print("demo of r+ mode")
f.close()
f=open('abc.txt','r+')
# f=open('pqr.txt','r+') if the file is not there then it will thorw the error

# print(f.readline())
f.writelines(['new lines are added \n','Are you okay with it ?\n'])
f.seek(0)
print(f.readlines())
f.close()
# w+ mode
print("Demo of w+ mode")
# Opens a file for both read and write , if file  does not exits it will create it
# If file already existed its content will be truncated
# the file pointer is palced at beginning of the file 
# Allow you to read and write from file , but previous content is lost
a=open("abc.txt",'w+')
print(a.readlines())  #  []

a.write("Ajay \n")
a.writelines(['SIHDIS \n','nosjdos\n'])
a.seek(0)
print(a.readlines())







