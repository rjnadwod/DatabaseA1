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
    # Makes sure the script is run with Python3
    assert sys.version_info >= (3,), "Python version too low. Run with python3"

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
    # Class variables for functions to utilize
    f = None
    f2 = None
    numRecords = 0
    recordSize = 162
    recordFields = ""

    # Blank record with no delimiters
    # Delimiter used will be ' '
    blank = "                                                                                                                                                                 "

    # Print menu to the user
    def printMenu(self):
        print("""Please select a menu option from the following: 
        1. Create a new database
        2. Open database (Must create a database first)
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
        fileName = input("Name of your file: ")
        fileName = fileName + ".csv"
        print("File selected: " + fileName)

        # Check for the file; if it is not found, exit the program
        if not os.path.isfile(fileName):
            print(fileName, "not found. Exiting now.")
            exit()

        else:
            # If file is found, let user know and create database 
            print(fileName, "found. Creating database.")

            # Create new .config file to store info about the database
            self.f = open("Parks.config", "r+")

            # Create new .data file to store data in
            self.f2 = open("Parks.data", "r+")

            # Create list to hold the field names in
            fields = []

            # Reading csv file 
            with open(fileName, 'r') as csvfile:
                # Creating a csv reader object 
                csvreader = csv.reader(csvfile)

                # Extracting field names through first row 
                self.f.write("Fields: ")
                fields = next(csvreader)
                for field in range(len(fields)):
                    self.f.write(fields[field] + ", ")
                    self.recordFields = self.recordFields + fields[field]

                # Extracting each data row one by one, adding delimters where necessary
                for record in csvreader:
                    # Add delimiters to the ID
                    if len(record[0]) < 7:
                        record[0] = record[0].ljust(7, ' ')
                    # Add delimiters to the name
                    if len(record[4]) < 90:
                        record[4] = record[4].ljust(90, ' ')
                    # Add delimiters to the type
                    if len(record[5]) < 40:
                        record[5] = record[5].ljust(40, ' ')
                    # Add delimiters to the visitors
                    if len(record[6]) < 10:
                        record[6] = record[6].ljust(10, ' ')

                    # Join the list together into a string
                    str1 = ' '.join(record)

                    # Write a single record to Parks.data
                    self.f2.write(str1 + "\n")

                    # Write a blank record to Parks.data between each record
                    self.f2.write(self.blank + "\n")

                # Get total number of records and write to .config
                print("Parks.config and Parks.data created. Name of database is 'Parks'")
                print("Total number of records: %d" % (csvreader.line_num))
                self.f.write("\n")
                self.f.write("Total no. of records: %d" % (csvreader.line_num))
                self.numRecords = csvreader.line_num

            print("Closing database.\n")
            self.f.close()
            self.f2.close()

    def openDB(self):

        # If there are no databases currently open, ask user for database to open
        if (self.f.closed == True and self.f2.closed == True):
            dbName = input("Name of database to open: ")

            # If the database is not found, exit
            if not os.path.isfile(dbName + ".data"):
                print(dbName, "database not found. Exiting now.")
                exit()

            else:
                # If file is found, let user know and open database 
                print(dbName, "database found. Opening database.")
                self.f = open("Parks.config", "r")
                self.f2 = open("Parks.data", "r+")
                print(str(self.f.name) + " and " + str(self.f2.name) + " have been opened.\n")

        # If there is a database currently open, prompt user to close them and try again
        else:
            print("There are database files currently open. Please close them and try again.")
            print("Returning to main menu.\n")
            return

    def closeDB(self):

        # If there is a database currently open, close the database
        if (self.f.closed != True and self.f2.closed != True):
            print(
                str(self.f.name) + " and " + str(self.f2.name) + " are currently open. Closing files now. Please wait.")
            self.f.close()
            self.f2.close()
            print("Files have been closed. Returning to main menu.\n")
            return

        # If there is no database currently open, let the user know
        else:
            print("All database files are currently closed.\n")
            return

    def displayRecord(self):

        # Variable to store a record into from the .data file
        storedRecord = ""

        if (self.f.closed == True and self.f2.closed == True):
            print("No database files open. Please open files before searching for a record.\n")
            return
        else:
            # Get record ID from user to search with
            recordID = input("Enter record ID to search: ")

            # Cast recordID with int() to make sure it is >= 0 and less than numRecords
        if int(recordID) >= 0:
            storedRecord, middle = self.binarySearch(recordID)

            if storedRecord != -1:
                # Print record with field names; remove delimiters from the record.
                # A blank record will print with blanks in every field
                print("ID ", recordID, "found at Record", middle)
                print(self.recordFields[0:2] + ': ' + storedRecord[:7].strip(' '))
                print(self.recordFields[2:8] + ': ' + storedRecord[8:10].strip(' '))
                print(self.recordFields[8:13] + ': ' + storedRecord[11:13].strip(' '))
                print(self.recordFields[13:17] + ': ' + storedRecord[14:18].strip(' '))
                print(self.recordFields[17:21] + ': ' + storedRecord[19:109].strip(' '))
                print(self.recordFields[21:25] + ': ' + storedRecord[110:150].strip(' '))
                print(self.recordFields[25:33] + ': ' + storedRecord[151:160].strip(' '))
                print("")
            else:
                print("ID", recordID, "not found in our records\n")
        else:
            print(recordID + " is out of bounds.")

    def updateRecord(self):

        # Variable to store a record into from the .data file
        storedRecord = ""

        if (self.f.closed == True and self.f2.closed == True):
            print("No database files open. Please open files before searching for a record.\n")
            return
        else:
            # Get record ID from user to search with
            recordID = input("Enter record ID to update: ")
            print("")

            # Cast recordID with int() to make sure it is >= 0
        if int(recordID) >= 0:
            storedRecord, middle = self.binarySearch(recordID)

            record = [storedRecord[:7], storedRecord[8:10], storedRecord[11:13], storedRecord[14:18],
                      storedRecord[19:109], storedRecord[110:150], storedRecord[151:160]]

            if storedRecord != -1:
                # Print record with field names; remove delimiters from the record.
                # A blank record will print with blanks in every field
                print("ID ", recordID, "found at Record", middle)
                print(self.recordFields[0:2] + ': ' + record[0])
                print(self.recordFields[2:8] + ': ' + record[1])
                print(self.recordFields[8:13] + ': ' + record[2])
                print(self.recordFields[13:17] + ': ' + record[3])
                print(self.recordFields[17:21] + ': ' + record[4])
                print(self.recordFields[21:25] + ': ' + record[5])
                print(self.recordFields[25:33] + ': ' + record[6])
                print("")

                fieldToUpdate = input("Select field to update: ")

                if fieldToUpdate == "ID":
                    print("Field 'ID' cannot be changed. Returning to main menu.")
                    return
                elif fieldToUpdate == "Region":
                    newRegion = input("Enter region: ")
                    record[1] = newRegion
                elif fieldToUpdate == "State":
                    newState = input("Enter state: ")
                    record[2] = newState
                elif fieldToUpdate == "Code":
                    newCode = input("Enter code: ")
                    record[3] = newCode
                elif fieldToUpdate == "Name":
                    newName = input("Enter name: ")
                    if len(newName) < 90:
                        newName = newName.ljust(90, ' ')
                    record[4] = newName
                elif fieldToUpdate == "Type":
                    newType = input("Enter type: ")
                    if len(newType) < 40:
                        newType = newType.ljust(40, ' ')
                    record[5] = newType
                elif fieldToUpdate == "Visitors":
                    newVisitors = input("Enter visitors: ")
                    if len(newVisitors) < 10:
                        newVisitors = newVisitors.ljust(10, ' ')
                    record[6] = newVisitors[:9]

                str1 = ' '.join(record)
                self.findRecord(middle)
                self.f2.write(str1)

                print("Record updated. Closing database files.\n")
                self.f.close()
                self.f2.close()

            else:
                print(recordID + " is out of bounds.")

        else:
            print(recordID + " is out of bounds.")

    def createReport(self):

        success = False

        # Check to make sure the file is readable before creating report
        print("Making sure files are readable.")
        if (self.f.closed == True and self.f2.closed == True):
            print("Please open database before creating report.\n")
            return

        # Create and open file to write the first 10 records to as a "report"
        print("Creating report.txt.")
        report = open("report.txt", "w")

        i = 0
        fields = self.f.readline()
        fields = fields.replace(", ", '  ')
        report.write(fields)
        while i < 10:
            recordStr = self.f2.readline()
            # Write the record to the report if it is not blank
            # Increment i by 1 as the operation is successful
            if (recordStr[0:7] != '       '):
                report.write(recordStr)
                i += 1
                success = True
            else:
                i += 0

        if success == True:
            print("Report successfully generated. Returning to main menu.\n")

    def addRecord(self):
        # Check to make sure the file is readable before creating report
        print("Making sure files are writable.")
        if (self.f.closed == True and self.f2.closed == True):
            print("Please open database before creating report.\n")
            return

        # Ask for user inputs for fields
        newID = input("New Record's ID: ").ljust(7, ' ')
        newRegion = input("New Record's Region: ")
        newState = input("New Record's State: ")
        newCode = input("New Record's Code: ")
        newName = input("New Record's Name: ").ljust(90, ' ')
        newType = input("New Record's Type: ").ljust(40, ' ')
        newVisitors = input("New Record's Visitors: ").ljust(10, ' ')

        newRec = [newID, newRegion, newState, newCode, newName, newType, newVisitors]
        rec = ' '.join(newRec)

        tmpRec, idx = self.binarySearch(newID)

        if tmpRec == self.blank:
            print("writing")
            self.f2.seek(0, 0)
            self.f2.seek(self.recordSize * idx)
            self.f2.write(rec)
        else:
            print("Reformatting")
            self.f2.seek(0, 0)
            #Copy whatever line is currently Here
            self.f2.seek(self.recordSize * idx)
            self.f2.write(self.blank + "\n")

        print("Closing database.")
        self.f.close()
        self.f2.close()

    def deleteRecord(self):

        if (self.f.closed == True and self.f2.closed == True):
            print("No database files open. Please open files before searching for a record.\n")
            return

        blank = "                                                                                                                                                                 "

        # Id to be deleted
        delID = int(input("Input Record ID to be deleted: "))

        # Find ID Line to be deleted

        tempRec, index = self.binarySearch(delID)

        # Delete Line
        print("Deleting Line")
        self.f2.seek(self.recordSize * index)
        self.f2.write(self.blank)

        return

    def quit(self):
        print("Goodbye! :)")
        exit()

    # Function to use seeks to find the record
    def find(self, ID):

        storedRecord = ""
        Success = False

        if ID >= 0 and ID < self.numRecords:
            self.findRecord(ID)  # Offset from the beginning of the file
            storedRecord = self.f2.readline()
            Success = True

        return storedRecord, Success

    # Binary Search by record ID
    def binarySearch(self, ID):
        global middle
        low = 0
        high = self.numRecords - 1
        Found = False
        Success = False

        while not Found and high >= low:
            middle = (low + high) // 2
            record, Success = self.find(middle)
            middleid = record[:7]
            middleidnum = middleid.strip(' ')

            if middleidnum == '':
                record, Success = self.find(middle - 1)
                middleid = record[:7]
                middleidnum = middleid.strip(' ')

            if middleidnum == ID:
                Found = True
            elif int(middleidnum) < int(ID):
                low = middle + 1
            elif int(middleidnum) > int(ID):
                high = middle - 1

        if (Found == True):
            return record, middle
        else:
            return self.blank, middle

    def findRecord(self, id):
        self.f2.seek(0, 0)
        self.f2.seek(self.recordSize * id)


if __name__ == "__main__":
    main()
