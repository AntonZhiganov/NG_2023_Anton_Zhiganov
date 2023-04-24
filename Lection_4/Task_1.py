import argparse
import os

#For the program to work, enter the name of the file and the folder
#in which you want to search for it, like this: 
#python Task_1.py --folder (your folder)r --file (your file)

# Create a command line argument parser

pars = argparse.ArgumentParser(description = 'Searching for files in a folder, and in folders of folders')

pars.add_argument('--folder', type = str, help = 'Folder to search in', required = True)
pars.add_argument('--file', type = str, help = 'File name to search for', required = True)

# Search the files

def findFile (folder, filename) :
    
    for root, dirs, files in os.walk(folder) :
        
        for f in files :
            
            if f == filename :
                
                if os.path.isfile(os.path.join(root, file)) :
                
                    print(os.path.join(root, file))
                
                else :
                    
                    print ("Error {} is not a file".format (os.path.join(root, filename)))
                
# Get command line arguments

arguments = pars.parse_args()

# Using arguments to find files

folder = arguments.folder

file = arguments.file

# Find files in folder

findFile(folder, file)

