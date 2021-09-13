import secrets

#more dev info in the randompass_commandline.py file comments
#i highly recommend reading over randompass_commandline.py
#it will give you more dev info and info on how this program operates
#even if you are only doing dev for this file.

password = "" #sets password variable
print("Random Password Generator. Input byte length of desired password.\n") 
bytes = input("bytes: ") #input for bytes
print("\n")
bytes = int(bytes) #converts bytes from a string to an integer
print("Choose password format. 1 for hex password and 2 for url safe passwords, (hex is letters and numbers url safe has capital letters and url safe special chars)\n")
format = input("") #input for format of password
print("\n")
print("Output to file? answer YES or NO\n") #output to a file? YES or NO prompt
file_choice = input("")
if file_choice == "YES": #if the user said YES
    print("input desired file name (include .txt extension)\n") #prompt for file name
    file_name = input("")
print("\n")

if format == "1": #if the format is 1 (hex)
    password = secrets.token_hex(bytes) #generate hex password to desired length
elif format == "2": #if the format is 2 (url_safe)
    password = secrets.token_urlsafe(bytes) #generate url_safe password to desired length

print(password + "\n") #print password
if file_choice == "YES": #if the user wants to save to a file and said YES
    file = open(file_name, "x") #creates file for writing
    file.write(password) #writes password to file
    file = open(file_name, "r") #opens written file
    file_content = file.read() #copy's the contents of the file to file_content
    file.close() #closes file
    if file_content == password: #confirms the file has the same contents as password
        print("password saved to file: " + file_name) #print confirmation
print("press enter to quit.") #hmm i don't know what his part does...
input("") #this too...