# TO READ A FILE

# file_open = open('day_49\sample.txt') # If you don't enter the read mode the python by default read it because the read mode is the default value. 

# file_open = open('day_49\sample.txt', 'r' ) # to read the txt file
# file_open = open('day_49\index.html', 'r' ) # to read the html file

# r = reading , w = writing , a = appending , x = create

# text_read = file_open.read()
# print(text_read)




# TO CREATE A FILE AND WRITE SOMETHING

# use the a which mean append if you use the w for write so you must be need to add the file.close() to properly write the data inside file.
# file_write = open("day_49\write.txt", "a" ) # first open the file then we move on.

# file_write.write("\nhi i add some text by the help of the write function.") # then add the data or write something in it.
# load = open("day_49\write.txt","r")# then after writing we open again the file again for reading not writing
# read = load.read() # by read function we read it
# print(read) # and print the data inside the file




# READ A PHOTO

# with open("day_49\img.jpg", "rb") as f:
#     while True:
#         byte = f.read(1)
#         if not byte:
#             break
#         print(byte)

# you can never see the actual photo formate in your terminal it's only the binary data that you ge from this function other wise if you want to get the visuall formate of it you must be need to go with a any library like matplotlib,opencv etc        




# ANOTHER WAY TO WRITE OF READ

with open('day_49\sample.txt',"r") as f:# write whatever you want to do with file like read,write,append etc...
    read = f.read()
    print(read)
    # by this way you have'nt worry about the file close and some other stuff 





