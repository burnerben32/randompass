#DEV INFO
#all the commented print statements are debug functions i used during development
#feel free to uncomment them to better understand the function of this
#if you'd like to add debugs to the randompass_user.py feel free because i wont.
#in my opinion they're not yet needed as simple as that code is.
#but if you'd like to id appreciate it.
#COMMENT INFO
#the comment under a line will always be the one that applies never above.
#but generally the comments will be beside code.
#all underneath comments will use three hashtags ### as to not be confused with debug code.
#LAST BUT NOT LEAST
#read the readme and architecture docs in the repository if you have not already.
#that is if you wanna have a good time.
#if you don't read the docs you'll have a bad time.
#also
#if you don't use the program learning the ins and out of how it functions before
#cracking open the code you're gonna have a bad time.
#seriously.
#do it.

import sys
import secrets

argv_length = len(sys.argv) #gets length of the command line arguments and puts that number in argv_length

#print(sys.argv)
#print("0 " + sys.argv[0])
#print("1 " + sys.argv[1])
#print("2 " + sys.argv[2])
#print("3 " + sys.argv[3])
#print("4 " + sys.argv[4])
#print("5 " + sys.argv[5])
#print("6 " + sys.argv[6])

if argv_length > 1: #if there is more than 1 command line statement run the loop
    ###there will always be 1 command line argument that being randompass_commandline.py
    #print("argv is longer than 1")
    if sys.argv[1] == "-h": #if the first command line argument is -h (this excludes [0] mentioned on line 31)
        ###-h stands for help if that wasn't obvious
        print("-h : see help menu\n-b : length of desired password in bytes (example: -b 36)\n-f : format of desired password. 1 for hex password 2 for url_safe. (url_safe is the most secure)\n-s : destination to save password if desired. must use .txt extension (example:-s password.txt)\n")
        ###prints help info

    if sys.argv[1] == "-b": #if the first command line argument is -b. -b stands for bytes
        #print("sys.argv[1] is -b")
        bytes = sys.argv[2] #sets bytes to the second argument
        #print("this is bytes " + bytes)

    if sys.argv[1] == "-f": #if the first command line argument is -f. -f stands for format
        #print("sys.argv[1] is -f")
        format = sys.argv[2] #sets format to second argument
        #print("this is format " + format)

    if sys.argv[1] == "-s": #if the first command line argument is -s. -s stands for save
        #print("sys.argv[1] is -s")
        file_choice = "y" #sets file_choice to y respresenting yes or true
        #print("this is file_choice " + file_choice)
        file_name = sys.argv[2] #file_name is equal to the second argument
        #print("this is file_name " + file_name)

    if sys.argv[3] == "-b": #if the third command line argument is -b
        #print("sys.argv[3] is -b")
        bytes = sys.argv[4] #sets bytes to the forth argument
        #print("this is bytes " + bytes)

    if sys.argv[3] == "-f": #if the third command line argument is -f
        #print("sys.argv[3] is -f")
        format = sys.argv[4] #sets format to the forth argument
        #print("this is format " + format)
    
    if sys.argv[3] == "-s": #if the third command line argument is -s
        #print("sys.argv[3] is -s")
        file_choice = "y" #set file_choice to y
        #print("this is file_choice " + file_choice)
        file_name = sys.argv[4] #set file_name to the forth argument
        #print("this is file_name " + file_name)

    if sys.argv[5] == "-b": #if the fifth command line argument is -b
        #print("sys.argv[5] is -b")
        bytes = sys.argv[6] #set bytes to the sixth argument
        #print("this is bytes " + bytes)

    if sys.argv[5] == "-f": #if the fifth command line argument is -f
        #print("sys.argv[5] is -f")
        format = sys.argv[6] #sets format to the sixth argument
        #print("this is format " + format)

    if sys.argv[5] == "-s": #if the fifth command line argument is -s
        #print("sys.argv[5] is -s")
        file_choice = "y" #sets file_choice to y
        #print("this is file_choice " + file_choice)
        file_name = sys.argv[6] #sets file_name to the sixth argument
        #print("this is file_name " + file_name)

    else: #if none of these apply the user messed the args and an error and help message are printed
        print("error: incorrect commandline arguments.\n-b, -f, or -s must be followed by their respective secondary arguments.\nexamples: -b 36 -f 2 -s password.txt\nuse the argument -h for the help menu")
else: #see 94
    print("error: incorrect commandline arguments.\n-b, -f, or -s must be followed by their respective secondary arguments.\nexamples: -b 36 -f 2 -s password.txt\nuse the argument -h for the help menu")
#print("end of argv loop")
if argv_length > 2: #if there is more than two args. if this wasn't here everytime you asked for -h(help) you'd get some tracebacks
    #print("start of password gen loop")
    if format == "1": #if the format is 1 aka hex
        bytes = int(bytes) #convert bytes from a string to an integer
        password = secrets.token_hex(bytes) #generate a hex password to length of bytes
        gen = 1 #set gen to 1 confirming a password was generated
        #print(gen)
    elif format == "2": #if the format is 2 aka url_safe
        bytes = int(bytes) #convert bytes from a string to an integer
        password = secrets.token_urlsafe(bytes) #generate a url_safe password to legnth of bytes
        gen = 1 #set gen to 1
        #print(gen)
    if gen == 1: #if gen is 1. confirming a password was generated
        print(password + "\n") #print the password
        if file_choice == "y": #if a file choice was made
            file = open(file_name, "x") #create the file for writing
            file.write(password) #writes the password
            file = open(file_name, "r") #reopens file with password now in it
            file_content = file.read() #sets file_content to contents of the file (duh)
            file.close() #closes the file
            if file_content == password: #confirms the file content is the same as the generated password
                print("password saved to file: " + file_name) #prints confirmation message
        print("press enter to quit.")
        input("")
        ###guess what this does (121 & 122) just guess really i believe in you