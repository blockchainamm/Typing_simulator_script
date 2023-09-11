from pynput.keyboard import Controller
import time
import os
from pathlib import Path

# Function to check if file exists in the current working directory
def check_file(file):
    # Get current working directory
    current_dir = os.getcwd()

    #print(current_dir)

    path = os.path.join(current_dir, file)

    # Check whether the specified
    # path exists or not
    isExist = os.path.exists(path)
    #print(isExist)
    return isExist

# Function to simulate text typing
def simTyping(data):
    keyboard = Controller()

    time.sleep(2)

    for char in data:
        keyboard.press(char)
        keyboard.release(char)
        time.sleep(0.05)

# Check file existence and call function to simulate text typing in file has .txt extension
def checktyping():
    # Take the name of the file from user and assign it to a variable image
    file = input("Enter file with text to simulate typing: ")
    print(f"The file name which you entered is: {file}" )
    
    # Check if the file exists in the current directory
    existcheck = check_file(file)

    # If the file exists then simulate typing
    if existcheck:
       
       if Path(file).suffix == '.txt':
            #pass
            #open text file in read mode
            text_file = open(file, "r")
            
            #read whole file to a string
            data = text_file.read()
            
            print(data)
            simTyping(data)

            #close file
            text_file.close()
       else:
            print(f'File {file} foes not have a .txt extention')
    
    else:
        print(f'File {file} not found in directory ', os.getcwd())
       
# Call function to simulate text typing
checktyping()