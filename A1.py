####################
# Date: 1/19/2021
# Authors: Riley Nadwodny & Daniel Miao
# Description: Implements a simple database using a sorted file of fixed length records.
# The files used are "Parks.csv" and "Parks2.csv". The goal of this assignment is to
# understand and practice using file management techniques to implement a database system.
# Parks.config contains useful data like names of the fields and the number of records.
# Parks.data contains the data records with one record per line and fixed size fields.
#
####################

import sys
import random
import os.path
import csv

def main():
    # While loop for menu; until the user selects "Exit", loop through the menu.
    # Users can select any number from 1-8 and be brought back to the menu. 
    # Picking 9 will break the loop and exit the program. 
    # Any value < 1 or > 9 will result in the user being told to try again.
    loop = True
    while loop:
        printMenu()
        choice = int(input("Please select a menu option [1-9]: "))
        if choice == 1:
            print("Create database selected")
            createDB()
        elif choice == 2:
            print("Open database selected")
            openDB()
        elif choice == 3:
            print("Close database selected")
            closeDB()
        elif choice == 4:
            print("Display record selected")
            displayRecord()
        elif choice == 5:
            print("Update record selected")
            updateRecord()
        elif choice == 6:
            print("Create report selected")
            createReport()
        elif choice == 7:
            print("Add record selected")
            addRecord()
        elif choice == 8:
            print("Delete record selected")
            deleteRecord()
        elif choice == 9:
            loop = False
            quit()
        else:
            print("""Invalid option selection. Please try again. 
            """)



# Print menu to the user
def printMenu():
    print("""Please select a menu option from the following: 
    1. Create a new database
    2. Open database
    3. Close database
    4. Display record
    5. Update record
    6. Create report
    7. Add record
    8. Delete record
    9. Quit""")



# User can create a new database
def createDB():
    # Prompt user for the name of a .csv file. Return name to user
    fileName = input("Name of your file (including .csv): ")
    print("File selected: " + fileName)

    # Create new .config file to store info about the database
    f = open("Parks.config", "w")

    # Create new .data file to store data in
    f2 = open("Parks.data", "w")
    fields = []

    # Blank record with no delimiters
    blank = ['', '', '', '', '', '', '']

    # Delimiter used will be '!'
    
    # Reading csv file 
    with open(fileName, 'r') as csvfile: 
        # Creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        
        # Extracting field names through first row 
        f.write("Fields:")
        fields = next(csvreader)
        for field in range(len(fields)):
            f.write(" " + fields[field])
    
        # Extracting each data row one by one, adding delimters where necessary
        for row in csvreader: 
            if len(row[4]) < 90:
                row[4] = row[4].ljust(90, '!')
            if len(row[5]) < 40:
                row[5] = row[5].ljust(40, '!')
            if len(row[6]) < 9:
                row[6] = row[6].ljust(9, '!')
            f2.write(str(row) + "\n")
            f2.write(str(blank) + "\n")
    
        # Get total number of rows and write to .config
        print("Total no. of rows: %d"%(csvreader.line_num))
        f.write("\n")
        f.write("Total no. of rows: %d"%(csvreader.line_num * 2)) 



def openDB():
    pass



def closeDB():
    pass



def displayRecord():
    pass



def updateRecord():
    pass



def createReport():
    pass



def addRecord():
    pass



def deleteRecord():
    pass



def quit():
    print("Goodbye! :)")
    exit()

    

if __name__ == "__main__":
    main()