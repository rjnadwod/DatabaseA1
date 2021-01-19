import sys
import random
import os.path
import csv

def main():
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

#Print menu to the user
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

#User can create a new database
def createDB():
    #Prompt user for the name of a .csv file. Return name to user
    fileName = input("Name of your file (including .csv): ")
    print(fileName)

    # initializing the titles and rows list 
    fields = [] 
    rows = [] 
    
    # reading csv file 
    with open(fileName, 'r') as csvfile: 
        # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
        
        # extracting field names through first row 
        fields = next(csvreader) 
    
        # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
    
        # get total number of rows 
        print("Total no. of rows: %d"%(csvreader.line_num)) 

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