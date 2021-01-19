#-----------------------------------------------------
# Example code to read from fixed length records (random access file)
#-----------------------------------------------------
import sys
import random
import os.path


num_records = 93
record_size = 71
filename='input.txt'

def main():

	if not os.path.isfile(filename):
		print(filename, "not found")
		exit()
	
	else:


		record_num = num_records
		f = open('input.txt', 'r')
	
	
		print("\n\n------------- Testing getRecord ------------\n\n")
		
		
				# Record out of range
		Sucess = False
		record_num = num_records
		Record, Success  = getRecord(f, record_num)
		if Success:
			print("\nRecord 93:",Record,"\n")
		else:
			print("\nRecord ",record_num," out of range")
			print("could not get the record\n")
		
	
				# First record in the file
		Sucess = False
		record_num = 0
		Record, Success  = getRecord(f, record_num)
		if Success:
			print("Record ",record_num,": ",Record,"\n")
		else:
			print("could not get the record")
	
		
		
				# Last record in the file	
		Sucess = False
		record_num = num_records-1
		Record, Success  = getRecord(f, record_num)
		if Success:
			print("Record ",record_num,": ",Record,"\n")
		else:
			print("could not get the record")
			
			
				# Some other record in the file
		Success = False
		record_num=5
		Record, Success  = getRecord(f, record_num)
		if Success:
			print("Record ",record_num,": ",Record,"\n")
		else:
			print("Could not get the record")
		
		
		
		
		print("\n\n------------- Testing binarySearch ------------\n\n")

		
				# Non-existant Record
		ID = '00100'
		Record, Middle = binarySearch(f, ID)
		if Record is not -1:
			print("ID ",ID,"found at Record",Middle)
			print("Record", middle,":", Record,"\n")
		else:
			print("ID",ID,"not found in our records\n")
		
		
				# First record
		ID = '00000'
		Record, Middle = binarySearch(f, ID)
		if Record is not -1:
			print("ID ",ID,"found at Record",Middle)
			print("Record", middle,":", Record,"\n")
		else:
			print("ID",ID,"not found in our records\n")
		
				# Last record 	
		ID = '00099'
		Record, Middle = binarySearch(f, ID)
		if Record is not -1:
			print("ID ",ID,"found at Record",Middle)
			print("Record", middle,":", Record,"\n")
		else:
			print("ID",ID,"not found in our records\n")
	
				# Some other record
		ID ='00006'
		Record, Middle = binarySearch(f, ID)
		if Record is not -1:
			print("ID ",ID,"found at Record",Middle)
			print("Record", middle,":", Record,"\n")
		else:
			print("ID",ID,"not found in our records\n")
	
	
		f.close()   #close the file when done
	


# Get record number n (Records numbered from 0 to NUM_RECORDS-1) 
def getRecord(f, recordNum):

	record = ""
	global num_records
	global record_size
	Success = False
	
	if recordNum >= 0 and recordNum < num_records:
		f.seek(0,0)
		f.seek(record_size * recordNum) #offset from the beginning of the file
		record = f.readline()
		Success = True
	#f.close()
	return " ".join(record.split()), Success


# Binary Search by record id
def binarySearch(f, name):
	global middle
	global num_records,record_size
	low=0
	high=num_records-1
	Found = False
	Success = False

	while not Found and high >= low:
		middle = (low+high) // 2
		#middle = low + (high-low) // 2
		record, Success = getRecord(f, middle)
		middleid = record.split()
		middleidnum = middleid[0]
		if middleidnum == name:
			Found = True
		if middleidnum < name:
			low = middle+1
		if middleidnum > name: 
			high = middle-1
	
	if(Found == True):
		return record, middle # the record number of the record
	else:
		return -1, middle
	
main()