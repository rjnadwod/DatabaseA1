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
    db = pyDatabase()
    loop = True
    while loop:
        db.printMenu()
        choice = int(input("Please select a menu option [1-9]: "))
        if choice == 1:
            print("Create database selected\n")
            db.createDB()
        elif choice == 2:
            print("Open database selected\n")
            db.openDB()
        elif choice == 3:
            print("Close database selected\n")
            db.closeDB()
        elif choice == 4:
            print("Display record selected\n")
            db.displayRecord()
        elif choice == 5:
            print("Update record selected\n")
            db.updateRecord()
        elif choice == 6:
            print("Create report selected\n")
            db.createReport()
        elif choice == 7:
            print("Add record selected\n")
            db.addRecord()
        elif choice == 8:
            print("Delete record selected\n")
            db.deleteRecord()
        elif choice == 9:
            loop = False
            db.quit()
        else:
            print("""Invalid option selection. Please try again. 
            """)


class pyDatabase:

    f = None
    f2 = None

    # Print menu to the user
    def printMenu(self):
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
    def createDB(self):
        # Prompt user for the name of a .csv file. Return name to user
        fileName = input("Name of your file (including .csv): ")
        print("File selected: " + fileName)

        # Create new .config file to store info about the database
        self.f = open("Parks.config", "w")

        # Create new .data file to store data in
        self.f2 = open("Parks.data", "w")
        fields = []

        # Blank record with no delimiters
        blank = ['', '', '', '', '', '', '']

        # Delimiter used will be '!'
        
        # Reading csv file 
        with open(fileName, 'r') as csvfile: 
            # Creating a csv reader object 
            csvreader = csv.reader(csvfile) 
            
            # Extracting field names through first row 
            self.f.write("Fields: ")
            fields = next(csvreader)
            for field in range(len(fields)):
                self.f.write(fields[field] + ", ")
        
            # Extracting each data row one by one, adding delimters where necessary
            for record in csvreader: 
                if len(record[4]) < 90:
                    record[4] = record[4].ljust(90, '!')
                if len(record[5]) < 40:
                    record[5] = record[5].ljust(40, '!')
                if len(record[6]) < 9:
                    record[6] = record[6].ljust(9, '!')
                self.f2.write(str(record) + "\n")
                self.f2.write(str(blank) + "\n")
        
            # Get total number of records and write to .config
            print("Total no. of records: %d"%(csvreader.line_num))
            print("")
            self.f.write("\n")
            self.f.write("Total no. of records: %d"%(csvreader.line_num * 2)) 



    def openDB(self):
        if (self.f.closed == True and self.f2.closed == True):
            dbName = input("Name of database to open: ")
        else:
            print("Please close the currently open database files.")
            print("Returning to main menu.\n")



    def closeDB(self):
        if (self.f.closed != True and self.f2.closed != True):
            print(str(self.f.name) + " and " + str(self.f2.name) + " are currently open. Closing files now. Please wait.")
            self.f.close()
            self.f2.close()
            print("Files have been closed. Returning to main menu.\n")
        else:
            print("All database files are currently closed.\n")



    def displayRecord(self):
        pass



    def updateRecord(self):
        pass



    def createReport(self):
        pass



    def addRecord(self):
        pass



    def deleteRecord(self):
        pass



    def quit(self):
        print("Goodbye! :)")
        exit()

    

if __name__ == "__main__":
    main()